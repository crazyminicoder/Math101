class Solution:
    def countMorse(self, words):
        wordDict = {}
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        morphs = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..",
                  "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        count = 0
        uniqueMorphs = set()
        for i in alpha:
            wordDict[i] = count
            count += 1
        for word in words:
            temp = ''
            for i in word:
                temp += morphs[wordDict[i]]

            uniqueMorphs.add(temp)

        return len(uniqueMorphs)


s = Solution()
words = ["gin", "zen", "gig", "msg"]
res = s.countMorse(words)
print(res)
