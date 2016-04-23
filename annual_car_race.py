# https://www.hackerrank.com/contests/womens-codesprint/challenges/annual-car-race
test_cases = int(raw_input().strip())

graphs = []
for t in range(test_cases):
    second_line = map(int,raw_input().strip().split(' '))
    # vertices
    number_stops = second_line[0]
    # edges
    number_roads = second_line[1]

    third_line = map(int,raw_input().strip().split(' '))
    s = third_line[0]
    t = third_line[1]

    nodes = []
    for r in range(number_roads):
        road = map(int,raw_input().strip().split(' '))
        nodes.append(road)

    graph = {}
    # construct the graph of the race
    all_nodes = []
    for node in nodes:
        st = node[0]
        e = node[1]
        all_nodes = list(set(all_nodes) | set([st, e]))
        dist = node[2]
        if st in graph.keys():
            graph[st][e] = dist
        else:
             graph[st] = {}
             graph[st][e] = dist

    graph[t] = {}
    graphs.append({'graph': graph, 'start': s, 'end': t, 'nodes': all_nodes})


for gidx in range(test_cases):
    graph_objs = graphs[gidx]
    graph = graph_objs['graph']
    all_nodes = graph_objs['nodes']
    s = graph_objs['start']
    t = graph_objs['end']
    # set of shortest paths from s to t
    P = []

    # s: the source node
    # s = 0
    # # t: the destination node
    # t = 6
    # K: the number of shortest paths to find
    K = 3

    # number of shortest paths found to node u
    counts = dict.fromkeys(all_nodes, 0)
    counts[t] = 0

    # B is a heap data structure containing paths
    # insert path Ps = {s} into B with cost 0
    # keys are list of the path
    # value are total cost of the path
    B = {tuple([s]): 0}
    final_cost = -1
    while len(B) > 0 and counts[t] < K:
        # let Pu be the shortest cost path in B with cost C
        C = min(B.values())
        pos_of_min_cost = B.values().index(C)
        Pu = B.keys()[pos_of_min_cost]
        # last node in this path
        # fixme
        u = Pu[-1]
        cost = B.pop(Pu)
        counts[u] += 1
        # if u = t then P = P U Pu
        # print P
        # print Pu
        # not positive this is doing the right thing
        if u == t: P = set(P) | set([Pu])
        # if countu <= K then
        if counts[u] < K:
            if u in graph.keys():
                # for each vertex v adjacent to u:
                vertices_adj_u = graph[u].keys()
                for v in vertices_adj_u:
                    # if v is not in Pu then
                    if v not in Pu:
                        # let Pv be a new path with cost C + w(u, v) formed by concatenating edge (u, v) to path Pu
                        Cv = C + graph[u][v]
                        # insert Pv into B
                        B[Pu + tuple([v])] = Cv
    print B.values()[0] if len(B.values()) > 0 else -1


