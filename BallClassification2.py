from sklearn import tree

# Rough   1
# Smooth  0

# Tennis  1
# Cricket 2

def main():
    print("Ball Classification Case Study")

    Features = [[35,1], [47,1], [90,0], [48,1], [90,0], [35,1], [92,0], [35,1], [35,1], [35,1]]

    Labels = [1,1,2,1,2,1,2,1,1,1]

    # Decide the Algorithm
    obj = tree.DecisionTreeClassifier()

    # Train the model
    obj = obj.fit(Features,Labels)

    # Test the Model
    print(obj.predict([[96,0]]))
    print(obj.predict([[35,1]]))


if __name__ == "__main__":
    main()

# DataSet size: 15
# Training size: 10
# Testing size