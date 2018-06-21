## Linux socket编程

原文链接：http://www.cnblogs.com/skynet/archive/2010/12/12/1903949.html

### 1. 网络中进程之间如何通信？

##### 本地的进程间通信(IPC)

1. 消息传递（管道、FIFO、消息队列）
2. 同步（互斥量、条件变量、读写锁、文件和写记录锁、信号量）
3. 共享内存（匿名的和具名的）
4. 远程过程调用（Solaris门和Sun RPC）



* 首要问题：如何唯一标识一个进程？

  做法：本地可以通过进程PID来唯一标识一个进程，网络TCP/IP协议族使用三元组（IP地址，协议，端口）标识网络的进程

* 使用TCP/IP协议的应用程序通常采用应用编程接口：UNIX BSD的套接字（socket）和UNIX System V的TLI（已经被淘汰）



### 2. 什么是socket？

* socket：插座；窝，穴；把...装入插座；套接字
* socket起源于Unix，继承了Unix/Linux“一切皆文件”的基本哲学
* 打开open -> 读写write/read ->关闭close

### 3. socket的基本操作

#### 3.1 socket()函数

> int socket (int domain, int type, int protocol);

socket()函数对应于普通文件的打开操作，普通文件的打开操作返回一个文件描述字，而socket()用于创建一个socket描述符（socket descriptor），它唯一标识一个socket。

#### 3.2 bind()函数

> int bind (int sockfd, const struct sockaddr *addr, socklen_t addrlen);

bind()函数把一个地址族中的特定地址赋给socket。

通常服务器在启动的时候都会绑定一个众所周知的地址（如IP地址+端口号），用于提供服务，客户就可以通过它来连接服务器；客户端不用指定，由系统自动分配一个端口号和自身的IP地址组合。

~~~
网络字节序与主机字节序

主机字节序就是我们平常说的大端和小端模式：不同的CPU有不同的字节序类型，这些字节序是指整数在内存中保存的顺序，这个叫做主机序。引用标准的Big-Endian和Little-Endian的定义如下：

　　a) Little-Endian就是低位字节排放在内存的低地址端，高位字节排放在内存的高地址端。

　　b) Big-Endian就是高位字节排放在内存的低地址端，低位字节排放在内存的高地址端。

网络字节序：4个字节的32 bit值以下面的次序传输：首先是0～7bit，其次8～15bit，然后16～23bit，最后是24~31bit。这种传输次序称作大端字节序。由于TCP/IP首部中所有的二进制整数在网络中传输时都要求以这种次序，因此它又称作网络字节序。字节序，顾名思义字节的顺序，就是大于一个字节类型的数据在内存中的存放顺序，一个字节的数据没有顺序的问题了。

所以：在将一个地址绑定到socket的时候，请先将主机字节序转换成为网络字节序，而不要假定主机字节序跟网络字节序一样使用的是Big-Endian。由于这个问题曾引发过血案！公司项目代码中由于存在这个问题，导致了很多莫名其妙的问题，所以请谨记对主机字节序不要做任何假定，务必将其转化为网络字节序再赋给socket。
~~~

#### 3.3 listen()、connect()函数

> int listen (int sockfd, int backlog);
>
> int connect (int sockfd, const struct sockaddr *addr, socklen_t addrlen);

服务器在socket()、bind()之后就会调用listen()来监听socket，客户端调用connect()发出连接请求给服务器。

#### 3.4 accept()函数

> int accept (int sockfd, struct sockaddr *addr, socklen_t addrlen);

* TCP server依次调用socket()、bind()、listen()之后，就会监听指定的socket地址；

  TCP client依次调用socket()、connect()之后，就向TCP服务器发送了一个连接请求。

* TCP服务器监听到这个请求之后，就会调用accept()取接收请求，从而建立连接。

  之后就可以开始网络I/O操作，即类似于普通文件的读写I/O操作。

* 如果accept成功，那么其返回值是由内核自动生成的一个全新的描述字，代表与返回客户的TCP连接。

#### 3.5 read()、write()等函数

网络I/O操作：

* read()/write()
* recv()/send()
* readv()/writev()
* **recvmsg()/sendmsg()**
* recvfrom()/sendto()

> \# include <unistd.h>
>
> ssize_t read (int fd, void *buf, size_t count);
>
> ssize_t write (int fd, const void *buf, size_t count);
>
>  
>
> \#include <sys/types.h>
>
> \#include <sys/socket.h> 
>
> ssize_t send (int sockfd, const void *buf, size_t len, int flags);
>
> ssize_t recv (int sockfd, void *buf, size_t len, int flags); 
>
> ssize_t sendto (int sockfd, const void *buf, size_t len, int flags, const struct sockaddr *dest_addr, socklen_t addrlen);
>
> ssize_t recvfrom (int sockfd, void *buf, size_t len, int flags, struct sockaddr *src_addr, socklen_t *addrlen); 
>
> ssize_t sendmsg (int sockfd, const struct msghdr *msg, int flags);
>
> ssize_t recvmsg (int sockfd, strcut msghdr *msg, int flags);

#### 3.6 close()函数

> \#include <unistd.h>
>
> int close (int fd);

close一个TCP socket的缺省行为时把该socket标记为以关闭，然后立即返回到调用进程。该描述字不能再由调用进程使用，也就是说不能再作为read或write的第一个参数。

注意：close操作只是使相应socket描述字的引用计数-1，只有当引用计数为0的时候，才会触发TCP客户端向服务器发送终止连接请求。

### 4. socket中TCP的三次握手建立连接详解

![image](https://images.cnblogs.com/cnblogs_com/skynet/201012/201012122157476286.png)

### 5. socket中TCP的四次握手释放连接详解

![image](https://images.cnblogs.com/cnblogs_com/skynet/201012/201012122157494693.png)

### 6. 一个例子



