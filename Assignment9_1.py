import os

def main():
    print("Enter the name of the file to check its existance :")
    Fname = input()

    if os.path.exists(Fname):
        print("Unable to create the file as file is already existing...")

    else:
        open(Fname, "x")
        print("File gets successfully created...")


if __name__ == "__main__":
    main()
    