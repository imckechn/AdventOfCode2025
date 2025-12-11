from cmath import inf
import math

class Solution:
    def JunctionBoxes(self, filename):
        data = self.parseFile(filename)

        for i in range(len(data)):
            if data[i][-1] == '\n':
                data[i] = data[i][:len(data[i])-1]
            data[i] = data[i].split(",")

        circuits = []
        shortestDistances = {}

        for i in range(len(data)):
            shortestDistance = inf
            shortest = -1
            for j in range(i + 1, len(data)):
                distance = math.sqrt((int(data[j][0])-int(data[i][0]))**2 + (int(data[j][1])-int(data[i][1]))**2 + (int(data[j][2])-int(data[i][2]))**2)
                shortestDistances[distance] = [i, j]        
        keySet = sorted(shortestDistances.keys())
        
        c = []
        circuits = []
        i = 0
        max = 6
        while i < max:
            ival, shortest = shortestDistances[keySet[i]]
            containsMatch = False
            jCircuit = False
            iCircuit = False
            for circuit in circuits:
                if ival in circuit:
                    iCircuit = circuit
                    containsMatch = True
                if shortest in circuit:
                    jCircuit = circuit
                    containsMatch = True

            if containsMatch:
                if iCircuit != False and jCircuit != False:
                    max += 1

                elif iCircuit != False:
                    iCircuit.append(shortest)
                else:
                    jCircuit.append(i)

            else:
                circuits.append([i, shortest])
            i += 1


        largest = -inf
        secondLargest = -inf
        thirdLargest = -inf

        for c in circuits:
            size = len(c)
            if size > largest:
                thirdLargest = secondLargest
                secondLargest = largest
                largest = size
            elif size > secondLargest:
                thirdLargest = secondLargest
                secondLargest = size
            elif size > thirdLargest:
                thirdLargest = size
        
        return largest * secondLargest * thirdLargest

    def parseFile(self, filename):
        file = open(filename, "r")
        data = file.readlines()
        return data


sol = Solution()
#Test 1
testFile = "Day8/rawData1.txt"

answer = sol.JunctionBoxes(testFile)
expected = 40
if answer != expected:
    print("Failed, got " + str(answer) + " and expected " + str(expected))
    exit()
else:
    print("Passed!")


print(sol.JunctionBoxes("Day8/rawData2.txt"))
#8 too low