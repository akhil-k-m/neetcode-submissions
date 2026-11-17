class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        deduplist = sorted(list(nums))
        count = 0
        res = 0
        if len(deduplist) == 1:
            return 1
        if len(deduplist) == 0:
            return 0

        for i in range(len(deduplist)-1):
            if deduplist[i] + 1 == deduplist[i+1]:
                if count == 0:
                    count +=2
                else:
                    count +=1
            else: 
                res = max(count, res)
                count = 0
        res = max(count, res)
        
        if res == 0:
            res = 1

        return res