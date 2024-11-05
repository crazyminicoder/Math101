class Solution:
    def toGoatLatin(self, sen):
        count = 1
        vowels = ['a', 'e', 'i', 'o', 'u']
        newWordList = []
        s = sen.split()
        for i in s:
            # print('i in s', i)
            if i[0].lower() in vowels:
                # print('in vowel', i)
                temp = i
                temp += 'ma'
                # print('temp after +ma', temp)
                for j in range(count):
                    temp += 'a'
                count += 1
                newWordList.append(temp)
            elif i[0].lower() not in vowels:
                temp = i[1:]
                temp += i[0]
                temp += 'ma'
                for j in range(count):
                    temp += 'a'

                count += 1
                newWordList.append(temp)

        return ' '.join(newWordList)


a = Solution()
sentence = "I speak Goat Latin"
res = a.toGoatLatin(sentence)
print(res)
