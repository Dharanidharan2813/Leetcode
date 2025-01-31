class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        value = -100001
        min_distance = 100001
        
        for num in nums:
            dist = abs(num)
            if dist < min_distance:
                min_distance = dist
                value = num
            elif dist == min_distance and num > value:
                value = num  
        return value