class Classfier:
    def __init__(self):
        self.trainData = None

    def training(self, data):
        self.trainData = data
    
class Validator:
    def __init__(self, classfier):
        self.classfier = classfier
        
def loadData(filePath):
    data = []
    with open(filePath, 'r') as file:
        for i in file:
            values = (map(float, i.split()))
            data.append(values)
    return data


if __name__ == "__main__":
    filePath = "small-test-dataset.txt"  
    try:
        data = loadData(filePath)
    except Exception as e:
        print("Error loading dataset: " + str(e))
        exit()

    
    
    
