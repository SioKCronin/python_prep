# Merge sort - O(n log(n))

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

test1 = [5, 4, 3, 2, 1]
test2 = [4, 1, 3, 2, 5]

print(merge_sort(test1))
print(merge_sort(test2))
