from copy import deepcopy
from typing import List, Dict


def dfs(G: Dict[int, List[int]], s: int) -> List[int]:
    queue = [s]
    # tworzę kolejkę do której wrzucam kolejne
    # wierzchołki listy sąsiedztwa zaczynając od startowego s
    visited = [False] * (len(G))
    result = []
    # visited - lista sprawdzająca czy dany wierzchołek był już
    # odwiedzony
    # result  - do tej listy będą dodawane wierzchołki
    # w kolejności odwiedzania
    while len(queue) > 0:
        v_id = queue.pop()
        # pętla while wyciągająca z kolejki drogi od wcześniej
        # sprawdzanego wierzchołka
        if not visited[v_id-1]:
            visited[v_id-1] = True
            result += [v_id]
            # sprawdzenie czy wierzchołek był wcześniej odwiedzony jeśli
            # nie zmieniamy jego status w visited na True, czyli
            # odwiedzony i dodajemy do wyniku
            for elem in G[v_id]:
                queue.append(elem)
                # dodanie do kolejki wierzchołków połączonych z tym
                # sprawdzanym w danej iteracji while
    return list(dict.fromkeys(result))


def is_coherent(G: Dict[int, List[int]]) -> bool:
    if len(dfs(G, 1)) == len(G):
        #do sprawdzenia spójności wykorzystuję napisaną
        # wcześniej funkcję dfs sprawdzam czy długość listy
        # odwiedzonych punktów jest rónwna długości listy
        # sąsiedztwa jeżeli tak graf jest spójny
        return True
    else:
        return False


def is_cyclic(G: Dict[int, List[int]]) -> bool:
    visited = [False] * (len(G))
    # visited - lista sprawdzająca czy dany wierzchołek
    # był już odwiedzony
    while False in visited:
        # wykonujemy program aż do momentu odwiedzenia
        # wszystkich wierzchołków
        G = deepcopy(G)
        # w celu sprawdzenia cylkiczności usuwamy ścieżki co wymaga
        # wprowadzenia kopii listy sąsiedztwa aby nie zmodyfikować
        # oryginalnego grafu
        for i in range(len(G)):
            if visited[i] is False:
                queue = [i+1]
                break
        # dodajemy do kolejki pierwszy nieodwiedzony wierzchołek
        while len(queue) > 0:
            v_id = queue.pop()
            if not visited[v_id-1]:
                visited[v_id-1] = True
                # sprawdzamy czy pierwszy wierzchołek z kolejki
                # został odwiedzony jeżeli nie zmieniamy jego
                # status w visited
                for elem in G[v_id].copy():
                    queue.append(elem)
                    G[elem].remove(v_id)
                    G[v_id].remove(elem)
                    # usuwamy ścieżkę prowadzącą z wcześniejszego
                    # wierzchołka do sprawdzanego obecne
            else:
                return True
            # jeżeli pomimo usunięcia jednej ścieżki wrócimy do wierzchołka
            # oznacza to  że graf jest cykliczny
    return False


