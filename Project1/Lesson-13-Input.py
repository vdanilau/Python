name = input("Enter your name: ")
print("Hello, " + name)

num1 = input("Enter X: ")
num2 = input("Enter Y: ")
num1, num2 = int(num1), int(num2)
summa1 = num1 + num2
print(summa1)

## or:
summa2 = int(num1) + int(num2)
print(summa2)
message = ""
while True:
    message = input("Enter Password: ")
    if message == "secret":
        break
    print(message + "Password is not correct")

print("Password was: " + message)

mylist = []
msg = ""
while msg != "stop".upper():
    msg = input("Enter new item, and STOP to finish: ")
    mylist.append(msg)

print(msg)
print(mylist)