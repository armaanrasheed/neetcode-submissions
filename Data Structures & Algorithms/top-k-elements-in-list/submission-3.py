#input: nums = [1,2,3,4] len(nums) = 4, and in the case that for example
# the number 4 apears 4 times, for us to track the bucket index which is responsible
# for 4 items being tracked the index would be 0,1,2,3,4 but the len of this
# array is 5, so we would need to do len(nums) + 1

from collections import defaultdict
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frequentDict = defaultdict(int)
        frequentOutputArr = [[] for i in range(len(nums)+1)]

        for number in nums:
            frequentDict[number]+=1

        for number, freqCount in frequentDict.items():
            frequentOutputArr[freqCount].append(number)

        res = []
        for i in range(len(frequentOutputArr)-1,0,-1):
            for num in frequentOutputArr[i]:
                res.append(num)
            
                if len(res) == k:
                    return res

            

        