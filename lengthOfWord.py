class Solution:
    def length(self, s):
        s = s.split()
        lastWord = s[-1]
        return len(lastWord)


res = Solution()
a = res.length("   fly me   to   the moon  ")
print(a)
