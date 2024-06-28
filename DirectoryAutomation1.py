import sys
import os
import time

def DirectoryWatcher(DirName, FileName):
    Count = 0
    
    flag = os.path.isabs(DirName)

    if (flag == False):
        print("Path is not a Absolute Path")
        DirName = os.path.abspath(DirName)
        print("Converted Absolute path is : ",DirName)

    exist = os.path.isdir(DirName)

    if(exist == True):
        for foldername, subfoldername, filename in os.walk(DirName):
            for name in filename:
                if name.lower().endswith(Extension):
                    os.remove(name)
                    print("Delete File name is : ",name)
                
    else:
        print("There is no Such Directory")
    

def main():
    print("--------------------------------------------------------------")
    print("--------------------Directory Watcher-------------------------")
    print("--------------------------------------------------------------")

    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This script is used to perform Directory Traversal")
            exit()

        if(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Usage of the script : ")
            print("Name_Of_File Name_Of_Directory Name_Of_")
            exit()

        if(len(sys.argv) == 3):
            try:
                starttime = time.time()
                DirectoryWatcher(sys.argv[1],sys.argv[2])
                endtime = time.time()

                print("Time requird to execute the script is : ",endtime-starttime)

            except Exception as obj2:
                print("Unable to perform the task due to ",obj2)

    else:
        print("Invalid Option")
        print("Use --h option to get the help and use --u option to get the useage of Application")
        exit()    
        
    print("---------------------------------------------------------------")
    print("--------------Thankyou for Using our Script--------------------")
    print("---------------------------------------------------------------")

if __name__ == "__main__":
    main()

        

    
