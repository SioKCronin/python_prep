# Breadth First Search

def breadth_first_search(G,s):
    for vertex in G.vertex:
        vertex.color = 'white'
        vertex.distance = distance(vertex,s)
        vertex.parent = none
    s.color = 'gray'
    s.distance = 0
    vetex.parent = none
    Q = Queue()
    while Q != 0:
        u = ???
        for vertex in u.adjacent:
            if vertex.color == 'white':
                v.color = 'gray'
                vertex.distance = distance(u,s) + 1
                vertex.parent = u
                enqueue(Q, vertex) ???
        dequeue(Q) ???
        u.color = 'black'
