# Digit constraints
#
# There are N integers with 77 digits, such that the sum of any three consecutive
# integers is at most 7. Find N. 

d = dict()

for n in range(2, 78):
    for i in range(8):
        for j in range(8):
            d[n, i, j] = 0

