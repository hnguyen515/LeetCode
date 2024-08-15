import sys

def merge(nums1, m, nums2, n):
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

def main():
   num1 = [1,2,3,0,0,0]
   num2 = 3
   num3 = [4, 7, 9]
   num4 = 3
   val = merge(num1, num2, num3, num4)
   print("The solution is: ", val)


if __name__ == "__main__":
  main()