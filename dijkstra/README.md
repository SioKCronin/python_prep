# Dijkstra

Dijkstra's algorithm finds the shortest path between two nodes in a graph. This
means we're working with a weighted graph, where each edge has an associated weight.
For instance, if the nodes represent cities and the edges represent roads, the
weight of an edge connecting two nodes might represent the length of the road in meters
connecting those two cities. Or gas burned by a diesel truck. Or roadside coffees
consumed by a tourist. The goal of this algorithm is to find the shortest path, which
means all possible paths need to be assessed, to ensure we haven't overlooked anything. 

How can we efficiently test every possible route between two cities?

Let's take a look at an implementation.

```




```

Here's a lengthier implementation I find [helpful](https://dev.to/mxl/dijkstras-algorithm-in-python-algorithms-for-beginners-dkc)

# A\*

I like to think of A\* as a Dijkstra extension that leverages a cost function
that helps us get to the result faster (hopefully). 
