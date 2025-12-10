class Solution:
    def quickMath(self, filename):
        data = self.parseFile(filename)
        total = 0

        for i in range(len(data)):
            if data[i][-1] == '\n':
                data[i] = data[i][:len(data[i])-1]

        numbers = []
        for i in range(len(data[0])-1, -1, -1):
            curNumber = 0

            for j in range(len(data)):
                if data[j][i] == "*":
                    numbers.append(curNumber)
                    colTotal = 1
                    for number in numbers:
                        if number != 0:
                            colTotal *= number

                    curNumber = 0
                    numbers = []
                    total += colTotal
                
                elif data[j][i] == "+":
                    numbers.append(curNumber)
                    colTotal = 0
                    for number in numbers:
                        colTotal += number

                    curNumber = 0
                    numbers = []
                    total += colTotal
    
                elif data[j][i] != " ":
                    curNumber *= 10
                    curNumber += int(data[j][i])

            numbers.append(curNumber)

        return total

    def parseFile(self, filename):
        file = open(filename, "r")
        data = file.readlines()
        return data


sol = Solution()
#Test 1
testFile = "Day6/rawData1.txt"

answer = sol.quickMath(testFile)
expected = 3263827
if answer != expected:
    print("Failed, got " + str(answer) + " and expected " + str(expected))
    exit()
else:
    print("Passed!")


print(sol.quickMath("Day6/rawData2.txt"))