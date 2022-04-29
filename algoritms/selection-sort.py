from random import randint

from random import randint
N = 10
arr = []
for i in range(N):
    arr.append(randint(1, 99))
print(f"Unsorted array: {arr}")

i = 0

while i < N - 1:
    m = i
    j = i + 1
    while j < N:
        if arr[j] < arr[m]:
            m = j
        j += 1
 
    arr[i], arr[m] = arr[m], arr[i]
 
    i += 1

print(f"Sorted array: {arr}")