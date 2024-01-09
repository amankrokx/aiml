def aStarAlgo(start_node, stop_node):
    open_set = set([start_node])
    closed_set = set()
    g = {start_node: 0}
    parents = {start_node: start_node}

    while open_set:
        n = min(open_set, key=lambda x: g[x] + heuristic(x))
        
        if n == stop_node or not Graph_nodes[n]:
            break

        for m, weight in get_neighbors(n):
            tentative_g = g[n] + weight

            if m not in open_set and m not in closed_set:
                open_set.add(m)
                parents[m] = n
                g[m] = tentative_g
            else:
                if g.get(m, float('inf')) > tentative_g:
                    g[m] = tentative_g
                    parents[m] = n

                    if m in closed_set:
                        closed_set.remove(m)
                        open_set.add(m)

        open_set.remove(n)
        closed_set.add(n)

    if n != stop_node:
        print('Path does not exist!')
        return None

    path = []
    while parents[n] != n:
        path.append(n)
        n = parents[n]

    path.append(start_node)
    path.reverse()

    print('Path found:', path)
    return path

def get_neighbors(v):
    return Graph_nodes.get(v, [])

def heuristic(n):
    H_dist = {
        'A': 10, 'B': 8, 'C': 5, 'D': 7, 'E': 3,
        'F': 6, 'G': 5, 'H': 3, 'I': 1, 'J': 0
    }
    return H_dist[n]

Graph_nodes = {
    'A': [('B', 6), ('F', 3)],
    'B': [('C', 3), ('D', 2)],
    'C': [('D', 1), ('E', 5)],
    'D': [('C', 1), ('E', 8)],
    'E': [('I', 5), ('J', 5)],
    'F': [('G', 1), ('H', 7)],
    'G': [('I', 3)],
    'H': [('I', 2)],
    'I': [('E', 5), ('J', 3)],
}

aStarAlgo('A', 'J')
