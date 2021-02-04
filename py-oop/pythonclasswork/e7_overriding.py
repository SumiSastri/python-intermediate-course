class FileHandler:
    def readFile(self, fileName):
        file1 = open(fileName,'r')
        content = file1.readlines()
        file1.close()
        return content


class FilterData(FileHandler):
    def readFile(self, fileName):
        content = super().readFile(fileName)
        list1 = []
        for line in content:
             if line.lower().startswith("l"): #filtro de cidade
                 list1.append(line)
        return list1

f1 = FilterData()
print(f1.readFile("data.txt")) # strip FIXME
