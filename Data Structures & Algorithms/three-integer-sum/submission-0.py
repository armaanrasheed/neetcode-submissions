class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #sort function first ->  O(nlogn) operation

        nums = sorted(nums)
        n = len(nums)
        output = []

        for i in range(0,n-2):

            if (i > 0) and nums[i] == nums[i-1]:
                continue

            j = i+1             # initial value
            k = n-1             # initial value

            while j < k:
                iValue = nums[i]
                jValue = nums[j]
                kValue = nums[k]
                sumValue = iValue + jValue + kValue

                if sumValue < 0: #sumValue is too small
                    j+=1
                    continue
                elif sumValue > 0:
                    k-=1
                    continue
                elif (sumValue == 0):
                    output.append([iValue,jValue,kValue])
                    k-=1
                    j+=1

                    while j<k and nums[j] == nums[j-1]:
                        j+=1

                    while j<k and nums[k] == nums[k+1]:
                        k-=1
                


        return output
                    
                

                    
