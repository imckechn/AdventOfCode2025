class Solution:
    def badDataFinder(self, filename):
        fileData = self.parseFile(filename)
        fileData = fileData[0].split(",")
        count = 0

        for dataRange in fileData:
            start, stop = dataRange.split("-")

            for i in range(int(start), int(stop)+1):
                number = str(i)
                length = len(number)

                if length % 2 == 1:
                    continue

                pointer = 0
                mirror = True

                while pointer < length/2:
                    if number[pointer] != number[pointer + length//2]:
                        mirror = False
                        break
                    else:
                        pointer += 1

                if mirror:
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
expected = 1227775554
if answer != expected:
    print("Failed, got " + str(answer) + " and expected " + str(expected))
    exit()
else:
    print("Passed!")


print(sol.badDataFinder("Day2/rawData2.txt"))
# 6426 too hight

# 6300 Too low