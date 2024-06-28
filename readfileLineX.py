import os

def main():
    print("Enter the name of File that you want to open for reading purpose :")
    Fname = input()

    if os.path.exists(Fname):
       

             

        
        fobj.close()

    else:
        print("Unable to open the file as file is not present in the current directory")
    

if __name__ == "__main__":
    main()