class Solution:
    def wordBreak(self, s, wordDict):
        word = ''
        newWords = set()
        count = 0
        for i in s:
            print(i)
            word += i
            if word in wordDict and word not in newWords:
                count += 1
                newWords.add(word)
                word = ''
                print('count', count)
        if count == len(wordDict):
            return True
        else:
            return False


sol = Solution()
s = 'leetcode'
wordDict = ['leet', 'code']
res = sol.wordBreak(s, wordDict)
print(res)
