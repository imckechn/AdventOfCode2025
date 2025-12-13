from cmath import inf
import math

class Solution:
    def largestBox(self, filename):
        data = self.parseFile(filename)
        largestBoxArea = 0

        for i in range(len(data)):
            if data[i][-1] == '\n':
                data[i] = data[i][:len(data[i])-1]
            data[i] = data[i].split(",")

        connections = set()
        for i in range(len(data)):
            firstX, firstY = data[i]

            if i == len(data)-1:
                secondX, secondY = data[0]
            else:
                secondX, secondY = data[i+1]

            if firstX == secondX:
                if firstY > secondY:
                    for j in range(firstY+1, secondY):
                        connections.add([firstX, j])

                else:
                    for j in range(secondY+1, firstY):
                        connections.add([firstX, j])

            else:
                if firstX > secondX:
                    for j in range(firstX+1, secondX):
                        connections.add([j, firstY])

                else:
                    for j in range(secondX+1, firstX):
                        connections.add([j, firstY])

        

        for i in range(len(data)):
            for j in range(i+1, len(data)):
                firstX, firstY = data[i]
                secondX, secondY = data[j]
                area = (1+abs(int(secondX)-int(firstX))) * (1+abs(int(secondY)-int(firstY)))
                
                if firstX == secondX:
                    if firstY > secondY:
                        for j in range(firstY+1, secondY):
                            if [firstX, j] in connections
                            connections.append()

                    else:
                        for j in range(secondY+1, firstY):
                            connections.append([firstX, j])

                else:
                    if firstX > secondX:
                        for j in range(firstX+1, secondX):
                            connections.append([j, firstY])

                    else:
                        for j in range(secondX+1, firstX):
                            connections.append([j, firstY])

        return largestBoxArea

    def parseFile(self, filename):
        file = open(filename, "r")
        data = file.readlines()
        return data


sol = Solution()
#Test 1
testFile = "Day9/rawData1.txt"

answer = sol.largestBox(testFile)
expected = 24
if answer != expected:
    print("Failed, got " + str(answer) + " and expected " + str(expected))
    exit()
else:
    print("Passed!")

print(sol.largestBox("Day9/rawData2.txt"))