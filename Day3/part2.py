class Solution:
    def maxJoltage(self, filename):
        batteryBanks = self.parseFile(filename)
        total = 0

        for bank in batteryBanks:
            if bank[-1] == '\n':
                bank = bank[:len(bank)-1]
            current = list(bank[len(bank)-12:])

            for i in range(len(bank)-13, -1, -1):
                current = self.propogate(current, bank[i])

            ans = int("".join(map(str, current)))
            print(ans)
            total += ans

        return total

    def propogate(self, cur, j):
        tbd = -1
        
        for i in range(len(cur)):
            if tbd == -1:
                if int(j) >= int(cur[i]):
                    tbd = cur[i]
                    cur[i] = j
                else:
                    return cur
            else:
                if int(tbd) > int(cur[i]):
                    tbd, cur[i] = cur[i], tbd

        return cur

    def parseFile(self, filename):
        file = open(filename, "r")
        data = file.readlines()
        return data

sol = Solution()
#Test 1
testFile = "Day3/rawData1.txt"

answer = sol.maxJoltage(testFile)
expected = 3121910778619
if answer != expected:
    print("Failed, got " + str(answer) + " and expected " + str(expected))
    exit()
else:
    print("Passed!")


print(sol.maxJoltage("Day3/rawData2.txt"))

# 175662878362039 too large