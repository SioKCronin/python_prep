import unittest
import pprint
from collections import defaultdict
import bisect

'''
Given an undirected graph G, find the minimum spanning tree within G.
A minimum spanning tree connects all vertices in a graph with the smallest possible
total weight of edges. Your function should take in and return an adjacency list structured like this:
{'A': [('B', 2)],
 'B': [('A', 2), ('C', 5)],
 'C': [('B', 5)]}
'''
class TestSpanningTree(unittest.TestCase):

    def test_graph_is_already_minimum_spanning_tree(self):
        tree = {'A': [('B', 2)],
 
                'B': [('A', 2), ('C', 5)],
                'C': [('B', 5)]}
        self.assertEqual(question3(tree), tree)

    def test_broad_tree(self):
        input_tree = {'A': [('B', 2)],
                      'B': [('A', 2), ('C', 5), ('D', 3)],
                      'C': [('B', 5), ('D', 1), ('E', 2)],
                      'D': [('B', 3), ('C', 1)],
                      'E': [('C', 2)]}

        output_tree = {'A': [('B', 2)],
                       'B': [('A', 2), ('D', 3)],
                       'C': [('D', 1), ('E', 2)],
                       'D': [('B', 3), ('C', 1)],
                       'E': [('C', 2)]}

def sorted_edge_weights(graph):
    edges = set()
    for n1 in graph:
        for n2, weight in graph[n1]:
            edges.add((weight, tuple(sorted((n1, n2)))))
    return sorted(list(edges))

def build_new_tree(graph):
    edges = sorted_edge_weights(graph)
    new_tree = defaultdict(list)
    connected_nodes = set()
    weight, (n1, n2) = edges.pop(0)
    bisect.insort(new_tree[n1], (n2, weight))
    bisect.insort(new_tree[n2], (n1, weight))
    connected_nodes.add(n1) 
    connected_nodes.add(n2)

    while len(graph) > len(connected_nodes):
        for i, edge in enumerate(edges):
            weight, (n1, n2) = edge
            if n1 not in connected_nodes and n2 not in connected_nodes:
                continue
            if n1 in connected_nodes and n2 in connected_nodes:
                continue
            connected_nodes.add(n1) 
            connected_nodes.add(n2)
            bisect.insort(new_tree[n1], (n2, weight))
            bisect.insort(new_tree[n2], (n1, weight))
    return dict(new_tree)

def question3(graph):
    return build_new_tree(graph)

if __name__ == '__main__':
    unittest.main()
