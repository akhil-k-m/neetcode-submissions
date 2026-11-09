class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ## Solution 1
        # if len(s) != len(t):
        #     return False 
        # s = sorted(s)
        # t = sorted(t)
        # for i in range(0, len(s), 1):
        #     if s[i]!= t[i]:
        #         return False
        # return True

        ## solution 2 
        return sorted(s) == sorted(t)
        