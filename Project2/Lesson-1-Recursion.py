def hello(x):
    if x == 0:
        return
    else:
        print("Hello World")
        hello(x-1)

hello(3)


def sum(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return x + sum(x-1)

z = sum(10)
print(z)


def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)

print(factorial(5))


def fido(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fido(x-1) + fido(x-2)

print(fido(77))