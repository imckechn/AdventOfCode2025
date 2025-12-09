class Solution:
    def badDataFinder(self, filename):
        fileData = self.parseFile(filename)
        fileData = fileData[0].split(",")
        count = 0

        for dataRange in fileData:
            start, stop = dataRange.split("-")

            for i in range(int(start), int(stop)+1):
                number = str(i)
                matchFound = False
                
                for k in range(len(number)//2):
                    if number[:k+1] == number[k+1:k+k+2]:
                        matchFound = True

                        for m in range(k+1, len(number)//(k+1)-1, k+1):
                            if number[:k+1] != number[(k+1)+m:(k+k+2)+m]:
                                matchFound = False
                                break

                        if matchFound:
                            print(i)
                            count += i

        return count

    def parseFile(self, filename):
        file = open(filename, "r")
        data = file.readlines()
        return data



sol = Solution()
#Test 1
testFile = "Day2/rawData1.txt"

answer = sol.badDataFinder(testFile)
expected = 4174379265
if answer != expected:
    print("Failed, got " + str(answer) + " and expected " + str(expected))
    exit()
else:
    print("Passed!")


print(sol.badDataFinder("Day2/rawData2.txt"))
# 6426 too hight

# 6300 Too low