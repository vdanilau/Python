from urllib import request, parse
import sys

myUrl = "https://www.google.com/search?"
value = {'q': 'ANDESA Soft'}

myHeader = {}
myHeader['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"

print("################## myHeader: " + str(myHeader) + "\n\n")

print("################## myHeader: " + myHeader['User-Agent'] + "\n\n")

print("################## myHeader keys: " + str(myHeader.keys()) + "\n\n")

print("################## myHeader values: " + str(myHeader.values()) + "\n\n")
# for header in myHeader:
#     print("################## myHeader: " + header + "\n\n")

try:
    mydata = parse.urlencode(value)
    print("################## mydata:" + mydata + "\n\n")

    myUrl = myUrl + mydata
    print("############# use URL:" + myUrl + "\n\n")

    myReq = request.Request(myUrl, headers=myHeader)
    myReply = request.urlopen(myReq)
    myReply = myReply.readlines()
    print("################## myreply: \n\n")
    for line in myReply:
        print(line)
except Exception:
    print("Error occuried during web request!!")
    print(sys.exc_info()[1])