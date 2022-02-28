from urllib import request

myUrl = "http://www.astahov.net"

reply = request.urlopen(myUrl)

mytext1 = reply.readlines()
mytext2 = reply.read()

print(reply)
print("########################## Read mytext2:\n\n")
print(mytext2)
print("########################## Read mytext1:\n\n")
for line in mytext1:
    print(line)