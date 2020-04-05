# Graph

## Representations of Graphs

We can choose between two standard ways to represent a graph G = (V, E) : as a collection of 
adjacency lists or as an adjacency matrix. Either way applies to both directed and undirected 
graphs. Because the adjacency-list representation provides a compact way to 
represent sparse graphs—those for which |E| is much less than |V|<sup>2</sup> — it is usually 
the method of choice. 

## BFS

Breadth-first search is one of the simplest algorithms for searching a graph and the archetype 
for many important graph algorithms. Prim’s minimum-spanning tree algorithm and Dijkstra’s 
single-source shortest-paths algorithm use ideas similar to those in breadth-first search.


```
BFS(G, s)
    for each vertex u ∈ G.V - {s}
        u.color = WHITE
        u.d = ∞
        u.π = NIL
    u.color = GRAY
    u.d = 0
    u.π = NIL
    Q = ∅
    ENQUEUE(Q, s)
    while Q ≠ ∅
        u = DEQUEUE(Q)
        for each v ∈ G.Adj[u]
            if v.color == WHITE
                v.color = GRAY
                v.d = u.d + 1
                v.π = u
                ENQUEUE(Q, v)
        u.color = BLACK
```

Time complexity: O(V + E)

## DFS
 
The strategy followed by depth-first search is, as its name implies, to search
“deeper” in the graph whenever possible. Depth-first search explores edges out
of the most recently discovered vertex v that still has unexplored edges leaving it.
Once all of v’s edges have been explored, the search “backtracks” to explore edges
leaving the vertex from which v was discovered. This process continues until we
have discovered all the vertices that are reachable from the original source vertex.
If any undiscovered vertices remain, then depth-first search selects one of them as
a new source, and it repeats the search from that source. The algorithm repeats this
entire process until it has discovered every vertex.

```
DFS(G)
    for each vertex u ∈ G.V
        u.color = WHITE
        u.π = NIL   
    time = 0
    for each vertex u ∈ G.V
        if u.color = WHITE
            DFS-VISIT(G, u)

DFS-VISIT(G, u)
    time = time + 1                // white vertex u has just been discovered
    u.d = time
    u.color = GRAY
    for each v ∈ G.Adj[u]         // explore edge (u, v)
        if v.color == WHITE
            v.π = u
            DFS-VISIT(G, v)
        u.color = BLACK           // blacken u; it is finished
        time = time + 1
    u.f = time
```

## Minimum Spanning Trees


## Single-Source Shortest Paths


## All-Pairs Shortest Paths


## Maximum Flow


## LeetCode problems

### easy
Problems|Solutions
---|---

### medium
Problems|Solutions
---|---

### hard
Problems|Solutions
---|---

## Reference
1. Cormen, Thomas H., Charles E. Leiserson, Ronald L. Rivest, and Clifford Stein. Introduction to algorithms. MIT press, 2009.