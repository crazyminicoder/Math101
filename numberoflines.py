class Solution:
    def numberOfLines(self, width, s):
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        wordDict = {}
        count = 0
        for i in alpha:
            wordDict[i] = count
            count += 1
        line = 1
        temp = 0
        for i in s:
            temp += width[wordDict[i]]
            if temp > 100:
                line += 1
                temp = 0
                temp += width[wordDict[i]]

        return [line, temp]


s = Solution()
widths = [4, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
          10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
a = "bbbcccdddaaa"
res = s.numberOfLines(widths, a)
print(res)
