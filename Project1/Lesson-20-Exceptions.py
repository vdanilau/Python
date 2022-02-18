import sys

filename = "./files/password1.txt"

while True:
    try:
        print("Inside Try")
        myfile = open(filename, mode='r', encoding='Latin-1')
    except Exception:
        print("Inside EXCEPT")
        print("Error Found!")
        print(sys.exc_info()[1]) # т.к.это массив
        filename = input("Enter correct file name: ")
        # sys.exit()  # Это выкинет из программы и до последнего print уже не дойдет
    else:
        print("Inside ELSE")
        print(myfile.read())
        sys.exit()
    finally:
        print("Inside FINALLY")


print("===========EOF=============")