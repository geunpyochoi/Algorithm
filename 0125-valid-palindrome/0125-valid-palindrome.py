import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub(r'[^a-zA-Z0-9]','',s)
        l,r = 0,len(s)-1
        while l < r :
            if s[l] != s[r]:
                print('false')
                return False
            l += 1
            r -= 1
        print("true")
        return True
        