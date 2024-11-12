class Solution:
    def lcp(self, strs):
        for i in range(len(strs[0])):
            char = strs[0][i]
            for string in strs[1:]:
                if i >= len(string) or string[i] != char:
                    
                    return strs[0][:i]
        return strs[0]

 

res = Solution()
ans = res.lcp(["flower", "flow", "flight"])
print(ans)
