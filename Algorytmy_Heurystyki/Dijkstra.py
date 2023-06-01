from typing import Dict, List
import math

Graf_matrix = [[math.inf, 40, 52, 58],
               [40, math.inf, 5, 2],
               [52, 5, math.inf, 4],
               [58, 2, 4, math.inf]]

Graf_Dict = {1: [2, 3, 4],
             2: [1, 3, 4],
             3: [1, 2, 4],
             4: [1, 2, 3]
             }


def DPA(G: Dict, s: int, a):
    sum = 0
    path = []
    # początkowe wartości zwracanych zmiennych
    alfa = [0 for i in range(len(G))]
    # utworzenie listy odwiedzonych wierzchołków zapełnionej tymczasowo zerami
    beta = [math.inf for i in range(len(G))]
    # stworzenie listy zawierającej wagi przejść między wierzchołkami tymczasowo zapełnionej
    # wartościami inf
    Q = [i + 1 for i in range(len(G))]  # uworzenie listy nieodwiedzonych wierzchołków
    beta[s - 1] = 0
    Q.remove(s)
    u_prim = s
    # ustawienie wartości dla wierzchołka startowego, usunięcie go z listy nieodwiedzonych wierzchołków,
    # zmiana odległości na 0 od teraz wierzchołek startowy służy jako wartość poprzednika u_prim
    while len(Q) > 0:
    #pętlę wykonujemy aż odwiedzone zostaną wszystkie wierzchołki
        for u in Q:
            for j in G[u_prim]:
                if a[j - 1][u_prim - 1] < beta[j - 1]:
    # szukamy najkrótszej drogi do kolejnego wierzchołka
                    alfa[j - 1] = u_prim
                    beta[j - 1] = a[j - 1][u_prim - 1]
    # dla danego wierzchołka w listę beta wpisujemy wagę potrzebną do jego osiągnięcia, w liście alfa dopisujemy
    # poprzedni wierzchołek
        min = math.inf
        for u in Q:
            if beta[u - 1] < min:
                min = beta[u - 1]
                u_prim = u

        Q.remove(u_prim)
    # szukamy najkrótszej drogi do kolejnego wierzchołka ustawiamy wartość poprzednika na ten właśnie wierzchołek
    # usuwamy go z listy nieodwiedzonych
        path.append((alfa[u_prim - 1], u_prim))
        sum += a[alfa[u_prim - 1] - 1][u_prim - 1]
    #dodajemy krawędź oraz jej wagę do końcowego wyniku
    return path, sum


P, S = DPA(Graf_Dict, 1, Graf_matrix)
print('\n path', P, '\n sum', S)
