class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countDict = defaultdict(int)
        outputArr = [[] for i in range(len(nums)+1)]

        for number in nums:
            countDict[number] +=1


        for number, count in countDict.items():
            outputArr[count].append(number)


        res = []

        for i in range(len(outputArr)-1,0,-1):
            for num in outputArr[i]:
                res.append(num)
                if len(res) == k:
                    return res