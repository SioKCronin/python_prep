def beautiful_arrangements(l, start):
    print(l, l[start:])
    if start == (len(l)-1):
        print("*match")
        return 1
    count = 0
    for i in range(start, len(l)):
        print('swapping indexes ', i, ' <-> ', start)
        l[start], l[i] = l[i], l[start]
        print('checking values ', i+1, 'and', l[i])
        if l[i] % (i+1) != 0 and (i+1) % l[i] != 0:
            l[start], l[i] = l[i], l[start] #backtracking
            continue
        count += beautiful_arrangements(l, start+1)
    return count

class Solution(object):
    def countArrangement(self, N):
        l = [x for x in range(1, N+1)]
        return beautiful_arrangements(l, 0)

s = Solution()
# print("Results for 2:", s.countArrangement(2))
print("Results for 3:", s.countArrangement(3))
# print("Results for 4:", s.countArrangement(4))
