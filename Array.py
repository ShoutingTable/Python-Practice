# import array as arr

# a = arr.array('i', [1, 2, 3])

# print("The new created array is: ")
# for i in range(0, 3):
#     print(a[i], end = " ")
# print()


from array import *

array1 = array('i', [10, 20, 30, 40, 50])

array1.append(4)

for x in array1:
    print(x)