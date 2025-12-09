class Solution:
    def maxJoltage(self, filename):
        paperRoles = self.parseFile(filename)
        total = 0
        
        for i in range(len(paperRoles)):
            paperRoles[i] = list(paperRoles[i])
            if paperRoles[i][-1] == '\n':
                paperRoles[i] = paperRoles[i][:len(paperRoles[-1])]

        for i in range(len(paperRoles)):
            for j in range(len(paperRoles[i])):
                if paperRoles[i][j] == ".":
                    continue

                count = 0
                #Check top left
                if i-1 >= 0 and j-1 >= 0:
                    if paperRoles[i-1][j-1] == '@':
                        count += 1

                #Check top
                if i-1 >= 0:
                    if paperRoles[i-1][j] == '@':
                        count += 1

                # Check top right
                if i-1 >= 0 and j+1 < len(paperRoles[i-1]):
                    if paperRoles[i-1][j+1] == '@':
                        count += 1

                #Check right
                if j+1 < len(paperRoles[i]):
                    if paperRoles[i][j+1] == '@':
                        count += 1

                #Check bottom right
                if i+1 < len(paperRoles) and j+1 < len(paperRoles[i+1]):
                    if paperRoles[i+1][j+1] == '@':
                        count += 1

                #Check bottom
                if i+1 < len(paperRoles):
                    if paperRoles[i+1][j] == '@':
                        count += 1

                #Check bottom left
                if i+1 < len(paperRoles) and j-1 >= 0:
                    if paperRoles[i+1][j-1] == '@':
                        count += 1
                
                #check left
                if j-1 >= 0:
                    if paperRoles[i][j-1] == '@':
                        count += 1

                if count < 4:
                    paperRoles[i][j] = "."
                    # print(str(i) + str(j))
                    total += 1

        return total

    def parseFile(self, filename):
        file = open(filename, "r")
        data = file.readlines()
        return data


sol = Solution()
#Test 1
testFile = "Day4/rawData1.txt"

answer = sol.maxJoltage(testFile)
expected = 13
if answer != expected:
    print("Failed, got " + str(answer) + " and expected " + str(expected))
    exit()
else:
    print("Passed!")


print(sol.maxJoltage("Day4/rawData2.txt"))