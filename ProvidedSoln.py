import sys

class Merge:
    def __init__(self) -> None:
        pass
    
  
    def merge_sort(self,nums1, m, nums2, n):
        j = 0;
        i = m;
        while (j<n):
            nums1[i] = nums2[j];
            j=j+1;
            i=i+1;
        nums1.sort();
        return nums1