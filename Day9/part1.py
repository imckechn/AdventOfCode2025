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

        for i in range(len(data)):
            for j in range(i+1, len(data)):
                firstX, firstY = data[i]
                secondX, secondY = data[j]
                area = (1+abs(int(secondX)-int(firstX))) * (1+abs(int(secondY)-int(firstY)))
                largestBoxArea = max(largestBoxArea, area)

        return largestBoxArea

    def parseFile(self, filename):
        file = open(filename, "r")
        data = file.readlines()
        return data


sol = Solution()
#Test 1
testFile = "Day9/rawData1.txt"

answer = sol.largestBox(testFile)
expected = 50
if answer != expected:
    print("Failed, got " + str(answer) + " and expected " + str(expected))
    exit()
else:
    print("Passed!")

print(sol.largestBox("Day9/rawData2.txt"))