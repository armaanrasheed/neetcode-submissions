class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set()
        longestSequence = 0
        # determining a valid start loop

        for number in nums:
            numsSet.add(number)

        for i in range(len(nums)):
            current = nums[i]
            length = 1
            if (current - 1) in numsSet:
                continue
            while (current + 1) in numsSet:
                current+=1
                length+=1
            longestSequence=max(length, longestSequence)

        return longestSequence