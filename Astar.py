import math

inf = float('inf')
sqrt = math.sqrt


def get_path(visted, current):
    path = [current]
    while current in visted:
        current = visted[current]
        path = [current] + path
    return path


# funkcja rekonstruująca ścieżkę z
# kolejnych odwiedzonych wierzchołków


def astar(graph, heuristic, init, goal):
    came_from = {}
    openset = [init]
    # wpisanie wierzchołka startowego do listy dostępnych
    # utworzenie słownika przejść
    g_score = [inf for i in range(len(graph))]
    g_score[init - 1] = 0
    # stworzenie wektora najbardziej optymalnej trasy
    f_score = [inf for i in range(len(graph))]
    f_score[init - 1] = heuristic[init - 1]
    print(heuristic, f_score)
    # stworzenie wektora przybliżonej wartości drogi od bieżącego do końcowego wierchołka
    while len(openset) > 0:
        min = inf
        current = -1
        for i in openset:
            if f_score[i - 1] < min:
                min = f_score[i - 1]
                current = i
        # szukanie wartości minimalnej/najkrótszej drogi do kolejnego wierzchołka
        # według heurystyki przypisanie nowego wierzchołka do bieżącej wartości
        if current == goal:
            return get_path(came_from, current)
        # sprawdzenie czy dotarliśmy do wierzchołka końcowego rekonstrukcja funkcji
        openset.remove(current)
        # usunięcie bierzącego wierzchołka z dostęnych
        for i in range(len(graph[current - 1])):
            if graph[current - 1][i] != inf:
                tentative_gscore = g_score[current - 1] + graph[current - 1][i]
                # alternatywny koszt dojścia do wierzchołka względem obecnego
                if tentative_gscore < g_score[i]:
                    came_from[i + 1] = current
                    g_score[i] = tentative_gscore
                    f_score[i] = tentative_gscore + heuristic[i]
                    # jeżeli alternatywa jest bardziej optymalna przypisujemy nowe wartości
                    if not i + 1 in openset:
                        openset.append(i + 1)
    return None


Pkt_x = [1, 2, 4, 8, 10, 15, 1, 10, 10,8]
pkt_y = [8, 3, 20, 11, 12, 15, 12, 8, 20,9]


def w(i, j):
    return sqrt((Pkt_x[i - 1] - Pkt_x[j - 1]) ** 2 + (pkt_y[i - 1] - pkt_y[j - 1]) ** 2)


Graph = [[inf, w(1, 2), w(1, 3), inf, inf, inf, inf, inf, inf, inf],
         [w(1, 2), inf, inf, inf, w(2, 5), inf, inf, inf, inf, inf],
         [w(1, 3), inf, inf, w(3, 4), w(3, 5), w(3, 6), inf, inf, inf, inf],
         [inf, inf, w(3, 4), inf, w(4, 5), inf, inf, inf, inf, inf],
         [inf, w(2, 5), w(3, 5), w(4, 5), inf, inf, inf, inf, inf, inf],
         [inf, inf, w(3, 6), inf, inf, inf, inf, w(6, 8), w(6, 9), inf],
         [inf, inf, inf, inf, inf, inf, inf, w(7, 8), w(7, 9), w(7, 10)],
         [inf, inf, inf, inf, inf, w(6, 8), w(7, 8), inf, inf, inf],
         [inf, inf, inf, inf, inf, w(6, 9), w(7, 9), inf, inf, inf],
         [inf, inf, inf, inf, inf, inf, w(7, 10), inf, inf, inf]]

end = 7
h = [w(i + 1, end) for i in range(len(Graph))]

print(astar(Graph, h, 1, end))
