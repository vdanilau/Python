import re

input_file_location = "./files/dumpfile.txt"
output_file_location = "./files/result_dumpfile.txt"

inputFile = open(input_file_location, mode='r', encoding='Latin-1')
outputFile = open(output_file_location, mode='w', encoding='Latin-1')
mytext = inputFile.read()

# lookfor = r"[\w.-]+@[A-Za-z-]+\.[\w]+" # в первом любая буква или . или -, потом любое колличество букв, потом @,
                                       # потом любая буква большая или маленькая или -, потом ., потом любая буква сколько угодно штук
# lookfor = r"[\w.-]+@[\w-]+\.[\w]+" # тоже самое\
lookfor = r"[\w.-]+@(?!yahoo\.org)[A-Za-z-]+\.[\w]+" # исключая домен yahoo.org
results = re.findall(lookfor, mytext)

for item in results:
    print(item)
    outputFile.write(item + "\n")

print("Total: " + str(len(results)))
