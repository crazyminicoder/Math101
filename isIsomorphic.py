class Solution:
    def isIsomorphic(self, s, t):
        sDict = {}
        unique = set()
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] in sDict:
                if sDict[s[i]] != t[i]:
                    return False
            else:
                if t[i] in unique:
                    return False

                sDict[s[i]] = t[i]
                unique.add(t[i])

        return True


s = Solution()

a = 'bada'
b = 'baba'

res = s.isIsomorphic(a, b)
print(res)
