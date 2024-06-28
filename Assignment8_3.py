
class Numbers:

    def __init__(self):
        self.Value = 0
        print("Enter the Number : ")
        self.Value = int(input())

    def ChkPrime(self):
        for i in range(2,self.Value):
            if(self.Value % i == 0):
                return False   
        return True
    
    def ChkPerfect(self):
        iCnt = 0
        for i in range(1,self.Value):
            if(self.Value % i == 0):
                iCnt = iCnt + i
                  
        if(iCnt == self.Value):
            return True
        else:
            return False
            
    def Factors(self):
        for i in range(1,self.Value+1):
            if(self.Value % i == 0):
                print(i, end = "  ")


    def SumFactors(self):
        iCnt = 0
        for i in range(1,self.Value+1):
            if(self.Value % i == 0):
                iCnt = iCnt + i 
        return iCnt
    

def main():
    Obj = Numbers()


    Ret1 = Obj.ChkPrime()
    if(Ret1 == True):
        print("Number is Prime")
    else:
        print("Number is not Prime")
 

    Ret2 = Obj.ChkPerfect()
    if(Ret2 ==True):
        print("Number is Perfect")
    else:
        print("Number is not a Perfect Number")


    Ret3 = Obj.SumFactors()
    print("Sum of Factors are : ",Ret3)


    Obj.Factors()


if __name__ == "__main__":
    main()

