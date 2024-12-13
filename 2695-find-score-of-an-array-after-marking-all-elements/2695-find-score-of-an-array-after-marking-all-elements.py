class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        marked = [False] * n 
        score = 0
        heap = []
        for i, num in enumerate(nums):
            heapq.heappush(heap, (num, i))

        while heap:
            val, i = heapq.heappop(heap)

            if marked[i]:
                continue

            score += val

            marked[i] = True
            if i - 1 >= 0:
                marked[i - 1] = True
            if i + 1 < n:
                marked[i + 1] = True

        return score