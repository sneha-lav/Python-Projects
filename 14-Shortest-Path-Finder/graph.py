import heapq


graph = {
    "A": {"B": 4, "C": 2},
    "B": {"A": 4, "C": 1, "D": 5},
    "C": {"A": 2, "B": 1, "D": 8, "E": 10},
    "D": {"B": 5, "C": 8, "E": 2},
    "E": {"C": 10, "D": 2}
}


def dijkstra(start, end):

    queue = [(0, start, [])]
    visited = set()

    while queue:

        cost, node, path = heapq.heappop(queue)

        if node in visited:
            continue

        path = path + [node]
        visited.add(node)

        if node == end:
            return cost, path

        for neighbor, weight in graph[node].items():

            if neighbor not in visited:
                heapq.heappush(
                    queue,
                    (cost + weight, neighbor, path)
                )

    return None, []