class Solution:
    def MajorLazer(self, filename):
        data = self.parseFile(filename)

        for i in range(len(data)):
            if data[i][-1] == '\n':
                data[i] = data[i][:len(data[i])-1]
            data[i] = list(data[i])

        s = 0
        for i in range(len(data[0])):
            if data[0][i] == "S":
                s = i
                break

        return self.fireLazer(data, 1, s)

    def fireLazer(self, data, col, row):
        if len(data) <= col:
            return 1
        
        elif data[col][row] == "^":
            total = 0
            total += self.fireLazer(data, col+1, row-1)
            total += self.fireLazer(data, col+1, row+1)
            return total
        
        elif data[col][row] == ".":
            ans =  self.fireLazer(data, col+1, row)
            data[col][row] = ans
            return ans
        else:
            return data[col][row]


    def parseFile(self, filename):
        file = open(filename, "r")
        data = file.readlines()
        return data


sol = Solution()
#Test 1
testFile = "Day7/rawData1.txt"

answer = sol.MajorLazer(testFile)
expected = 40
if answer != expected:
    print("Failed, got " + str(answer) + " and expected " + str(expected))
    exit()
else:
    print("Passed!")


print(sol.MajorLazer("Day7/rawData2.txt"))