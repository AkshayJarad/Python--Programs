
class Demo:
    Value = 0  # class variable

    def __init__(self,A,B): # instace method # constructor
        self.No1 = A   # instance variable
        self.No2 = B   # instance variable

    
    def Fun(self):    #  instance method
        print("Value of No1 inside Fun is : ",self.No1)
        print("Value of No2 inside Fun is : ",self.No2)

    def Gun(self):    # instance method
        print("Value of No1 inside Gun is : ",self.No1)
        print("Value of No1 inside Gun is : ",self.No2)


def main():

    Obj1 = Demo(11,21)
    Obj2 = Demo(51,101)

    Obj1.Fun()
    Obj2.Fun()
    Obj1.Gun()
    Obj2.Gun()

if __name__ == "__main__":
    main()


