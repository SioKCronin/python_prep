# Bubble Sort - O(n^2)

# Start at the beginning of the array and swap the first two elements,
# if the first is greater than the second. Then go to the next pair.
# Continue to make sweeps over the array until the entire array is sorted 

def bubble_sort(data):
    while True:
        hold = None
        for i in range(len(data)-1):
            if data[i] > data[i+1]:
                hold = data[i]
                data[i] = data[i+1]
                data[i+1] = hold
        if hold == None: return data

test1 = [5, 4, 3, 2, 1]
test2 = [1, 4, 2, 3, 5]

print(bubble_sort(test1))
print(bubble_sort(test2))

