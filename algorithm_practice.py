# %%
# list storing
import sys

n=10
data = []
for i in range(n):
    a= len(data)
    b = sys.getsizeof(data)

    print('The lenth is : {0:3d}, size in bytes: {1:4d}'.format(a, b))
    data.append(n)

print(len(data))
# Summary: Python can increase  memory size of array as nessecary
# List memory for an empty is 64 bytes, for string's character is 2 bytes.
# python list try to fill up the memory(64->96-> 128 ->192(per 4 element at the beginning))
# when it cant fill up more , it's going to create a new sized array, 
# The larger array, can hold more and more element
# %%
# Dynamic array:
