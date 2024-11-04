class Solution:
    def canConstruct(self, ransomNote, magazine):
        ransomDict = {}
        magazineDict = {}
        rdSet = set()
        mdSet = set()
        for i in ransomNote:
            rdSet.add(i)
            if i in ransomDict:
                ransomDict[i] += 1
            else:
                ransomDict[i] = 1

        for i in magazine:
            mdSet.add(i)
            if i in magazineDict:
                magazineDict[i] += 1
            else:
                magazineDict[i] = 1

        for i in rdSet:
            if ransomDict[i] != magazineDict[i] and ransomDict[i] > magazineDict[i]:
                return False

        return True


s = Solution()
a = s.canConstruct('a', 'abb')
print(a)
