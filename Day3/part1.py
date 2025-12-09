class Solution:
    def maxJoltage(self, filename):
        batteryBanks = self.parseFile(filename)
        total = 0

        for bank in batteryBanks:
            bank = bank[:len(bank)-1]
            largest = int(bank[-2])
            secondLargest = int(bank[-1])

            for i in range(len(bank)-3, -1, -1):
                val = int(bank[i])
                if val > largest or (largest*10 + secondLargest < val*10 + largest):
                    if largest > secondLargest:
                        secondLargest = largest
                    largest = val
            print(largest*10 + secondLargest)
            total += largest*10 + secondLargest

        return total

    def parseFile(self, filename):
        file = open(filename, "r")
        data = file.readlines()
        return data


sol = Solution()
#Test 1
testFile = "Day3/rawData1.txt"

answer = sol.maxJoltage(testFile)
expected = 357
if answer != expected:
    print("Failed, got " + str(answer) + " and expected " + str(expected))
    exit()
else:
    print("Passed!")


print(sol.maxJoltage("Day3/rawData2.txt"))