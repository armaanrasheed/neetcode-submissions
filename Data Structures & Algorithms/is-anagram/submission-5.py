class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # char freq

        if len(s) != len(t):
            return False

        sDict = {}
        tDict = {}

        for S, T in zip(s,t):
            sDict[S] = sDict.get(S, 0) + 1
            tDict[T] = tDict.get(T, 0) + 1
        
        if sDict == tDict:
            return True

        return False

        

        