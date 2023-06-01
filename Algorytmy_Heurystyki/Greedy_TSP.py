from math import inf

Graph = [[inf, 5, inf, 10, inf, inf, inf, 13, inf, inf],
         [inf, inf, 4, inf, 15, inf, inf, inf, inf, inf],
         [inf, inf, inf, inf, inf, 18, inf, inf, inf, inf],
         [inf, 3, 8, inf, inf, inf, 10, inf, 21, inf],
         [inf, inf, inf, 11, inf, inf, 14, inf, 20, inf],
         [17, inf, inf, inf, 5, inf, inf, inf, inf, inf],
         [9, inf, inf, inf, inf, inf, inf, 16, inf, inf],
         [23, inf, inf, inf, 12, inf, inf, inf, inf, inf],
         [inf, inf, inf, inf, inf, 6, inf, 9, inf, 10],
         [inf, inf, inf, inf, 13, 18, inf, inf, inf, inf]]

Graph2 = [[inf, 5, 12, 10, 23, 31, 11, 13, 9, 8],
          [14, inf, 4, 13, 15, 8, 23, 11, 5, 8],
          [19, 17, inf, 13, 11, 18, 13, 10, 32, 13],
          [8, 3, 8, 9, inf, 18, 10, 15, 21, 20],
          [10, 12, 18, 11, inf, 9, 14, 19, 20, 13],
          [17, 17, 12, 15, 5, inf, 7, 14, 19, 22],
          [9, 22, 19, 21, 17, 12, inf, 16, 19, 20],
          [23, 10, 12, 14, 12, 16, 17, inf, 22, 13],
          [14, 18, 13, 19, 12, 6, 14, 9, inf, 10],
          [21, 20, 15, 14, 13, 18, 22, 31, 10, inf]]

G1 = [[inf, 2, 4, 4, 2, 5],
      [2, inf, 4, 7, 1, 3],
      [4, 4, inf, 1, 2, 3],
      [4, 7, 1, inf, 2, 6],
      [2, 1, 2, 2, inf, 8],
      [5, 3, 3, 6, 8, inf]]


def is_cycle(path, vertex1, vertex2):
    visited = []
    next = vertex2
    # utworzenie pustej listy odwiedzonych wierzchołków
    # przypisanie początkowego wierzchołka
    for j in range(len(path)):
        if next not in visited:
            # sprawdzenie czy węzeł został już odwiedzony
            # w ścieżce
            for i in range(len(path)):
                if path[j][0] == next:
                    # przeszukanie dotychczasowej ścieżki w celu
                    # znalezienia kolej krawędzi
                    visited.append(next)
                    next = path[i][1]
                    # dodanie nowej wartości do odwiedzonych wierzchołków
                    if next == vertex1:
                        return True
                    # jeżeli dotarliśmy do elementu już występującego w ścieżc
                    # występuje cykl
                    break
    return False


def G_TSP(G):
    edges = []
    visited_in = []
    # lista wierzchołków z których wychodzi ścieżka
    visited_out = []
    # lista wierzchołków do których wchodzi ścieżka
    for i in range(len(G)):
        for j in range(len(G)):
            if G[i][j] != inf:
                edges.append([G[i][j], i + 1, j + 1])
    edges.sort()
    # posortowanie krawędzi niemalejąco
    visited_in.append(edges[0][1])
    visited_out.append(edges[0][2])
    shortest = [[edges[0][1], edges[0][2]]]
    shortest_length = edges[0][0]
    # dodanie do ścieżki i do odwiedzonych punktów pierwszej krawędzi
    del edges[0]
    # usunięcie pierwszego elementu z listy krawędzi
    for i in range(len(edges)):
        road = edges[i]
        if road[1] not in visited_in and road[2] not in visited_out and [road[2], road[1]] not in shortest:
            # jeżeli wierzchołek nowej krawędzi był już odwiedzany przez ścieżkę nie rozważamy go
            # podobnie jeżeli istnieje już ścieżka skierowana w drugą stronę
            if len(G) - 1 > len(shortest):
                if is_cycle(shortest, road[1], road[2]) is False:
                    visited_in.append(road[1])
                    visited_out.append(road[2])
                    shortest.append([road[1], road[2]])
                    shortest_length += road[0]
            # dla ścieżki o krótszej niż rozmiar grafu dodajemy pod warunkiem braku cyklu
            else:
                if len(G) - 1 == len(shortest):
                    visited_in.append(road[1])
                    visited_out.append(road[2])
                    shortest.append([road[1], road[2]])
                    shortest_length += road[0]
            # ostatnia dodana krawędź musi zamykać ścieżkę więc nie sprawdzamy warunku cykliczności

    if len(G) != len(visited_out) or len(G) != len(visited_in):
        raise ValueError
    return shortest, shortest_length
    # Algorytm nie zawsze znajduje odpowiednie rozwiązanie czasami
    # znaleziona ścieżka jest za krótka wtedy zwracamy błąd

def path_sort(path):
    sorted = [path[0]]
    next = path[0][1]
    for j in range(len(path) - 1):
        for i in range(len(path)):
            if path[i][0] == next:
                sorted.append(path[i])
                next = path[i][1]
                break
    return sorted
# funkcja sortująca ścieżkę w sumie nie poyrzebna

print('\nGraf 1:')
try:
    path, length = G_TSP(Graph2)

    path = path_sort(path)
    print('ścieżka:\n', path)
    print('długość ścieżki:\n', length)

except:
    print('Nie znaleziono ścieżki')
print('\n\n Graf 2:')
try:
    path, length = G_TSP(Graph)
    print('ścieżka:\n', path)
    print('długość ścieżki:\n', length)

except:
    print('Nie znaleziono ścieżki')
print('\n\n Graf 3:')
try:
    path, length = G_TSP(G1)
    path = path_sort(path)
    print('ścieżka:\n', path)
    print('długość ścieżki:\n', length)
except:
    print('Nie znaleziono ścieżki')


