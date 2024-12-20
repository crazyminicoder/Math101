class Solution:
    def combinationSum2(self, candidates, target):
        def backtrack(start, target, path):
            if target == 0:
                result.append(list(path))
                return

            if target < 0:
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                path.append(candicates[i])

                backtrack(i+1, target-candidates[i], path)
                path.pop()
        candidates.sort()

        result = []
        backtrack(0, target, [])
        return result


s = Solution()
candicates = [10, 1, 2, 7, 6, 1, 5]
target = 8
res = s.combinationSum2(candicates, target)
print(res)
