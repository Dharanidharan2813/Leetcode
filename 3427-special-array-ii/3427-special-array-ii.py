class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        # Step 1: Create `same_parity` array
        same_parity = [0] * (n - 1)
        for i in range(n - 1):
            if nums[i] % 2 == nums[i + 1] % 2:
                same_parity[i] = 1
    
        # Step 2: Build prefix sum of `same_parity`
        prefix_sum = [0] * n
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + (same_parity[i - 1] if i - 1 < len(same_parity) else 0)
    
        # Step 3: Process each query using the prefix sum
        result = []
        for from_idx, to_idx in queries:
            # Check if there are any "same parity" pairs in the range
            if prefix_sum[to_idx] - prefix_sum[from_idx] > 0:
                result.append(False)
            else:
                result.append(True)
    
        return result
    