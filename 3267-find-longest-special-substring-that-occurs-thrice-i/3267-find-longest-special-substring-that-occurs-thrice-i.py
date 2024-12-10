class Solution:
    def maximumLength(self, s: str) -> int:
        n = len(s)
        max_length = -1 
        for length in range(1, n + 1):
            for i in range(n - length + 1):
                substring = s[i:i + length]
                if len(set(substring)) == 1:
                    count = sum(s[j:j + length] == substring for j in range(n - length + 1))
                    if count >= 3:
                        max_length = max(max_length, length)

        return max_length