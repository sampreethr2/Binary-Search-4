class Solution:
    from collections import defaultdict
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #Time: O(n+m)
        #Space: O(min(n,m))
        if nums1>nums2:
            return self.intersect(nums2,nums1)
        if nums1==[] or nums2==[]:
            return []
        d = defaultdict(int)
        sol = []
        for i in nums1:
            d[i]+=1
        for i in nums2:
            if i in d and d[i]>0:
                d[i]-=1
                sol.append(i)
        return sol