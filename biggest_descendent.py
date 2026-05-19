
def biggest_descendent(graph,root,value):
    result ={}
    def dfs(u):
        best=value[u]

        for child in graph.neighbors(u):
            child_best=dfs(child)
            if child_best>best:
                best=child_best
        result[u]=best
        return best
    dfs(root)
    return result

