class DisjointSetForest:
    def __init__(self, nodes):
        self._parent = {node: node for node in nodes}
        self._rank = {node: 0 for node in nodes}

    def find(self, x):
        root = x
        while self._parent[root] != root:
            root = self._parent[root]
        while self._parent[x] != root:
            self._parent[x], x = root, self._parent[x]
        return root

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return
        if self._rank[rx] < self._rank[ry]:
            rx, ry = ry, rx
        self._parent[ry] = rx
        if self._rank[rx] == self._rank[ry]:
            self._rank[rx] += 1
    def in_same_set(self, x, y):
        return self.find(x) == self.find(y)


def slc(graph, d, k):

    components = DisjointSetForest(graph.nodes)
    num_components = len(graph.nodes)
    for edge in sorted(graph.edges, key=d):
        if num_components <= k:
            break
        u, v = edge
        if not components.in_same_set(u, v):
            components.union(u, v)
            num_components -= 1
    clusters = {}
    for node in graph.nodes:
        rep = components.find(node)
        clusters.setdefault(rep, set()).add(node)
    return frozenset(frozenset(cluster) for cluster in clusters.values())