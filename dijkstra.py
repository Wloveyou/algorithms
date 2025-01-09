import sys
import heapq

INF = sys.maxsize

def dijkstra(start, graph):
    n = len(graph)
    dist = [INF] * n
    visited = [False] * n

    dist[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, u = heapq.heappop(priority_queue)

        if visited[u]:
            continue

        visited[u] = True

        for v, weight in graph[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                heapq.heappush(priority_queue, (dist[v], v))

    print(f"Кратчайшие расстояния от вершины {start}:")
    for i in range(n):
        print(f"До вершины {i} расстояние: {'бесконечность' if dist[i] == INF else dist[i]}")

if __name__ == "__main__":
    n, m = map(int, input("Введите количество вершин и рёбер: ").split())
    graph = [[] for _ in range(n)]

    print("Введите рёбра в формате (u v вес):")
    for _ in range(m):
        u, v, weight = map(int, input().split())
        graph[u].append((v, weight))
        graph[v].append((u, weight))  # Для неориентированного графа

    start = int(input("Введите начальную вершину: "))
    dijkstra(start, graph)
