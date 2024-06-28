
def Display(No):
    for i in range(No):
        print("") 
        for i in range(No):
            print("*", end = "    ")
            

def main():
    print("Enter the Number : ")
    Value = int(input())

    Display(Value)

if __name__ == "__main__":
    main()