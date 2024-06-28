
class Circle:
    PI = 3.14

    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def Accept(self):
        print("Enter the Radius : ")
        self.Radius = int(input())

    
    def CalculateArea(self):
        self.Area = Circle.PI * self.Radius * self.Radius


    def CalculateCircumference(self):
        self.Circumference = 2 * Circle.PI * self.Radius

    def Display(self):
        print("Radius of the Circle is : ",self.Radius)
        print("Area of the Circle is : ",self.Area)
        print("Circumference of the Circle is : ",self.Circumference)

def main():

    Obj1 = Circle()

    Obj1.Accept()
    Obj1.CalculateArea()
    Obj1.CalculateCircumference()
    Obj1.Display()

if __name__ == "__main__":
    main()
        
