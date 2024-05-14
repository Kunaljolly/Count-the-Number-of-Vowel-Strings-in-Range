class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        l = ["a","e","i","o","u"]
        count = 0
        for x in range(left,right+1):
             if (words[x][0] in l) and (words[x][-1] in l):
                count += 1
        return count
