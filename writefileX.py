import os

def main():
    print("Enter the name of File that you want to open for writing purpose :")
    Fname = input()

    if os.path.exists(Fname):
       fobj = open(Fname, "a")
       print("File is Successfully opened in write mode")

       print("Enter data that you want to write in the File")
       Data = input()

       fobj.write(Data)

    else:
        print("Unable to open the file as file is not present in the current directory")
    

if __name__ == "__main__":
    main()