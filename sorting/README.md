# Sorting

## O(n^2)

### Bubble Sort

```
def bubble_sort(data):
    while True:
        hold = None
        for i in range(len(data)-1):
            if data[i] > data[i+1]:
                # Swap
                hold = data[i]
                data[i] = data[i+1]
                data[i+1] = hold
        if hold == None: return data
```

### Insertion Sort

```
def insertion_sort(data):
    for i in range(1, len(data)):
        current = data[i]
        position = i

        while position > 0 and current < data[position-1]:
            data[position] = data[position-1]
            position -= 1

        data[position] = current

    return data
```

## O (n log n)

### Merge Sort

```
def merge(left, right):
     left_idx, right_idx = 0, 0
     result = []
     while left_idx < len(left) and right_idx < len(right):
         if left[left_idx] < right[right_idx]:
             result.append(left[left_idx])
             left_idx += 1
         else:
             result.append(right[right_idx])
             right_idx += 1

     result += left[left_idx:]
     result += right[right_idx:]
     return result

def merge_sort(data):
     if len(data) <= 1:
         return data

     half = len(data) // 2
     left = merge_sort(data[:half])
     right = merge_sort(data[half:])

     return merge(left, right)
```

### Quicksort

```
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
```
