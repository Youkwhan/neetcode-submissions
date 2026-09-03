class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_len = len(nums1) + len(nums2)
        if len(nums1) < len(nums2):
            shorter,longer = nums1,nums2
        else:
            shorter,longer = nums2, nums1 
        l,r = 0, len(shorter)-1 
        #we could have a case where 
        # r < l  if it goes beyond
        while (l-1)<=r:
            #m1 is the index 
            m1 = (l+r)//2 
                  #count - #count
                  #we want index as well
            m2 = (total_len//2) - (m1+1) - 1

            SL = shorter[m1] if m1 >= 0 else float("-inf")
            SR = shorter[m1+1] if m1+1 < len(shorter) else float("inf")
            LL = longer[m2] if m2 >=0 else float("-inf")
            LR = longer[m2+1] if m2+1 < len(longer) else float("inf")

            if SL <= LR and LL <= SR:
                if total_len%2 == 0:
                    return (max(SL,LL) + min(SR,LR))/2
                else:
                    return min(SR,LR)
            if SL > LR:
                r = m1-1
            else:
                l = m1+1

        