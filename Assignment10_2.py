import sys
import os
import glob
from pathlib import Path

def Change_File_Extension(Directory,OldExtension,NewExtension):
    if not OldExtension.startswith('.'):
        OldExtension = '.'+OldExtension
    if not NewExtension.startswith('.'):
        NewExtension = '.'+NewExtension

    try:
        path = Path(Directory)

        for file_path in path.glob(f'*{OldExtension}'):
            new_file_path = file_path.with_suffix(NewExtension)
            file_path.rename(new_file_path)
            print(f'Renamed : {file_path} to {new_file_path}')

            print("Renaming Complete")
            
    except Exception as eobj:
        print("Exception Occured : ",eobj)
    

def main():

    print("Name of the Directory is : ",sys.argv[1])
    print("first extension : ",sys.argv[2])
    print("second extension : ",sys.argv[3])

    if os.path.isdir(sys.argv[1]):
        print("Directory Exists")
        Change_File_Extension(sys.argv[1],sys.argv[2],sys.argv[3])
    else:
        print("Directory Does not  Exist")

    

if __name__ == "__main__":
    main()