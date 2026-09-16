class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        flatList = [x for row in matrix for x in row]

        n = len(flatList)
        l, mid, r = 0, 0, n-1

        while l <= r:
            mid = (l+r)//2
            if flatList[mid] > target:
                r = mid - 1
                continue

            if flatList[mid] < target:
                l = mid + 1
                continue

            if flatList[mid] == target:
                return True

        return False
