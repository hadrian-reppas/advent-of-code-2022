from shared import graph, rates

max_pressure = 0


def visit(node, pressure, rate, time, unlocked, visited):
    if node in visited:
        return
    global max_pressure
    max_pressure = max(max_pressure, pressure + rate * time)
    if node not in unlocked and time > 0:
        visit(
            node,
            pressure + rate,
            rate + rates[node],
            time - 1,
            unlocked | {node},
            visited,
        )
    for neighbor, dist in graph[node].items():
        if dist < time:
            visit(
                neighbor,
                pressure + rate * dist,
                rate,
                time - dist,
                unlocked,
                visited | {node},
            )


visit("AA", 0, 0, 30, {"AA"}, set())

print(max_pressure)
