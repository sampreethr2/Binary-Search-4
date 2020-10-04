class Solution:
    def hIndex(self, citations: List[int]) -> int:
        #Time: O(log(N))
        #Space: O(1)
        low = 0
        high = len(citations)-1
        while low<=high:
            mid = low+(high-low)//2
            curr_index=len(citations)-mid
            if citations[mid]==curr_index:
                return curr_index
            elif citations[mid]<curr_index:
                low=mid+1
            else:
                high=mid-1
        return len(citations)-low