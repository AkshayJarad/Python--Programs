import psutil

def DisplayProcess(process_name):

    for proc in psutil.process_iter(['pid','name','username']):
        try:
            if proc.info['name'] == process_name:
                print(proc.info)
            
        except(psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    print("The Process in not Running")


def main():
    print("Enter the Name of the Process : ")
    process_name = input()

    DisplayProcess(process_name)


if __name__ == "__main__":
    main()