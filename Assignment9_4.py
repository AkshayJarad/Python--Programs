import filecmp
import os

def main():
    print("Enter the name of the First file : ")
    F1name = input()

    print("Enter the name of the Seconf File :")
    F2name = input()

    result = filecmp.cmp(F1name,F2name)
    print(result)


if __name__ == "__main__":
    main()