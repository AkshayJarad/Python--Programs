import shutil

def Copy():
    shutil.copyfile("Akshay.txt","Akshay1.txt")
    
    print("File gets Successfully copied...")

def main():

    Copy()

if __name__ == "__main__":
    main()