
class BankAccount:
    ROI = 10.5

    def __init__(self):
        self.Name = ""
        print("Enter Account Holders name : ")
        self.Name = input()

        self.Amount = 0
        print("Enter the Amount : ")
        self.Amount = int(input())

    def Display(self):
        print("Name is : ",self.Name)
        print("Amount is : ",self.Amount)

    def Deposit(self):
        No = 0
        print("Enter the amount for Deposit : ")
        No = int(input())

        self.Amount = self.Amount + No

    def Withdraw(self):
        No = 0
        print("Enter the Amount for Withdraw : ")
        No = int(input())
        self.Amount = self.Amount - No


    def CalculateInterest(self):
        Interest = (self.Amount * self.ROI) / 100
        print("Interest calculated is : ",Interest)
        
    

def main():

    Obj = BankAccount()
    Obj.Display()
    Obj.Deposit()
    Obj.Withdraw()
    Obj.CalculateInterest()

if __name__ == "__main__":
    main()