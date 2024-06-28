import psutil

def DisplayProcess():
    print("List of Running Processes are : ")

    print("__________________________________________________________________")

    for proc in psutil.process_iter(['pid','name','username']):
        print(proc.info)

    print("___________________________________________________________________")

def main():
    DisplayProcess()

if __name__ == "__main__":
    main()
