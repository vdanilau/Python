for x in range(0, 100 + 1):
    print("*****")
    print("-----------")
    print(x)

for x in range(0, 100, 2):  #С шагом в 2
    print(x)

for x in range(100, 10, -2):  #С шагом в 2
    print("Number x = " + str(x))
    if x == 50:
        break

print("----------EOF----------")

while True:
    print(x)
    x = x + 1
    if x == 100:
        break