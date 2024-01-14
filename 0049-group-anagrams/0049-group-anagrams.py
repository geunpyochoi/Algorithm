class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 새로운 객체에 정렬한 단어가 맞는 것들을 모으기
        anagram = collections.defaultdict(list)
        
        for word in strs:
            anagram[''.join(sorted(word))].append(word)
        
        return anagram.values()