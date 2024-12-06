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
        return self.trainData[nearestNeighbor][0]  

class Validator:
    def __init__(self, classfier):
        self.classfier = classfier

    
        

def loadData(filePath):
    data = []
    with open(filePath, 'r') as file:
        for line in file:
            values = list(map(float, line.split()))
            data.append(values)
    return data


if __name__ == "__main__":
    filePath = "small-test-dataset.txt"  
    try:
        data = loadData(filePath)
    except Exception as e:
        print("Error loading dataset: " + str(e))
        exit()

    
    featSubset = list(map(int, input("Enter the feature subset: ").split()))  

