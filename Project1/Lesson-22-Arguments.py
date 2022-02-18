import sys
import os

print("Hello")

sys.argv # все аргументы из CMD пересылаются в этот массив. Команда из cmd: python Lesson-22-Arguments.py sdfsdfsdf  sdfsdfsf

x = len(sys.argv)

if x > 1:
    if sys.argv[1] == "/?":
        print("Help Requested")
        print("Use these arguments in this program: pyhon myfile1 myfile2")
    print("Arguments entered: " + str(sys.argv[1:])) # т.е. выводит от первого аргумента и далее
else:
    print("Arguments is not provided")

os.system("dir > files/test.txt") # выполняет системные команды