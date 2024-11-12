class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        n=len(nums)
        if n == 1:
            return False
        for i in range(n-1):
            if nums[i]==nums[i+1]:
                return True
        return False