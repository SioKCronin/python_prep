# Backtracking

Backtracking is a form of recursion that improves upon brute force by ruling
out options that can not deliver us the results we are looking for. I like to think
of it as taking a step a back if we hit a known dead-end, and then continue evaluating
other possible directions. We evaluate in some way, and if it's a "no-go" we back up
to the place we most recently made a decision, and explore any options that are still
viable. 

Let's considering the following backtracking function taken from the website Brilliant:

```
def permutation(list, start, end):
    '''This prints all the permutations of a given list
       it takes the list, the starting and ending indices as input'''
    if (start == end):
        print list
    else:
        for i in range(start, end + 1):
            list[start], list[i] = list[i], list[start]  # The swapping
            permutation(list, start + 1, end)
            list[start], list[i] = list[i], list[start]  # Backtracking

permutation([1, 2, 3], 0, 2)

>>>
[1, 2, 3]
[1, 3, 2]
[2, 1, 3]
[2, 3, 1]
[3, 2, 1]
[3, 1, 2]
```

To see what's happening, let's look first at what the for loop is doing in the else
statement. It is progressing through possible start positions, and swapping them
with indices further and further in the list. Notice how it starts by swapping the start (0)
with the first i (0) so is essentialy starting the first number in the list (1) with itself. 
We see that in the output, as the first two permutations printed start with the number 1. 

From there, the recursive call advances through the start positions, much as the outer loop does,
swapping as it goes, only stopping to print when it reaches the end of the list
(or, a leaf if you imagine these permutations sprawling out as a tree). Notice how within
each pass through the for loop we are resetting the values so that the next for loop 
gets a fresh crack at a clean, reset list to work with. 

Let's check out another example to gel this concept.

