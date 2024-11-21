import random
class Feature:
 def __init__(self, numFeatures):
        self.numFeatures = numFeatures

 def fowardSelect(self):
    currFeature = []
    overallAccuracy = 0
    bestFeature = []
    for i in range(1, self.numFeatures + 1):
        bestAccuracy = 0   
        addFeature = 0
        for i in range(1, self.numFeatures + 1):
            if i not in currFeature:
                tempFeature = list(currFeature) + [i]
                accuracy = round(random.uniform(20, 100))
                print("Using feature(s) " + str(set(tempFeature)) + " accuracy is " + str(accuracy) + "%")
                if accuracy > bestAccuracy:
                    bestAccuracy = accuracy
                    addFeature = i
                    
        if addFeature:
            currFeature.append(addFeature)
            print("Feature set " + str(set(currFeature)) + " was best, accuracy is " + str(bestAccuracy) + "%")
            if bestAccuracy > overallAccuracy:
                overallAccuracy = bestAccuracy
                bestFeature = list(currFeature)
            
    print("Finished search!! The best feature subset is " + str(set(bestFeature)) + ", which has an accuracy of " + str(overallAccuracy) + "%")

def main():
    print("Welcome to Justin's and Kyle's Feature Selection Algorithm.")
    numFeatures = int(input("Please enter the total number of features: "))
    featAlgor = Feature(numFeatures)
    
    print("Type the number of the algorthim you want to run.\n1. Forward Selection\n2. Backward Elimination")
    choice = int(input())

    if choice == 1:
     featAlgor.fowardSelect()

if __name__ == "__main__":
    main()
