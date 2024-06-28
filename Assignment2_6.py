
def Display(No):
    i = 0
    j = 0
    for i in range(No,0,-1):
        print("")
        for j in range(i):
            if(i == j, i <= j):
                print("*", end = "    ")
            else:
                print("   ",end = "") 

def main():
    print("Enter the Number : ")
    Value = int(input())

    Display(Value)

if __name__ == "__main__":
    main()

