# Selection Sort - O(n^2)

def selection_sort(data):
    for slot in range(len(data)-1, 0, -1): # Reverse approach
        max_position=0
        for location in range(1, slot+1):
            if data[location] > data[max_position]:
                max_position = location

        #Here's the swap
        temp = data[slot]
        data[slot] = data[max_position]
        data[max_position] = temp

    return data

test1 = [5, 4, 3, 2, 1]
test2 = [1, 4, 2, 3, 5]

print(selection_sort(test1))
print(selection_sort(test2))

