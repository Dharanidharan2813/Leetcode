class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        freq = Counter(s)
        max_heap = []
        for char, count in freq.items():
            heapq.heappush(max_heap, (-ord(char), count))  

        result = []

        while max_heap:
            ascii_neg, count = heapq.heappop(max_heap)
            char = chr(-ascii_neg)
            use_count = min(count, repeatLimit)
            result.append(char * use_count)
            remaining = count - use_count
            if remaining > 0:
                if not max_heap:
                    break 
                ascii_neg2, count2 = heapq.heappop(max_heap)
                char2 = chr(-ascii_neg2)
                result.append(char2)
                count2 -= 1
                if count2 > 0:
                    heapq.heappush(max_heap, (ascii_neg2, count2))
                heapq.heappush(max_heap, (ascii_neg, remaining))
        return ''.join(result)
