import sys
import LeetCode
import ProvidedSoln

num1 = [1,3,5,0,0, 0,0]
num2 = 3
num3 = [2, 7, 8, 9]
num4 = 4
print("\n*****************************************************")
print("This is for merging array elements.")
print("-------------------------------------------------------")
print("num1:", num1)
print("num2:", num2)
print("num3:", num3)
print("num4:", num4)
test1 = LeetCode.Merge()
test2 = ProvidedSoln.Merge()

val1 = test1.merge_sort(num1, num2, num3, num4)
val2 = test2.merge_sort(num1, num2, num3, num4)

print("Merging into num1: ", val1)
print("Soln Merging into num1: ", val2)
print("Answer and Solution MATCHED:", val1==val2)
print("-------------------------------------------------------\n")


# Removing an element from the array.
print("\n*****************************************************")
print("-------------------------------------------------------")
print("This is for removing an array element.\n")
nums = [0, 1, 2, 3, 4, 2, 5, 6];
val = 2;
print("nums:", nums);
print("val:", val);
test3 = LeetCode.Remove
rmv = test3.rmv_elm(nums, val)
print("rmv_elm(,", val, "):", rmv)
print("-------------------------------------------------------\n")