from random import randint
from copy import deepcopy
from time import time

n = 20  #Size of array

data = [randint(0, 1000) for _ in range(n)]
ground_truth = sorted(data)
# print(data)


arr = deepcopy(data)

def bubbleSort(arr, n = n):
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if arr[j] < arr[i]:
                temp = arr[j]
                arr[j] = arr[i]
                arr[i] = temp

bubbleSort(arr)

print(f"Before Sorting : {data}")
print(f"After Sorting : {arr}")
print(arr == ground_truth)
