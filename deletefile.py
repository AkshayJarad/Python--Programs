import os

def main():
    print("Enter the name of File that you want to delete :")
    Fname = input()

    if os.path.exists(Fname):
       os.remove(Fname)
       
    else:
        print("Unable to open the file as file is not present in the current directory")
    

if __name__ == "__main__":
    main()