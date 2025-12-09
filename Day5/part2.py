class Solution:
    def maxJoltage(self, filename):
        foodStuffs = self.parseFile(filename)

        for i in range(len(foodStuffs)):
            if foodStuffs[i][-1] == '\n':
                foodStuffs[i] = foodStuffs[i][:len(foodStuffs[i])-1]

        ranges, index = self.getRanges(foodStuffs)

        pairs = []
        for elem in ranges:
            elem = elem.split("-")
            elem[0], elem[1] = int(elem[0]), int(elem[1])
            pairs.append(elem)

        pairs.sort()

        i = 1
        while i < len(pairs):
            if pairs[i][0] <= pairs[i-1][1]:
                pairs[i-1][1] = max(pairs[i][1], pairs[i-1][1])
                pairs.pop(i)
            else:
                i += 1

        count = 0
        for start, end in pairs:
            count += end-start+1

        return count
    
    def getRanges(self, data):
        ranges = []
        
        for i, r  in enumerate(data):
            if r != "":
                ranges.append(r)
            else:
                return ranges, i

    def parseFile(self, filename):
        file = open(filename, "r")
        data = file.readlines()
        return data


sol = Solution()
#Test 1
testFile = "Day5/rawData1.txt"

answer = sol.maxJoltage(testFile)
expected = 14
if answer != expected:
    print("Failed, got " + str(answer) + " and expected " + str(expected))
    exit()
else:
    print("Passed!")

print(sol.maxJoltage("Day5/rawData2.txt"))
