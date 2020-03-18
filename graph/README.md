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

Given a graph G = (V, E) and a distinguished source vertex s, breadth-first
search systematically explores the edges of G to “discover” every vertex that is
reachable from s. It computes the distance (smallest number of edges) from s
to each reachable vertex. It also produces a “breadth-first tree” with root s that
contains all reachable vertices. For any vertex v reachable from s, the simple path
in the breadth-first tree from s to v corresponds to a “shortest path” from s to v
in G, that is, a path containing the smallest number of edges. The algorithm works
on both directed and undirected graphs.

Breadth-first search is so named because it expands the frontier between discovered 
and undiscovered vertices uniformly across the breadth of the frontier. That
is, the algorithm discovers all vertices at distance k from s before discovering any
vertices at distance k + 1.

To keep track of progress, breadth-first search colors each vertex white, gray, or
black. All vertices start out white and may later become gray and then black. A
vertex is discovered the first time it is encountered during the search, at which time
it becomes nonwhite. Gray and black vertices, therefore, have been discovered, but
breadth-first search distinguishes between them to ensure that the search proceeds
in a breadth-first manner. If (u, v) ∈ E and vertex u is black, then vertex v
is either gray or black; that is, all vertices adjacent to black vertices have been
discovered. Gray vertices may have some adjacent white vertices; they represent
the frontier between discovered and undiscovered vertices.

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
of the most recently discovered vertex  that still has unexplored edges leaving it.
Once all of v’s edges have been explored, the search “backtracks” to explore edges
leaving the vertex from which v was discovered. This process continues until we
have discovered all the vertices that are reachable from the original source vertex.
If any undiscovered vertices remain, then depth-first search selects one of them as
a new source, and it repeats the search from that source. The algorithm repeats this
entire process until it has discovered every vertex.

As in breadth-first search, whenever depth-first search discovers a vertex v during a 
scan of the adjacency list of an already discovered vertex u, it records this
event by setting v’s predecessor attribute v.π to u. Unlike breadth-first search,
whose predecessor subgraph forms a tree, the predecessor subgraph produced by
a depth-first search may be composed of several trees, because the search may
repeat from multiple sources. The predecessor subgraph of a depth-first search forms a 
depth-first forest comprising several depth-first trees.

As in breadth-first search, depth-first search colors vertices during the search to
indicate their state. Each vertex is initially white, is grayed when it is discovered
in the search, and is blackened when it is finished, that is, when its adjacency list
has been examined completely. This technique guarantees that each vertex ends up
in exactly one depth-first tree, so that these trees are disjoint.

Besides creating a depth-first forest, depth-first search also timestamps each vertex.
Each vertex v has two timestamps: the first timestamp v.d records when v
is first discovered (and grayed), and the second timestamp v.f records when the
search finishes examining v’s adjacency list (and blackens v). These timestamps provide
 important information about the structure of the graph and are generally
helpful in reasoning about the behavior of depth-first search.

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