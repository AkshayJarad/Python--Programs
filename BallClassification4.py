from sklearn import tree

def MarvellousClassifier(weight,surface):

    Features = [[35,1], [47,1], [90,0], [48,1], [90,0], [35,1], [92,0], [35,1], [35,1], [35,1]]

    Labels = [1,1,2,1,2,1,2,1,1,1]

    # Decide the Algorithm
    obj = tree.DecisionTreeClassifier()

    # Train the model
    obj = obj.fit(Features,Labels)

    # Test the Model
    ret = (obj.predict([[weight,surface]]))

    if ret == 1:
        print("Your object looks like tennis ball")
    else:
        print("Your object looks like Cricket ball")


def main():
    print("------------Ball type Classification Case Study-----------")

    print("Please enter the information about the object that you want to test")

    print("Enter the Weight of the ball : ")
    weight = int(input())

    print("Enter the surface of the ball i.e rough or smooth")
    data = input()


    if data.lower() == "rough":
        data = 1
    elif data.lower() == "smooth":
        data = 0
    else:
        print("Invalid type of surface")
        exit()

    MarvellousClassifier(weight,data)



if __name__ == "__main__":
    main()

# DataSet size: 15
# Training size: 10
# Testing size