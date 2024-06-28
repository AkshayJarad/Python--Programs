from sys import *
import hashlib
import os

def hashfile(path, blocksize = 1024):
    afile = open(path, 'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()

def DisplayCheckSum(path):
    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)

    if exists:
        for dirName, subdirs, fileList in os.walk(path):
            print("Current folder is : "+dirName)
            for filen in fileList:
                path = os.path.join(dirName, filen)
                file_hash = hashfile(path)
                print(path)
                print(file_hash)
                print(' ')
    else:
        print("Invalid Path")

def main():
    print("-------------------Application to Display CheckSum--------------------")
    print("Name of the Directory is : ",argv[1])

    if(len(argv) != 2):
        print("Error : Invalid Number of Arguements")
        exit()

    if(argv[1] == '--h') or (argv[1] == '--H'):
        print("This Script is used to travel specific directory and display checksum of files")
        exit()

    if(argv[1] == '--u') or (argv[1] == '--U'):
        print("Application Name   Absolute_Path_Of_Directory   Extension")
        exit()

    try:
        arr = DisplayCheckSum(argv[1])
        print("   ")
        print("   ")
        print("   ")

    except Exception as obj1:
        print("Exception Occured due to ",obj1)


if __name__ == "__main__":
    main()