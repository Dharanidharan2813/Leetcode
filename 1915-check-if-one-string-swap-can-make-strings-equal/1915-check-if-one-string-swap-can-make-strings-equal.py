class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        diffs = [(i, s1[i], s2[i]) for i in range(len(s1)) if s1[i] != s2[i]]
        if len(diffs) != 2:
            return False
        return (diffs[0][1], diffs[1][1]) == (diffs[1][2], diffs[0][2])