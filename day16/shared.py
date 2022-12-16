rates = {}
graph = {}
for line in open("input.txt").read().split("\n"):
    _, node, _, _, rate, _, _, _, _, *edges = line.split()
    rates[node] = int(rate[5:-1])
    graph[node] = {edge[:2]: 1 for edge in edges}

while True:
    for node, neighbors in graph.items():
        if rates[node] == 0 and len(neighbors) == 2:
            (a, aw), (b, bw) = neighbors.items()
            del graph[node]
            del graph[a][node]
            del graph[b][node]
            graph[a][b] = aw + bw
            graph[b][a] = aw + bw
            break
    else:
        break
