class Solution:
    def revVowels(self, s):
        vowels = ['a', 'e', 'i', 'o', 'u']
        vowelsInS = []
        s_list = list(s)
        for i in range(len(s)):
            temp = s[i]
            if temp.lower() in vowels:
                vowelsInS.append(s[i])

        vowelsInS = vowelsInS[::-1]
        j = 0
        for i in range(len(s)):
            temp = s[i]
            if temp.lower() in vowels:
                s_list[i] = vowelsInS[j]
                j += 1

        return ''.join(s_list)


a = Solution()
res = a.revVowels("leetcode")
print(res)
