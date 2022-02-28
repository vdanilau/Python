import os, time

DAYS = 5 # Max age of file to stay, older will be deleted
FOLDERS = [
            "C:\Test_For_Delete\Garbage",
            "C:\Test_For_Delete\Rubbish",
            "C:\Test_For_Delete\Trash"
]

TOTAL_DELETED_SIZE = 0 # Total size of deleted files
TOTAL_DELETED_FILE = 0 # Total deleted files
TOTAL_DELETED_DIRS = 0 # Total deleted empty folders

nowTime = time.time() # Get Current time in SECONDS
ageTime = nowTime - 60*60*24*DAYS # Minus DAYS in SECONDS

def delete_old_files(folder):
    """Delete files older than X DAYS"""
    global TOTAL_DELETED_FILE
    global TOTAL_DELETED_SIZE
    for path, dirs, files in os.walk(folder):
        for file in files:
            fileName = os.path.join(path, file) # get full path to file
            fileTime = os.path.getmtime(fileName) # time of the last modification of file
            if fileTime < ageTime:
                sizeFile = os.path.getsize(fileName)
                TOTAL_DELETED_SIZE += sizeFile # Count SUM of all free space
                TOTAL_DELETED_FILE += 1
                print("Deleting file: " + str(fileName))
                os.remove(fileName) # Delete file


def delete_empty_dir(folder):
    global TOTAL_DELETED_DIRS
    empty_folders_in_this_run = 0
    for path, dirs, files in os.walk(folder):
        if (not dirs) and (not files):
            TOTAL_DELETED_DIRS += 1
            empty_folders_in_this_run += 1
            print("Deleting empty DIR: " + str(path))
            os.rmdir(path)
    if empty_folders_in_this_run > 0:
        delete_empty_dir(folder)


# ===============MAIN===============
starttime = time.asctime()

for folder in FOLDERS:
    delete_old_files(folder)    # Delete old files
    delete_empty_dir(folder)    # Delete empty folders

finishtime = time.asctime()

print("-------------------------------------------------")
print("Start Time: " + str(starttime))
print("Total Clered Space: " + str(TOTAL_DELETED_SIZE/1024/1024) + " MB")
print("Total Deleted files: " + str(TOTAL_DELETED_FILE))
print("Total Deleted Empty folders: " + str(TOTAL_DELETED_DIRS))
print("FINISH TIME: " + str(finishtime))
print("------------------- EOF -------------------------")