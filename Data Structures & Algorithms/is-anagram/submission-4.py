class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # char freq

        if len(s) != len(t):
            return False

        sDict = {}
        tDict = {}

        for S, T in zip(s,t):
            currentS = sDict.get(S, 0)
            sDict[S] = currentS + 1
            currentT = tDict.get(T, 0)
            tDict[T] = currentT + 1
        
        if sDict == tDict:
            return True

        return False

        

        