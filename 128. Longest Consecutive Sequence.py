from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hm = {}
        s_arr = sorted(nums)
        i = 0
        while i < len(s_arr):
            if i+1 == len(s_arr):
                break
            nex_con = self.check_con(s_arr, i)
            if nex_con != i:
                hm[i] = nex_con-i+1
                i = nex_con
            else:
                hm[i] = 1
                i+=1
        arr = list(hm.values())
        return max(arr)
    def check_con(self,sorted_arr,index):
        n = index
        while sorted_arr[n+1] == sorted_arr[n]+1:
            n += 1
        return n
    

s = Solution()
nums = [100,4,200,1,3,2]
ans = s.longestConsecutive(nums)
print(ans)