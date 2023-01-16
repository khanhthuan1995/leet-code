from typing import List
class Solution:
    def findKmax(self, d, k):
        z = []
        for i in range(k):
            ik = 0
            max_in = 0
            for index, value in d.items():
                if value > max_in:
                    max_in = value
                    ik = index
            z.append(ik)
            d.pop(ik)
        return z
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        for i in nums:
            if i in hm.keys():
                hm[i] += 1
            else: 
                hm[i] = 1
        return self.findKmax(hm, k)

   