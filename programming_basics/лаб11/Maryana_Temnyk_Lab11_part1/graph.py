# Complete all of the following functions. Currently they all just
# 'pass' rather than explicitly return value, which means that they
# implicitly return None.


def get_graph_from_file(file_name):
    """
    (str) -> (list)

    Read graph from file and return a list of edges.

    >>> get_graph_from_file("data1.txt")
    [[1, 2], [3, 4], [1, 5]]
    """
    with open(file_name, 'r') as file_gr:
        gr_lst = []
        gr = file_gr.read().split('\n')
        for edge in gr:
            edge = edge.split(',')
            for i in range(len(edge)):
                edge[i] = int(edge[i])
            gr_lst.append(edge)
        return gr_lst


def to_edge_dict(edge_list):
    """
    (list) -> (dict)

    Precondition: list must contain only pairs of numbers,
    representing edges.

    Convert a graph from list of edges to dictionary of vertices.

    >>> to_edge_dict([[1, 2], [3, 4], [1, 5], [2, 4], [2, 1]])
    {1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}
    """
    values = []
    for edge in edge_list:
        values.extend(edge)
    values = set(values)
    edge_list2 = []
    for val in values:
        a = []
        for edge in edge_list:
            if val in edge:
                a.extend(edge)
                a.remove(val)
        a = list(set(a))
        edge_list2.append((val, a))
    return dict(edge_list2)


def is_edge_in_graph(graph, edge):
    """
    (dict, tuple) -> dict

    Return True if graph contains a given edge and False otherwise.

    >>> is_edge_in_graph({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (3, 1))
    False
    >>> is_edge_in_graph({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (6, 7))
    False
    """
    if edge[1] not in graph or edge[0] not in graph:
        return False
    elif edge[1] in graph[edge[0]] or edge[0] in graph[edge[1]]:
        return True
    else:
        return False


def add_edge(graph, edge):
    """
    (dict, tuple) -> dict

    Add a new edge to the graph and return new graph.

    >>> add_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (1, 3))
    {1: [2, 5, 3], 2: [1, 4], 3: [4, 1], 4: [2, 3], 5: [1]}
    >>> add_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (6, 7))
    {1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1], 6: [7], 7: [6]}
    >>> add_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (1, 7))
    {1: [2, 5, 7], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1], 7: [1]}
    >>> add_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (1, 2))
    {1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}
    """
    if is_edge_in_graph(graph, edge):
        return graph
    elif edge[1] in graph and edge[0] in graph:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    elif edge[1] in graph and edge[0] not in graph:
        graph[edge[1]].append(edge[0])
        graph[edge[0]] = [edge[1]]
    elif edge[0] in graph and edge[1] not in graph:
        graph[edge[0]].append(edge[1])
        graph[edge[1]] = [edge[0]]
    else:
        graph[edge[1]] = [edge[0]]
        graph[edge[0]] = [edge[1]]
    return graph


def del_edge(graph, edge):
    """
    (dict, tuple) -> (dict)

    Precondition: edge must be in given graph.

    Delete an edge from the graph and return a new graph.

    >>> del_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (2, 4))
    {1: [2, 5], 2: [1], 3: [4], 4: [3], 5: [1]}
    >>> del_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (3, 4))
    {1: [2, 5], 2: [1, 4], 3: [], 4: [2], 5: [1]}
    >>> del_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (6, 7))
    {1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}
    """
    if not is_edge_in_graph(graph, edge):
        return graph
    else:
        graph[edge[0]].remove(edge[1])
        graph[edge[1]].remove(edge[0])
        return graph


def add_node(graph, node):
    """
    (dict, int) -> (dict)

    Add a new node to the graph and return a new graph.

    >>> add_node({1: [2], 2: [1]}, 3)
    {1: [2], 2: [1], 3: []}
    """
    if node not in graph:
        graph[node] = []
    return graph


def del_node(graph, node):
    """
    (dict, int) -> (dict)

    Delete a node and all incident edges from the graph.

    >>> del_node({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, 4)
    {1: [2, 5], 2: [1], 3: [], 5: [1]}
    >>> del_node({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, 7)
    {1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}
    """
    if node in graph:
        del graph[node]
        for vert in graph:
            if node in graph[vert]:
                graph[vert].remove(node)
    return graph


def convert_to_dot(graph):
    """
    (dict) -> (None)

    Save the graph to a file in a DOT format.
    """
    key_lst = list(graph.keys())
    vert_lst = reversed(list(graph.keys()))
    for vert in vert_lst:
        for key in key_lst:
            if key in graph[vert]:
                graph[vert].remove(key)
        if graph[vert] == []:
            del graph[vert]
        key_lst.remove(vert)
    with open('graph.DOT', 'w') as file:
        file.write('graph {\n')
        for node in graph:
            if len(graph[node]) > 1:
                file.write(str(node) + ' -- ' + str(set(graph[node])) + ';\n')
            else:
                file.write(str(node) + ' -- ' + str(graph[node][0]) + ';\n')
        file.write('}')


import doctest
if __name__ == '__main__':
    print(doctest.testmod())
