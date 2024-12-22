class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        s=0
        e=0
        n=len(nums1)
        m=len(nums2)
        nums3=[]
        i=0
        j=0
        while(i < n and j < m):
            if(nums1[i]<nums2[j]):
                nums3.append(nums1[i])
                i+=1
            else:
                nums3.append(nums2[j])
                j+=1
        while(i<n):
            nums3.append(nums1[i])
            i+=1
        while(j<m):
            nums3.append(nums2[j])
            j+=1
        c=n+m
        if(c%2==1):
          return(float(nums3[c//2]))
        else:
          return(float(nums3[c//2] + nums3[c//2 - 1])/2)