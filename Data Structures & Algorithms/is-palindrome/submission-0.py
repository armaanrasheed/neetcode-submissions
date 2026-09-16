class Solution:
    def isPalindrome(self, s: str) -> bool:

        left, right = 0, len(s)-1

        while left < right:
            sLLower = s[left].lower()
            sRLower = s[right].lower()
            if not sLLower.isalnum():
                left+=1
                continue
            elif not sRLower.isalnum():
                right-=1
                continue
            elif sLLower != sRLower:
                return False
            else:
                right-=1
                left+=1
       
        return True

