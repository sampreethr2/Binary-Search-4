class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #Time: O(log(N))
        #Space: O(1)
        
        #Smaller array to be the first array
        if len(nums1)>len(nums2):
            return self.findMedianSortedArrays(nums2,nums1)
        
        left = 0
        right = len(nums1)
        
        #Binary Search
        while left<=right:
            mid = left +(right-left)//2
            
            #mid = nums1 partition
            if mid==0:
                l1 = float('-inf')
            else:
                l1 = nums1[mid-1]
            if len(nums1)==mid:
                r1 = float('inf')
            else:
                r1 = nums1[mid] 
            
            #part = nums2 partition
            part = ((len(nums1)+len(nums2)+1)//2)-mid
            if part==0:
                l2 = float('-inf')
            else:
                l2 = nums2[part-1]
            if len(nums2)==part:
                r2 = float('inf')
            else:
                r2 = nums2[part]
            
            #checking right set of partitions greater than left set in both arrays
            if (l1<=r2 and l2<=r1):
                if (len(nums1)+len(nums2))%2==0:
                    return (max(l1,l2)+min(r1,r2))/2
                else:
                    return max(l1,l2)
            
            #Moving the partitions around to obtain the above condition
            else:
                if l1>r2:
                    right=mid-1
                else:
                    left=mid+1
            
                