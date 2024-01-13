import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r'[^\w]',' ',paragraph).lower().split() if word not in banned]
        cnt = 0
        cnt2 = 0
        ans = ''
        for i in words:
            for j in words:
                if i == j:
                    cnt2 += 1
            if cnt2 > cnt :
                cnt = cnt2
                ans = i
            cnt2 = 0
        return ans