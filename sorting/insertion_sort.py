# Insertion Sort - O(n^2)

def insertion_sort(data):
    for i in range(1, len(data)):
        current = data[i]
        position = i

        while position > 0 and current < data[position-1]:
            data[position] = data[position-1]
            position -= 1

        data[position] = current

    return data

test1 = [5, 4, 3, 2, 1]
test2 = [1, 4, 2, 3, 5]

print(insertion_sort(test1))
print(insertion_sort(test2))

