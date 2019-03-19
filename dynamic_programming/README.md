# Dynamic Programming

The big idea behind dynamic programming is that we want to explore multiple possible
branches, but notice we can exploit the fact that there are overlapping sub-branches,
which means we can log data from these sub-branches so we don't have to calculate
the same thing over and over again. We'll call those logs **memos**.

There are two flavors of Dynamic Programming, **top-down** and **bottom-up**, which
we'll explore anon, yet first, let's observe how we might insert a memo into
a recursive implmentation of function calculating the nth Fibonnaci number.

## Fibonnaci

Here's a classic recursive Fibonnaci implementation:

```
def nth_fibonnaci_recursive(n):
    if n <= 0: return 0
    if n == 1: return 1
    else: 
        return nth_fibonnaci_recursive(n-2) + nth_fibonnaci_recursive(n-1) 
```
It's tidy code, but we're stacking up to O(2^n) as we're adding two calls to the
callstack for each pass through. And there's a redundancy across the branches.
Let's see how we might store values and bring in a lookup to optimize this function.

Let's start by creating a list of 0's of length $n + 1$ (so we can store calculated
values for each number less than or equal to n). 

```
memo = [0] * (n + 1)

# Top Down approach
def topdown_dp_fibonnaci(n, memo):
    if n == 0 or n == 1: return n
    if memo[n] == 0:
        memo[n] = topdown_dp_fibonnaci(n-1, memo) + topdown_dp_fibonnaci(n-2, memo)
    return memo[n]
```
All we had to do was pass the memo in, and, voila!, we've reduced our run time
to O(n). Do you see why? We only calculate the function once for each unique 
number less than or equal to n. This style is considered the top down approach.
Why? 

Perhaps the answer will become clearer as we examine the bottom up approach. This 
time, instead of building up our memor from n-1 and n-2, we'll start with the base
cases of 0 and 1 and build up the memo from the bottom.

```
# Bottom Up approach
def bottom_up_dp_fibonnaci(n):
    if n == 0: return 0
    a, b = 0, 1
    for i in range(2, n):
        c = a + b
        a = b
        b = c
    return a + b
```
This is still employing **memoization**, only we only need the past previous
two numbers in order to calculate the current position's total. I believe this 
is DP (what the cool kids call Dynamic Programming) at its finest. We are not
only saving ourselves from excessive function calls, we are also optimizing our
storage needs so we only keep track of what need to solve the problem.

## Coin Change

Let's take a look at one more example, the classic Coin Change problem. 

This is a problem you will have encountered if you've ever had a job where you
had to give change back to customers. Someone would like to buy a package of Skittles,
which costs 30 cents in this wishful thinking example, and hands you a dollar. You
scan the Skittles, the cash machine pops open, and you're faced with the question
of which coins to return to them. Perhaps instinctively, you optimize to return the
fewest coins possible to cover the 70 cents you owe the customer (which would be
two quarters and two dimes), but how would you write that up as an algorithm?

Like our Top Down approach above, we'll need some way to keep track of our memos,
so let's kick things off with a list of 0s.

```
def dp_coin_changer(coin_value_list, change, i, memo=[]):
    if i == -1:
        return -1

    memo.append(coin_value_list[i])
    s = round(sum(memo), 2)

    if s < change:
        return dp_coin_changer(coin_value_list, change, i, memo)

    if s > change:
        memo.pop()
        i -= 1
        return dp_coin_changer(coin_value_list, change, i, memo)

    return len(memo)
```
