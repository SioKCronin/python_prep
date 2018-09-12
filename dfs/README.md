# Depth-First Search

## Graph representation
* edge lists
```
    prerequisites = [[0,1], [0,2]]
    
    graph = collections.defaultdict(list)
    for course, pre_course in prerequisites:
        graph[pre_course].append(course)
    seen, in_stack = set(), set()

```
* adjacency map
```
adjacency_matrix = {1: [2, 3],
                    2: [4, 5],
                    3: [5],
                    4: [6],
                    5: [6]}                 
```
* object (node with children)

## Structure
* Iterative
```
def dfs(graph, start):
    visited = set()
    stack = [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.append(graph[vertex] - visited)
    return visited
```
* Recursive
```
def dfs_recursive(graph, vertex, path=[]):
    path += [vertex]

    for neighbor in graph[vertex]:
        if neighbor not in path:
            path = dfs_recursive(graph, neighbor, path)

    return path
    
dfs_recursive(adjacency_matrix, 1)
```

## Data structures
* visited sets
* stack

## Data to Return
* min/max depth length
```
def minDepth(self, root, depth=0):
    if not root:
        return depth
    depth += 1
    return min(self.minDepth(root.left, depth), self.minDepth(root.right, depth))
```
* any path between two nodes
```
def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))
```
* all unique paths between to nodes
* sum between two nodes (if path exists)
