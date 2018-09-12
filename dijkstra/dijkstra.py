from collections import defaultdict
from heapq import *
import unittest

edges = [("A", "B", 7),
        ("A", "D", 5),
        ("B", "C", 8),
        ("B", "D", 9),
        ("B", "E", 7),
        ("C", "E", 5),
        ("D", "E", 15),
        ("D", "F", 6),
        ("E", "F", 8),
        ("E", "G", 9),
        ("F", "G", 11)
        ]

class TestDijkstra(unittest.TestCase):

    def test_edges(self):
        self.assertEqual(dijkstra(edges, 'A', 'E'), (14, ('A', 'B', 'E')))
        self.assertEqual(dijkstra(edges, 'F', 'G'), (11, ('F', 'G')))

def dijkstra(edges, f, t):
    g = defaultdict(list)
    for l,r,c in edges:
        g[l].append((c,r))

    p_queue = [(0,f,())]   # priorty queue implemented with heapq
    seen = set()           # set of all seen nodes
    dist = {f: 0}          # map of the min value for each node in heap

    while p_queue:
        (cost,v1,path) = heappop(p_queue)
        if v1 in seen: continue

        seen.add(v1)
        path += (v1,)
        if v1 == t: return (cost, path)

        for c, v2 in g.get(v1, ()):
            if v2 in seen: continue

            # Not every edge will be calculated.
            # The edge which can improve the value of node in heap will be useful.
            if v2 not in dist or cost+c < dist[v2]:
                dist[v2] = cost+c
                heappush(p_queue, (cost+c, v2, path))

    return float("inf")

if __name__ == "__main__":
    unittest.main()
