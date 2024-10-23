class Solution:

    def isPalindrome(self, s):
        return s == s[::-1]

    def palindromePartition(self, s):
        finalList = []

        def backtrack(start, tempList):
            if start == len(s):
                finalList.append(tempList[:])
                return

            for end in range(start, len(s)):
                substring = s[start:end+1]
                if self.isPalindrome(substring):
                    tempList.append(substring)
                    backtrack(end + 1, tempList)
                    tempList.pop()

        backtrack(0, [])
        return finalList


# Test the function
res = Solution()
a = res.palindromePartition("aab")
print(a)
