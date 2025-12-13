from cmath import inf
import math

class Solution:
    def TurnOnLights(self, filename):
        data = self.parseFile(filename)
        total = 0

        for i in range(len(data)):
            if data[i][-1] == '\n':
                data[i] = data[i][:len(data[i])-1]
            data[i] = data[i].split(" ")
        
        lights = []

        for row in data:
            lights.append(row.pop(0))
            row.pop()

        newData = []

        for row in data:
            newRow = []
            for elem in row:
                arr = []
                for char in elem:
                    if char.isdigit():
                        arr.append(int(char))
                newRow.append(arr)
            newData.append(newRow)
        data = newData

        for i in range(len(lights)):
            lightSet = []
            indexesToTurnOn = self.findLights(lights[i])
            subCount = 0

            while lightSet != indexesToTurnOn:
                subCount += 1
                toBeTurnedOn = []
                toBeTurnedOff = []

                copy = lightSet.copy()
                for k in indexesToTurnOn:
                    if k not in copy:
                        toBeTurnedOn.append(k)
                    else:
                        copy.remove(k)
                
                toBeTurnedOff = copy
                highScore = 0
                opperation = None

                for button in data[i]:
                    score = 0
                    for sublight in button:
                        if sublight in toBeTurnedOff or sublight in toBeTurnedOn:
                            score += 1
                    
                    if score > highScore:
                        highScore = score
                        opperation = button
                
                for light in opperation:
                    if light in lightSet:
                        lightSet.remove(light)
                    else:
                        lightSet.append(light)

            print("subcount = " + str(subCount))
            total += subCount
        return total
    
    def findLights(self, lights):
        indexes = []
        for i in range(1, len(lights)-1):
            if lights[i] == "#":
                indexes.append(i-1)
        return indexes

    def parseFile(self, filename):
        file = open(filename, "r")
        data = file.readlines()
        return data


sol = Solution()
#Test 1
testFile = "Day10/rawData1.txt"

answer = sol.TurnOnLights(testFile)
expected = 7
if answer != expected:
    print("Failed, got " + str(answer) + " and expected " + str(expected))
    exit()
else:
    print("Passed!")

print(sol.TurnOnLights("Day10/rawData2.txt"))