from math import sqrt

class Classfier:
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
        return self.trainData[ nearestNeighbor][0]  

class Validator:
    def __init__(self, classfier):
        self.classfier = classfier

    def validate(self, data, featIndice):
        predictions = 0
        nn = len(data)

        for i in range(nn):
            testInstance = data[i]
            trainData = data[:i] + data[i+1:]

            self.classfier.training(trainData)
            predictClass = self.classfier.test(testInstance, featIndice)
            actualClass = testInstance[0]

            print("Instance", i+1, ": Predicted =", predictClass, ", Actual =", actualClass)

            if predictClass == actualClass:
                predictions += 1

        accuracy = predictions / nn
        print("Predictions:", predictions, "/", nn)
        return accuracy


def loadData(filePath):
    data = []
    with open(filePath, 'r') as file:
        for line in file:
            values = list(map(float, line.split()))
            data.append(values)
    return data


if __name__ == "__main__":
    filePath = "large-test-dataset.txt"  
    try:
        data = loadData(filePath)
    except Exception as e:
        print("Error loading dataset: " + str(e))
        exit()

    
    featSubset = list(map(int, input("Enter the feature subset: ").split()))  

    nnClass = Classfier()
    validator = Validator(nnClass)

    accuracy = validator.validate(data, featSubset)
    print(f"Accuracy: {accuracy:.3f}")
