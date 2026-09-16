class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #use a set and keep adding unique members till we have the first membership fail
        # i wonder if you can do multiple sets spawned based on starting again or clear a set

        l, r = 0, 1

        maxCounter = 0
        duplicate = set()

        for r in range(len(s)):
            while s[r] in duplicate:
                duplicate.remove(s[l])
                l+=1
            
            duplicate.add(s[r])
            currentCount = (r-l+1)
            maxCounter = max(currentCount, maxCounter)
        
        return maxCounter