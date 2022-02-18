cars = ['bmw', 'vw', 'seat', 'shkoda', 'jeely']

for x in cars:
    print(x.upper())

mynumber_list = list(range(0, 10))
print(mynumber_list)
print("===========================================")

for x in mynumber_list:
    x = x * 2
    print(x)

mynumber_list.sort(reverse=True)
print(mynumber_list)

print("Max number is: " + str(max(mynumber_list)))
print("Max number is: " + str(min(mynumber_list)))
print("Sum of list is: " + str(sum(mynumber_list)))
print("===========================================")

cars = ['bmw', 'vw', 'seat', 'shkoda', 'jeely']
mycars = cars[1:4] # вырежет от vm до jeely, не включая shkoda
print(mycars)

mycars = cars[:4] # вырежет с начала (поэтому слева от : ничего нет)
print(mycars)

mycars = cars[-3:] # стартуем с -3 позиции - если считается индекс с конца, то он стартует с -1
print(mycars)

mycars = cars[-3:-1]
print(mycars)
print("===========================================")

cars = ['bmw', 'vw', 'seat', 'shkoda', 'jeely']
mycars = cars[:]  # копирование массива в другой массив и в памяти будет два массива
mycars = cars # а так по сути делается новый указатель для массива

mynumber_list01 = []
for i in range(0, 10):
    mynumber_list01.append(i)
print(mynumber_list01)

# list generator:
mynumber_list02 = [i for i in range(10)]
print(mynumber_list02)