# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal
# substring
# consisting of non-space characters only.
class Solution:
    def length(self, s):
        s = s.split()
        lastWord = s[-1]
        return len(lastWord)


res = Solution()
a = res.length("   fly me   to   the moon  ")
print(a)
