n = int(input())
s = 0

for i in range(0, 6):
    s += (n % 10, -(n % 10))[i < 3]
    print(f"s= {s}")

    print("this is i = " + str(i))
    n //= 10
    print(f"n//10 = {n%10}")    
    print(f"This is n = {n}")
    print("################")
print(('Счастливый', 'Несчастливый')[bool(s)])
print(s)

# print(163%10)
# print(-(163%10))
# print(12//=10)