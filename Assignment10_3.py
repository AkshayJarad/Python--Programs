import sys
import os
import shutil
from pathlib import Path

def Files_Copy(SourceDir,DestinationDir):
    try:
        src_path = Path(SourceDir)
        dest_path = Path(DestinationDir)

        dest_path.mkdir()

        for file_path in src_path.iterdir():
            if file_path.is_file():
                dest_file_path = dest_path / file_path.name
                shutil.copy2(file_path,dest_file_path)
                print(f'Copied : {file_path} to {dest_file_path}')
        
        print("Copying Completed")

    except Exception as eobj:
        print("Exception Occured : ",eobj)
    

def main():
    print("Directory in which files are present : ",sys.argv[1])
    print("Directory in which files get copied : ",sys.argv[2])

    if os.path.isdir(sys.argv[1]):
        print("Directory exists")
        Files_Copy(sys.argv[1],sys.argv[2])
    else:
        print("Directory does not exists")


if __name__ == "__main__":
    main()