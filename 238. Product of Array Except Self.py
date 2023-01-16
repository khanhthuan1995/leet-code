from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        hm = {}
        km= {}
        for i in range(len(nums)):
            if i == 0:
                hm[0] = 1
                km[0] = 1
            else:
                hm[i] = hm[i-1]*nums[i-1]
                km[i] = km[i-1]*nums[len(nums)-i]
        for i in range(len(nums)):
            ans.append(hm[i]*km[len(nums)-i-1])
        return ans
    
        