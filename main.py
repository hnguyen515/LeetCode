import sys
import LeetCode

num1 = [1,3,5,0,0, 0,0]
num2 = 3
num3 = [2, 7, 8, 9]
num4 = 4
print("num1:", num1)
print("num2:", num2)
print("num3:", num3)
print("num4:", num4)
test = LeetCode.Merge()
val = test.merge_sort(num1, num2, num3, num4)
print("Merging into num1: ", val)
