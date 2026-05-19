from collections import deque
def cluster(graph, weights, level):
    visited=set()
    clusters=[]

    for start in graph.nodes:
        if start in visited:
            continue

        component=set()
        queue=deque([start])
        visited.add(start)

        while queue:
            u=queue.popleft()
            component.add(u)

            for v in graph.neighbors(u):
                if v in visited:
                    continue
                if weights(u,v)<level:
                    continue
                visited.add(v)
                queue.append(v)
        clusters.append(frozenset(component))
    return frozenset(clusters)