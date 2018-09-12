# Quick Sort - O(n log(n)) average, and O(n^2) worst

# Pick a random element and partition the array - all numbers
# that are less then the partitioning array come before all the numbers
# that are greater than it (through a series of swaps)

import numpy as np

test1 = [5, 4, 3, 2, 1]
test2 = [4, 1, 3, 2, 5]

def quick_sort_random(data):
    if len(data) == 0:
        return
    if len(data) == 1:
        return data
    if len(data) == 2:
        if data[0] > data[1]:
            return [data[1], data[0]]
        else:
            return data
    pivot_idx = np.random.randint(0, len(data)-1)
    print("Pivot", pivot_idx)
    data1 = data[:pivot_idx]
    data2 = data[pivot_idx:]
    return quick_sort_random(data1) + quick_sort_random(data2)

print(quick_sort_random(test1))



