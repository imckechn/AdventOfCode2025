class Solution:
    def maxJoltage(self, filename):
        foodStuffs = self.parseFile(filename)
        total = 0

        for i in range(len(foodStuffs)):
            if foodStuffs[i][-1] == '\n':
                foodStuffs[i] = foodStuffs[i][:len(foodStuffs[i])-1]

        ranges, index = self.getRanges(foodStuffs)
        foodIds = foodStuffs[index+1:]

        pairs = []
        for elem in ranges:
            elem = elem.split("-")
            elem[0], elem[1] = int(elem[0]), int(elem[1])
            pairs.append(elem)


        for id in foodIds:
           id = int(id)
           for pair in pairs:
                if id == pair[0] or id == pair[1] or (id > pair[0] and id < pair[1]):
                   total += 1
                   break
               

        return total
    
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
expected = 3
if answer != expected:
    print("Failed, got " + str(answer) + " and expected " + str(expected))
    exit()
else:
    print("Passed!")


print(sol.maxJoltage("Day5/rawData2.txt"))