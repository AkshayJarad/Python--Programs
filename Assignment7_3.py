
class Arithmetic:

    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        print("Enter the First Number : ")
        self.Value1 = int(input())
        
        print("Enter the Second Number : ")
        self.Value2 = int(input())

    def Addition(self):
        Ans = self.Value1 + self.Value2
        return Ans
    
    def Subtraction(self):
        Ans = self.Value1 - self.Value2
        return Ans
    
    def Multiplication(self):
        Ans = self.Value1 * self.Value2
        return Ans
    
    def Division(self):
        Ans = self.Value1 // self.Value2
        return Ans
    
def main():
    Obj1 = Arithmetic()

    Obj1.Accept()

    Ret1 = Obj1.Addition()
    print("Addition is : ",Ret1)

    Ret2 = Obj1.Subtraction()
    print("Subtraction is : ",Ret2)

    Ret3 = Obj1.Multiplication()
    print("Multiplication is : ",Ret3)

    Ret4 = Obj1.Division()
    print("Division is : ",Ret4)


if __name__ == "__main__":
    main()