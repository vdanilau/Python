x = 25

if x == 25:
    print("Yes you're right")
else:
    print("No, you're wrong")


age = 14

if (age <=4):
    print("You are baby")
elif (age > 4) and (age < 12):
    print("You are kid")
elif (age >= 12) and (age < 19):
    print("You are teen")
else:
    print("You are old")

print("-----END-----\n")


all_cars = ['bmw', 'vw', 'seat', 'shkoda', 'jeely', 'lada', 'audi', 'ford', 'Chevrolet']
german_cars = ['bmw', 'vw', 'audi']

if 'lada' in all_cars:
    print("Yes LADA is in the list")
else:
    print("LADA is not in the list")
print("-----END-----\n")

for xxxx in all_cars:
    if xxxx in german_cars:
        print(xxxx.title() + " is a German car")
    else:
        print(xxxx + " is not a German car")