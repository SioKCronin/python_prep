# Backtracking

Backtracking is a form of recursion that improves upon brute force by ruling
out options that can not deliver us the results we are looking for. I like to think
of it as taking a step a back if we hit a known dead-end, and then continue evaluating
other possible directions. We evaluate in some way, and if it's a "no-go" we back up
to the place we most recently made a decision, and explore any options that are still
viable.

## Permutations

Let's considering the following list permutation function taken from the website Brilliant:

```
def permutation(list, start, end):
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

To see what's happening, let's look first at what the for loop is doing in the `else`
statement. It is progressing through possible start positions, and swapping them
with indices further and further in the list. Notice how it starts by swapping the `start` (0)
with the first `i` (0) so is essentialy swapping the first number in the list (1) with itself. 
We see that in the output, as the first two permutations printed start with the number 1. 

From there, the recursive call advances through the start positions, swapping as it goes, 
only stopping to print when it reaches the end of the list
(or, a leaf if you imagine these permutations sprawling out as a tree). Notice how within
each pass through the `for` loop we are resetting the values so that the next `for` loop 
gets a fresh crack at a clean, reset list. 

## Sudoku

Let's check another example to gel this concept.

The goal of Sudoku is to fill an `n x n` grid such that each column, row, and subgrid
contains all of the numbers 1 to n exactly once. 

```
# This helper function checks for duplicate integers
def is_distinct(l):
    used = []
    for i in l:
        if i == 0:
            continue
        if i in used:
            return False
        used.append(i)
    return True

# This checks if the n x n board is valid (rewrite as generic)
def is_valid( brd ):
    for i in range(3):
        row = [brd[i][0],brd[i][1],brd[i][2]]
        if not is_distinct(row):
            return False
        col = [brd[0][i],brd[1][i],brd[2][i]]
        if not is_distinct(col):
            return False
    return True

# Here's where we solve the Sudoku board
def solve( brd , empties = 9):
    if empties == 0:
        return is_valid( brd )
    for row,col in product(range(3),repeat=2):
        cell = brd[row][col]
        if cell != 0:
            continue
        brd2 = copy( brd )
        for test in [1,2,3]:
            brd2[row][col] = test
            # If the integer has not already been used and leads to a successful solve
            if is_valid(brd2) and solve(brd2,empties-1): 
                return True
            brd2[row][col] = 0 #BackTrack
    return False
```

The helper function and "is board valid" functions are fairly straightforward, but 
check out what's going on as we get down to that second for loop in the solver. 
We only test possible numbers if the cell is 0, and once we do, the if statement
checks to see if the integer has already been used by calling `is_valid` and whether
or not it is possible to bring the board to finish line with that integer in that position, 
which is what's happening with that recursive call to solve with empties depracated by one. 
If those conditions are NOT met, the cell is restored to 0, and we move on. 

In this example, a copy of the board is made to use as a draft that can be marked up,
without mutating the board itself. Can you think of another way to keep track of these
solutions without creating a board copy?
