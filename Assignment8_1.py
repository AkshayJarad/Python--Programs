
class BookStore:
    NoOfBooks = 0

    def __init__(self,A,B):
        self.Name = A
        self.Author = B
        BookStore.NoOfBooks = BookStore.NoOfBooks + 1

    def Display(self):
        print(self.Name,"by",self.Author)
        print("Number of Books are : ",self.NoOfBooks)

def main():

    Obj1 = BookStore("Linux System Programming","Robert Love")
    Obj1.Display()

    Obj2 = BookStore("C Programming","Ajay Mittal")
    Obj2.Display()

if __name__ == "__main__":
    main()


