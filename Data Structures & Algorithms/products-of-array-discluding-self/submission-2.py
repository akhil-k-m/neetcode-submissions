class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pro = 1
        zero_count = 0
        for num in nums:
            if num:
                pro = pro*num
            else: 
                zero_count +=1
        
        list1 = []
        for num in nums:
            if zero_count > 1:
                list1.append(0)
            else:
                if zero_count == 1:
                    if num:
                        list1.append(0)
                    else:
                        list1.append(pro)
                else:
                    list1.append(pro//num)
        return list1




        