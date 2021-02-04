class ReadFile:

    def readData(self, fileName):
        file1 = open(fileName, 'r')
        content = file1.readlines()
        file1.close()
        return content

class FilterData(ReadFile):

    def readData(self, fileName):
        fileContent = super().readData(fileName)
        cities = []
        for line in fileContent:
            if line.startswith('L'. lower()):
                cities.append(line.strip('\n'))
        return cities # indentation is part of a method not a loop

f1 = FilterData()
print(f1.readData('data.txt'))