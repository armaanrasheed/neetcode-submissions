class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        sDict = dict()
        tDict = dict()


        for char in s:
            sCount = sDict.get(char,0) + 1
            sDict[char]=sCount
                
        
        for char in t:
            tCount = tDict.get(char,0) + 1
            tDict[char]=tCount

        if sDict == tDict:
            return True
        
        return False
