import csv
import re
with open('B:\git\pythonProjectNew\ФАЙЛ\Crimes.csv', 'r', newline='') as csvFile:
    reader = csv.DictReader(csvFile)
    s = []
    primaryType = {}

    #Выборка по году
    def getprimaryType(row):
        for value in row.values():
            if re.search(r'/2015', value):
                primaryType.update(row)
                return True
        return False
    # Выборка по типу преступления
    def getList(primaryType):
        for key, value in primaryType.items():
            if re.search(r'Primary Type', key):
                s.append(value)
                return s

    def getMaxList(s):
        m = 0
        x = ''
        for i in s:
            a = s.count(i)
            if s.count(i) > m:
                x = i
                m = s.count(i)
        print(x)


    def primaryTypes(reader):
        for row in reader:
            if getprimaryType(row):
                getList(primaryType)
        getMaxList(s)

    primaryTypes(reader)