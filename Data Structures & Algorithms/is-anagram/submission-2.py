class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        sDict = dict()
        tDict = dict()


        for char in s:
            sDict[char]=sDict.get(char,0) + 1
                
        
        for char in t:
            tDict[char] = tDict.get(char,0) + 1

        if sDict == tDict:
            return True
        
        return False
