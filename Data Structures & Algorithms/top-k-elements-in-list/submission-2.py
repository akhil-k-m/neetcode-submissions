class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash1 = {}
        ans = []
        for num in nums:
            hash1[num] = hash1.get(num,0) + 1
        
        sorted_items = sorted(
            hash1.items(), 
            key = lambda x: x[1],
            reverse = True)
        
        for k, v in sorted_items[:k]:
            ans.append(k)
        return ans


        