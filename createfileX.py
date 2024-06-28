import os

def main():
    print("Enter the name of File that you want to create :")
    Fname = input()

    if os.path.exists(Fname):
        print("Unable to create file as file is already existing")

    else:
        open(Fname, "x")
        print("File gets successfully created")
    

if __name__ == "__main__":
    main()


# Absolute path : /Sagar/Desktop/Python/Automation/Marvellous.txt
# Relative path : Automations/Marvellous.txt