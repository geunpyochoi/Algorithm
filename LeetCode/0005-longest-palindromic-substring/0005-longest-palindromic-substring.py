class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        for i in range(0,len(s)):
            for j in range(i+1,len(s)+1):
                s2 = s[i:j]
                if s2[::-1] == s[i:j] and len(ans) < len(s2):
                    ans = s2
        return ans