class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        sDict = dict()
        tDict = dict()


        for charS, charT in zip(s,t):
            sDict[charS]=sDict.get(charS,0) + 1
            tDict[charT]=tDict.get(charT,0) + 1   
        
        if sDict == tDict:
            return True
        
        return False
