import dsc40graph

def assign_good_and_evil(graph):
    labels={}

    for start_node in graph.nodes:
        if start_node in labels:
            continue
        labels[start_node]='good';
        queue=[start_node]

        while queue:
            current= queue.pop(0)
            if(labels[current]=='good'):
                neighbor_label='evil'
            else:
                neighbor_label='good'

            for neighbor in graph.neighbors(current):
                if neighbor not in labels:
                    labels [neighbor]=neighbor_label
                    queue.append(neighbor)
                elif labels[neighbor]!=neighbor_label:
                    return None
    return labels

