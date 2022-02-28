from urllib import request
import sys

myUrl = "http://adv400.tripod.com/kartinka.jpg"
myFile = "./files/my_picture.jpg"

try:
    print("Start Downloading file from: " + myUrl)
    request.urlretrieve(myUrl, myFile)
except Exception:
    print("Got Error!!!")
    print(sys.exc_info())
    exit()

print("File Downloaded and saved: " + myFile)
