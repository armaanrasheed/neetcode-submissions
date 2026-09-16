
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frq = {}

        l = 0

        maxCount = 0

        output = 0


        for r in range(len(s)):

            frq[s[r]] = frq.get(s[r],0) + 1

            maxCount = max(maxCount, frq[s[r]])

            while r-l+1 - maxCount > k:
                frq[s[l]]-=1
                l+=1
        
            output = max(r-l+1, output)

        return output
