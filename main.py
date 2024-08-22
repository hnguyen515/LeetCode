import sys
import LeetCode

num1 = [1,2,3,0,0, 0,0]
num2 = 3
num3 = [4, 7, 8, 9]
num4 = 4
test = LeetCode.Merge()
val = test.merge_sort(num1, num2, num3, num4)
print("The solution is: ", val)
