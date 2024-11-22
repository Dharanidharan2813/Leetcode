class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        pattern_count = Counter()
        for row in matrix:
            base_pattern = tuple(row[i] ^ row[0] for i in range(len(row)))
            pattern_count[base_pattern] += 1
        return max(pattern_count.values())
