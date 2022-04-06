inputfile = "./files/user_names.txt"
outfile = "./files/password.txt"

password_to_look_to = "Davidson"

myfile1 = open(inputfile, mode='r', encoding='latin_1')
myfile2 = open(outfile, mode='w', encoding='latin_1')

for num, line in enumerate(myfile1, 1):  # нумерует с 1, при этом в line заходит все еще каждая строчка из файла, а вот в num уже идет номерное значение.
    if password_to_look_to in line:
        print("Line №:  " + str(num) + " : " + line.strip())
        myfile2.write("Found password: " + line)

myfile1.close()
myfile2.close() 
