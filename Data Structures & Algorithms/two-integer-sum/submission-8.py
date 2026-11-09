class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = len(nums) - 1
        k = sorted(enumerate(nums), key = lambda x : x[1])
        while i < j:           
            if k[i][1] + k[j][1] == target:
                l1 = [k[i][0], k[j][0]]
                l1.sort()
                return l1
            if k[i][1] + k[j][1] > target:
                j = j-1
            else:
                i = i+1
        return None

        