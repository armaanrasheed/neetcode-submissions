class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
                
        leftPass = [1] * len(nums)
        rightPass = [1] * len(nums)
        res = [1] * len(nums)
        n = len(nums)

        for i in range(n):
            if i == 0:
                leftPass[i]=1
            else: 
                leftPass[i] = nums[i-1]*leftPass[i-1]

        for i in range(n-1,-1,-1):
            if i == n-1:
                rightPass[i] = 1
            else:
                rightPass[i] = nums[i+1]*rightPass[i+1]

        for i in range(n):
            res[i] = leftPass[i] * rightPass[i]

        return res
        