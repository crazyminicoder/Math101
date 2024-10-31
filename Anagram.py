from collections import Counter


class Solution:
    def anagram(self, s, t):
        s1 = list(s)
        d1 = {}
        d2 = {}
        if len(s) != len(t):
            return False
        for letter in s:
            if letter in d1:
                d1[letter] += 1
            else:
                d1[letter] = 1

        for letter in t:
            if letter in d2:
                d2[letter] += 1
            else:
                d2[letter] = 1
        for i in t:
            if i in s1:
                countInT = d2[i]
                countInS = d1[i]
                if countInT != countInS:
                    return False
            else:
                return False

        return True
        # for i in t1:
        # if i not in s1:
        # return False

    def anagram2(self, s, t):
        if len(s) != len(t):
            return False
        if Counter(s) != Counter(t):
            return False
        return True


s = Solution()
res = s.anagram('rat', 'car')
res1 = s.anagram2('rat', 'car')
print(res)
print(res1)
