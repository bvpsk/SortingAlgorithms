from random import randint
from copy import deepcopy
from time import time

n = 20  #Size of array

data = [randint(0, 1000) for _ in range(n)]
ground_truth = sorted(data)
# print(data)


arr = deepcopy(data)

def insertionSort(arr, n = n):
    for i in range(n):
        key = arr[i]
        for j in range(0, i):
            if key < arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp

insertionSort(arr)

print(f"Before Sorting : {data}")
print(f"After Sorting : {arr}")
print(arr == ground_truth)
