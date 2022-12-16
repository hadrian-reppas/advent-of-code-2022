from collections import deque
from math import inf
from shared import graph, rates


def edge_weight(a, b):
    if a == b:
        return 0
    elif b not in graph[a]:
        return inf
    return graph[a][b]


distance = {a: {b: edge_weight(a, b) for b in graph} for a in graph}

for a in graph:
    for b in graph:
        for c in graph:
            if distance[b][a] + distance[a][c] < distance[b][c]:
                distance[b][c] = distance[b][a] + distance[a][c]

pressures = {}
queue = deque([("AA", 0, 26, frozenset())])
while queue:
    node, pressure, time, visited = queue.popleft()
    if visited in pressures:
        pressures[visited] = max(pressures[visited], pressure)
    else:
        pressures[visited] = pressure

    is_close = lambda other: distance[node][other] < time
    for other in filter(is_close, set(graph) - visited):
        dp = (time - distance[node][other] - 1) * rates[other]
        new_visited = visited | frozenset([other])
        queue.append(
            (other, pressure + dp, time - distance[node][other] - 1, new_visited)
        )

max_pressure = 0
for (human, human_pressure) in pressures.items():
    for (elephant, elephant_pressure) in pressures.items():
        if not human & elephant:
            max_pressure = max(
                max_pressure,
                human_pressure + elephant_pressure,
            )

print(max_pressure)
