class Solution:
    MAX = 100
    MIN = 0

    def safeBreaker(self, filename):
        fileData = self.parseFile(filename)
        currentNumber = 50
        zeroCount = 0

        for row in fileData:
            count = int(row[1:])

            if currentNumber == 0 and row[0] == "L":
                currentNumber -= count
                
                currentNumber += self.MAX

            else:
                if row[0] == "L":
                    currentNumber -= count
                else:
                    currentNumber += count

            if (currentNumber >= self.MAX or currentNumber < self.MIN):
                while (currentNumber >= self.MAX or currentNumber < self.MIN):
                    zeroCount += 1

                    if currentNumber >= self.MAX:
                        currentNumber -= self.MAX
                    else:
                        currentNumber += self.MAX
            elif currentNumber == 0:
                zeroCount += 1

        return zeroCount

    def parseFile(self, filename):
        file = open(filename, "r")
        data = file.readlines() #No need to worry about mem isssues since the file is <4500 lines long
        return data



sol = Solution()
#Test 1
# testFile = "Day1/textInputData.txt"

# answer = sol.safeBreaker(testFile)
# if answer != 6:
#     print("Failed, got " + str(answer) + " and expected 6")
#     exit()
# else:
#     print("Passed!")


print(sol.safeBreaker("Day1/input.txt"))
# 6426 too hight

# 6300 Too low