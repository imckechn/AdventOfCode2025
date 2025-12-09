class Solution:
    def quickMath(self, filename):
        data = self.parseFile(filename)
        total = 0

        for i in range(len(data)):
            if data[i][-1] == '\n':
                data[i] = data[i][:len(data[i])-1]

        isAddition = True
        for i in range(len(data)-1, -1, -1):
            columnTotal = 0
            while len(data[i]) > 0:
                if data[i][0] == "*":
                    isAddition = False
                    columnTotal = 1
                    break
                elif data[i][0] != " " and data[i][0] != "+":
                    j = 0
                    number = 0
                    while data[i][j] != " ":
                        number *= 10
                        number += int(data[i][j])
                    
                    if isAddition:
                        columnTotal += number
                    else:
                        columnTotal *= number
                        break
                    
                data[i] = data[i][1:]
            total += columnTotal
            print("Column total " + str(columnTotal))

        return total

    def parseFile(self, filename):
        file = open(filename, "r")
        data = file.readlines()
        return data


sol = Solution()
#Test 1
testFile = "Day6/rawData1.txt"

answer = sol.quickMath(testFile)
expected = 4277556
if answer != expected:
    print("Failed, got " + str(answer) + " and expected " + str(expected))
    exit()
else:
    print("Passed!")


print(sol.maxJoltage("Day6/rawData2.txt"))