#!/bin/python3

import shutil # For CopyFile
import os # For GetFileSize and check if file exists
import sys # For CLI arguments

# Lesson-4-PurgeLog.py mylog.txt 10 5 # как будем запускать. При этом 10 это мак размер в кб, 5 - сколько доп лог файлов хотим

if(len(sys.argv) < 4):
     print("Missing arguments: Use script.py 10 5")
     exit(1)

file_name = sys.argv[1]
limit_size = int(sys.argv[2])
logs_number = int(sys.argv[3])

if(os.path.isfile(file_name) ==True):    # Check file existing
    log_file_size = os.stat(file_name).st_size # Get Filesize in Bytes
    log_file_size = log_file_size / 1024 # Convert from Bytes to KiloBytes

    if(log_file_size >= limit_size):
        if(logs_number > 0):
            for currentFileNum in range(logs_number, 1, -1):
                src = file_name + "_" + str(currentFileNum-1)
                dst = file_name + "_" + str(currentFileNum)
                if(os.path.isfile(src) == True):
                    shutil.copyfile(src, dst) # Copy file
                    print("Copied: " + src + " to " + dst)
            shutil.copyfile(file_name, file_name + "_1")
            print("Copied: " + file_name + " to " + file_name + "_1")
        myfile = open(file_name, 'w') # если просто открыть файл в режиме w, то он сразу обнуляется
        myfile.close()
