## second discussion

notes from ykx



无人超市不能解决折损率问题，现成产品较多，竞争力不足

主要场景为衣柜和书架

#### 衣柜

problems：

- 重叠问题：堆叠放入如何识别和区分
- 不同物件识别问题：相同颜色如何识别，只能获取基本信息，条纹信息不明确
- 初步解决方案：要求用户的存放方式必须是一件一件放入，但是对用户要求太高

设计：

- 镜子+显示屏作为输入输出端，采用拍照片贴照片的方式和用户交互
- 卷的衣服，叠的衣服，挂的衣服分区
- 衣服分类不是问题

#### 书架

problems：

- 一本本放书问题不大，在其他场景中也有类似的多物体同时处理和区分问题


- 算法的性能不是很了解，需要去做一定的测试
- 同类物体或类似物体区分，标记正确率

设计：

* 不单独外置摄像头
* 新想法：红外代替视频探测书本位置
* 用红外发射器和接收器组成阵列



### conclusion

#### 书架

优先考虑背面探测：遮挡，隐私，成本的问题

背面探测成本降低很多

复杂环境下的多人使用，只能使用“或”的方式来记录物品的位置信息

#### 衣柜

* 镜子要有摄像头，在镜子前展示衣服来打tag

  一件一件放入问题不大

  概率算法来估计多衣服放入场景下相同特征衣服的位置

* 衣柜的整体构架：

  衣服分成卷、叠、挂

  卷和挂问题不大，主要问题在于一叠衣服的处理

  优先把卷和瞎几把扔的衣服放抽屉里，瞎几把扔的只能给定大致位置

  叠的衣服放入类似键盘抽屉的平台上，最好能够抽出来，这样有一定的径深，帮助用户解决内部无法直接目视到所有衣服时确定衣服位置的问题

* 最好能够语音输入和语音控制

  I/O的速度要足够快，如果用户直接找衣服更快捷则整个设计没有意义

  给用户语音或者图像指示衣服位置

  叠的衣服给出在哪一叠的第几件（或者是可能是哪几件，视存储位置信息时的状况而定）

  抽屉内的衣物指出在哪一个抽屉内，给出大致位置

  挂的衣服可直视，不需要特殊处理