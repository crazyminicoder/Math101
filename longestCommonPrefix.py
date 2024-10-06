class Solution:
    def lcp(self, str):
        s = ''
        for i in str:
            count = 0
            currentStr = ""
            for j in range(len(str)-1):
                temp = str[j]
                print('temp ', temp)
                currentStr += temp[j]
                print('currentStr ', currentStr)
                if temp[j] == temp[j+1]:
                    count += 1
            if count == len(str):
                s += currentstr
                print('s', s)
            else:
                return s


res = Solution()
ans = res.lcp(["flower", "flow", "flight"])
print(ans)
