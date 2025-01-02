class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        prefix = [0]
        cur = 0
        vowelSet = set(['a', 'e', 'i', 'o', 'u'])
        for s in words:
            if s[0] in vowelSet and s[-1] in vowelSet:
                cur += 1
            prefix.append(cur)
        res = []
        for s, e in queries:
            res.append(prefix[e+1] - prefix[s])
        return res