class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        twoSumDict = {}
        
        for index, key in enumerate(nums):
            twoSumDict[key] = index
                                      
        for i in range(len(nums)):
            makeTarget = target - nums[i]
            if (makeTarget in twoSumDict) and (i != twoSumDict[makeTarget]):
                return [i, twoSumDict[makeTarget]]