# From Brilliant (https://brilliant.org/wiki/recursive-backtracking/)

def permutation(l, start, end):
    '''This prints all the permutations of a given list
       it takes the list,the starting and ending indices as input'''
    if (start == len(l) - 1):
        print(l)
    else:
        for i in range(start, end + 1):
            l[start], l[i] = l[i], l[start]  # The swapping
            permutation(l, start + 1, end)
            l[start], l[i] = l[i], l[start]  # Backtracking


permutation([1, 2, 3], 0, 2)  # The first index of a list is zero
