import urllib
import httplib 
test_data = {'grant_type':'client_credentials','client_id':'cck8XUmWiGclfBcV8k7rv5Y2','client_secret':'zxbVOOGuiEDKHkDCxrGOFmISommL5itU'}
test_data_urlencode = urllib.urlencode(test_data)

requrl = "https://openapi.baidu.com/oauth/2.0/token"
headerdata = {"Host":"openapi.baidu.com"}

conn = httplib.HTTPConnection("openapi.baidu.com")

conn.request(method="POST",url=requrl,body=test_data_urlencode,headers = headerdata) 

response = conn.getresponse()

res= response.read()

print res
