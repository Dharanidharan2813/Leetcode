class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        stack1 = []
        for i in range(len(nums)):
            if nums[i] != val:
                stack1.append(nums[i])
        nums[:] = stack1
        return len(stack1)