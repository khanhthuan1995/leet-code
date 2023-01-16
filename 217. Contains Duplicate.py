from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 1 or len(nums) == 0:
            return False
        else: 
            hm = {}
            for i in nums:
                if i in hm:
                    return True
                else: 
                    hm[i] = True
            return False
            