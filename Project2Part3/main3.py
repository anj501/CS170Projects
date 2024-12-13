from math import sqrt

class Feature:
    def __init__(self, numFeatures, validator, data):
        self.numFeatures = numFeatures
        self.validator = validator
        self.data = data

    def forwardSelect(self):
        currFeature = []
        overallAccuracy = 0
        bestFeature = []
        initialAccuracy = self.validator.validate(self.data, currFeature)
        print(f"Using no features and leave-one-out evaluation, I get an accuracy of {initialAccuracy:.2%}")
        print("Beginning search.")

        for i in range(1, self.numFeatures + 1):
            bestAccuracy = 0
            addFeature = 0
            for feature in range(1, self.numFeatures + 1):
                if feature not in currFeature:
                    tempFeature = list(currFeature) + [feature]
                    accuracy = self.validator.validate(self.data, tempFeature)
                    print(f"Using feature(s) {set(tempFeature)} accuracy is {accuracy:.2%}")
                    if accuracy > bestAccuracy:
                        bestAccuracy = accuracy
                        addFeature = feature

            if addFeature:
                currFeature.append(addFeature)
                print(f"Feature set {set(currFeature)} was best, accuracy is {bestAccuracy:.2%}")
                if bestAccuracy > overallAccuracy:
                    overallAccuracy = bestAccuracy
                    bestFeature = list(currFeature)

        print(f"Finished search!! The best feature subset is {set(bestFeature)}, which has an accuracy of {overallAccuracy:.2%}")

    def backwardElimination(self):
        currFeature = list(range(1, self.numFeatures + 1))
        overallAccuracy = 0
        bestFeature = list(currFeature)
        initialAccuracy = self.validator.validate(self.data, currFeature)
        print(f"Using all features and leave-one-out evaluation, I get an accuracy of {initialAccuracy:.2%}")
        print("Beginning search.")

        while len(currFeature) > 0:
            removeFeature = 0
            bestAccuracy = 0

            for feature in currFeature:
                tempFeature = currFeature.copy()
                tempFeature.remove(feature)
                accuracy = self.validator.validate(self.data, tempFeature)
                print(f"Using feature(s) {set(tempFeature)} accuracy is {accuracy:.2%}")
                if accuracy > bestAccuracy:
                    bestAccuracy = accuracy
                    removeFeature = feature

            if removeFeature in currFeature:
                currFeature.remove(removeFeature)
                print(f"Feature set {set(currFeature)} was best, accuracy is {bestAccuracy:.2%}")
                if bestAccuracy > overallAccuracy:
                    overallAccuracy = bestAccuracy
                    bestFeature = list(currFeature)

        print(f"Finished search!! The best feature subset is {set(bestFeature)}, which has an accuracy of {overallAccuracy:.2%}")


class Validator:
    def __init__(self, classifier):
        self.classifier = classifier

    def validate(self, data, featIndices):
        correctPredictions = 0
        numInstances = len(data)

        for i in range(numInstances):
            testInstance = data[i]
            trainData = data[:i] + data[i+1:]

            self.classifier.training(trainData)
            predictedClass = self.classifier.test(testInstance, featIndices)
            actualClass = testInstance[0]  

            if predictedClass == actualClass:
                correctPredictions += 1

        accuracy = correctPredictions / numInstances
        return accuracy

class Classifier:
    def __init__(self):
        self.trainData = None

    def training(self, data):
        self.trainData = data

    def test(self, testInstance, featIndice):
        trainFeat = []
        for i in self.trainData:
            trainFeat.append([i[j] for j in featIndice])

        testFeat = []
        for i in featIndice:
            testFeat.append(testInstance[i])

        Edistance = []
        for i in trainFeat:
            distance = 0
            for j in range(len(i)):
                distance += (i[j] - testFeat[j]) ** 2
            Edistance.append(sqrt(distance))

        nearestNeighbor = Edistance.index(min(Edistance))
        return self.trainData[nearestNeighbor][0]

def loadData(filePath):
    data = []
    with open(filePath, 'r') as file:
        for line in file:
            values = list(map(float, line.split()))
            data.append(values)
    return data

if __name__ == "__main__":
    print("Welcome to Kyle and Justin's Feature Selection Algorithm.")
    filePath = input("Type in the name of the file to test: ")
    try:
        data = loadData(filePath)
    except Exception as e:
        print("Error loading dataset: " + str(e))
        exit()

    numFeatures = len(data[0]) - 1  
    print(f"This dataset has {numFeatures} features (not including the class attribute), with {len(data)} instances.")

    print("Type the number of the algorithm you want to run.")
    print("1. Forward Selection")
    print("2. Backward Elimination")

    choice = input()

    classifier = Classifier()
    validator = Validator(classifier)
    featureSelector = Feature(numFeatures, validator, data)

    if choice == "1":
        print("\nRunning Forward Selection:")
        featureSelector.forwardSelect()
    elif choice == "2":
        print("\nRunning Backward Elimination:")
        featureSelector.backwardElimination()

#Group: Kyle Taing ktain007 024, Justin An jan053 024
#Large Dataset Result:
#Forward= {1,27} = 95.50%
#Backward= {27} = 84.70%
#Small Dataset Result:
#Backward = {2,4,5,7,10} = 83.00%
#Forward = {3,5} = 92.00%
#Titanic Dataset Result
#Forward = {2} = 78.01%
#BackWard = {2} = 78.01%