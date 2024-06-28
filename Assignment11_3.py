from sys import *
import hashlib
import os

def DeleteFiles(dict1):
    results = list(filter(lambda x : len(x) > 1, dict1.values()))

    iCnt = 0
    if len(results) > 0:
        for result in results:
            for subresult in result:
                iCnt = iCnt + 1
                if iCnt >= 2:
                    os.remove(subresult)
            iCnt = 0
    else:
        print("No Duplicate Files found !")
    
def hashfile(path, blocksize = 1024):
    fd = open(path, 'rb')
    hasher = hashlib.md5()
    buf = fd.read(blocksize)

    while len(buf) > 0:
        hasher.update(buf)
        buf = fd.read(blocksize)
    fd.close()
    return hasher.hexdigest()

def FindDuplicate(path):
    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)

    dups = {}
    if exists:
        for dirName, subdirs, fileList in os.walk(path):
            print("Current folder is : "+dirName)
            for filen in fileList:
                path = os.path.join(dirName, filen)
                file_hash = hashfile(path)
                if file_hash in dups:
                    dups[file_hash].append(path)
                else:
                    dups[file_hash] = [path]
        return dups
    else:
        print("Invalid Path")

def PrintDuplicate(dict1):
    results = list(filter(lambda x : len(x) > 1, dict1.values()))

    if len(results) > 0:
        print("Duplicates Found :")
        print("Follwing Files are Identical.")

        iCount = 0
        for result in results:
            for subresult in result:
                print(subresult)
                iCount = iCount+ 1
    
        print("Number of Deleted Files are : ",iCount)

    else:
        print("No Duplicate files found !")

def main():
    print("-------------------Application to Delete Duplicate Files--------------------")
    print("Name of the Directory is : ",argv[1])

    if(len(argv) != 2):
        print("Error : Invalid Number of Arguements")
        exit()

    if(argv[1] == '--h') or (argv[1] == '--H'):
        print("This Script is used to travel specific directory and delete Duplicate files")
        exit()

    if(argv[1] == '--u') or (argv[1] == '--U'):
        print("Application Name   Absolute_Path_Of_Directory   Extension")
        exit()

    try:
        arr ={}
        arr = FindDuplicate(argv[1])
        PrintDuplicate(arr)
        DeleteFiles(arr)
        print("   ")
        print("   ")
        print("   ")

    except ValueError:
        print("Error : Invalid Datatype of input")

    except Exception as obj1:
        print("Exception Occured due to ",obj1)


if __name__ == "__main__":
    main()