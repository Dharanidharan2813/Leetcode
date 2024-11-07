class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def fun(mid, s=0):
            count = 0
            for v in nums:
                if s == 0 and v <= mid:
                    count += 1
                    s = True 
                else:
                    s = False 
            return count >= k
        start =0 
        end = max(nums)
        result = end
        while start <= end:
            mid = start + (end - start)//2
            if fun(mid):
                result = mid
                end = mid - 1
            else:
                start = mid + 1
        return result