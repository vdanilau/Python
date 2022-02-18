def print_hello():
    """"Greeting"""
    print("Hello World!")
    print("Congratulation!")


def print_hello_with_name(name):
    """"Greeting"""
    print("Congratulation " + name + "!")


def sum(x, y):
    print(x+y)


def sum_with_return(x, y):
    return x + y


def factorial(x):
    """Calculate factorial of number X"""
    answer = 1
    for i in range(1, x + 1):
        answer = answer * i
    return answer

print("--------------------------")

print_hello()
print("--------------------------")

print_hello_with_name("Boy")
print_hello_with_name("Girl")
print("--------------------------")

sum(5,4)
print("--------------------------")

x = sum_with_return(33, 22)
print(x)
print("--------------------------")

for i in range(1, 10):
    print(str(i) + "!\t =\t" + str(factorial(i)))