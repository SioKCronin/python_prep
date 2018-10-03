## Bellman-Ford Algorithm

While slower than Dijkstra's, this algorithm has the advantage of being able to
handle graphs where some edges are negative numbers. The algorithm can detect
"negative cycles" (where a pass around sums to a negative value), which would mean
there is not definitive shorter path (since any shortest path with a node in the 
negative cycle can be made shorter by passing through the negative cycle again). 

Unlike Dijkstra's algorithm which processes the closest vertex which has not yet
been processed, Bellman-Ford "relaxes" all edges V-1 times. The complexity is 
O(V*E).
