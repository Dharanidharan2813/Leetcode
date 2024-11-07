class Solution:
    def minCapability(self, a: List[int], k: int) -> int:
        def check(cap, q=0):
            count = 0
            for v in a:
                if q == 0 and v <= cap:
                    count += 1
                    q = True 
                else:
                    q = False 
            return count >= k
        minCap =0 
        maxCap = max(a)
        result = maxCap
        while minCap <= maxCap:
            cap = minCap + (maxCap - minCap)//2
            if check(cap):
                result = cap
                maxCap = cap - 1
            else:
                minCap = cap + 1
        return result