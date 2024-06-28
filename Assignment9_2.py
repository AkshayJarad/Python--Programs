import os

def main():
    print("Enter the name of File that you want to open : ")
    Fname = input()

    if os.path.exists(Fname):
        fobj = open(Fname, "r")
        print("File is Successfully opened")
        
        Data = fobj.read()
        print(Data)

    else:
        print("Unable to open the file as file is not present in the current folder")




if __name__ == "__main__":
    main()