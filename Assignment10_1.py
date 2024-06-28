import sys
import os
import glob

def Find_Files(Directory,Extension):
    if not Extension.startswith('.'):
        Extension ='.'+Extension

    search_pattern = os.path.join(Directory,f'*{Extension}')

    try:
        print("Name of the File in which data is written : ",sys.argv[3])

        open(sys.argv[3],"x")
        fobj = open(sys.argv[3],"w")

        Files = glob.glob(search_pattern)

        if Files:
            for file in Files:
                (fobj.write(file))

        else:
            print(f"No Files with Extension'{Extension}' Found in Directory'{Directory}'")
    
    except FileExistsError as Dobj:
        print("Exception Occured : ",Dobj)
    except UnboundLocalError as Uobj:
        print("Exception Occured : ",Uobj)
    except Exception as eobj:
        print("Exception Occured : ",eobj)

    

def main():

    print("Name of the Directory is : ",sys.argv[1])
    print("extension is : ",sys.argv[2])
   
    if os.path.isdir(sys.argv[1]):
        print("Directory Exists")
        Find_Files(sys.argv[1],sys.argv[2])
    else:
        print("Directory Does not  Exist")

    

if __name__ == "__main__":
    main()