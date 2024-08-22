import sys

class LeetCode:

# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, 
# representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
  def __init__(self) -> None:
    pass
    
  
  def merge(self, nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """

    for j in range(n):
      nums1[m+j] = nums2[j]
    
    nums1.sort()
    return nums1

num1 = [1,2,3,0,0, 0,0]
num2 = 3
num3 = [4, 7, 8, 9]
num4 = 4
sol = LeetCode()
val = sol.merge(num1, num2, num3, num4)
print("The solution is: ", val)


#if __name__ == "__main__":
#  main()