from math import inf

from matplotlib import pyplot as plt
from matplotlib.patches import Patch

Graph = [[inf, 4, 6, 8, inf, inf, 17, inf, inf, inf],
         [inf, inf, inf, inf, 5, 6, inf, inf, inf, inf],
         [inf, 5, inf, 6, inf, 3, 7, inf, inf, inf],
         [inf, inf, inf, inf, inf, inf, 4, inf, inf, inf],
         [inf, inf, inf, inf, inf, inf, inf, 6, 4, inf],
         [inf, inf, inf, inf, 2, inf, inf, 7, 10, inf],
         [inf, inf, inf, inf, inf, 5, inf, 10, inf, 21],
         [inf, inf, inf, inf, inf, inf, inf, inf, inf, 5],
         [inf, inf, inf, inf, inf, inf, inf, inf, inf, 4],
         [inf, inf, inf, inf, inf, inf, inf, inf, inf, inf]]


# czasy wykonywania poszczególnych zadań

class Vertex:
    def __init__(self, index, early_term=0, late_term=0):
        self.early_ = early_term
        self.late_ = late_term
        self.index_ = index
        self.In_neighbors_ = []
        self.Out_neighbors_ = []

    # klasa do przechwywania danych o węźle będą to stany pomiędzy poszczególnymi zadaniami

    def __str__(self):
        return str(self.index_ + 1)


class Edge:
    def __init__(self, Vertex_in: Vertex, Vertex_out: Vertex, time, zapas):
        self.vert_in: Vertex = Vertex_in
        self.vert_out: Vertex = Vertex_out
        self.time = time
        self.zapas = zapas
        self.erl_start = Vertex_in.early_
        self.late_start = Vertex_out.late_ - time
        self.erl_end = Vertex_in.early_ + time
        self.late_end = Vertex_out.late_
# klasa przechowująca dane o zadaniu

    def __str__(self):
        to_string = '    l:' + str(self.vert_in.late_) + '   ' + str(self.time) + ',(' + str(
            self.zapas) + ')       l:' + str(self.vert_out.late_)
        to_string += '\n' + str(self.vert_in.index_ + 1) + '.   ----------->  ' + str(self.vert_out.index_ + 1) + '.\n'
        to_string += '    e:' + str(self.vert_in.early_) + '               e:' + str(self.vert_out.early_) + '\n'
        to_string += 'erl_st:' + str(self.erl_start) + ', l_st:' + str(self.late_start) + ', erl_e:' + str(
            self.erl_end) + ', l_e:' + str(self.late_end)

        return to_string


VertexList_ = [Vertex(i) for i in range(10)]
# utworzeie listy wierzchołków
for i in range(len(VertexList_)):
    for j in range(len(Graph)):
        if Graph[i][j] != inf:
            VertexList_[i].Out_neighbors_.append(VertexList_[j])
            VertexList_[j].In_neighbors_.append(VertexList_[i])
#przypisanie do wierzchołków sąsiadów

def latest_time_approx(graph, vertex_list: list[Vertex]):
    visited = []
    start: Vertex = None
    for i in range(len(vertex_list)):
        if not vertex_list[i].In_neighbors_:
            start = vertex_list[i]
            visited.append(start)
            break
    #znalezienie początkowego wierzchołka takiego do którego nie dochodzą żadne drogi
    while len(visited) < len(vertex_list):
        # najpóźniejszych możliwych czasów odwiedzenia wierzchołka szukamy aż znajdziemy wartości dla każdego
        for i in range(len(vertex_list)):
            all_paths_aprox = True
            time = []
            for j in range(len(vertex_list[i].In_neighbors_)):
                if vertex_list[i].In_neighbors_[j] not in visited:
                    all_paths_aprox = False
                    break
            # spawdzenie czy dla danego wierzchołka zostały wyliczone wszystkie wartości czasu dotarcia od sąsiadów
            if all_paths_aprox:
                for j in range(len(vertex_list[i].In_neighbors_)):
                    time.append(
                        vertex_list[i].In_neighbors_[j].early_ + graph[vertex_list[i].In_neighbors_[j].index_][i])
                # dodanie czasów dotarcia do wierzchołka z poszczególnych sąsiadów
                if vertex_list[i] not in visited:
                    visited.append(vertex_list[i])
                # dodanie wierzchołka do odwiedzonych
                if len(time) == 0:
                    vertex_list[i].early_ = 0
                else:
                    vertex_list[i].early_ = max(time)
                # znalezienie najdłuższego czasu


def erliest_time_approx(graph, vertex_list: list[Vertex]):
    visited = []
    start: Vertex = None
    start_idx = None
    for i in range(len(vertex_list)):
        if not vertex_list[i].In_neighbors_:
            start = vertex_list[i]
            start_idx = i
            visited.append(start)
            break
    while len(visited) < len(vertex_list):
        for i in range(len(vertex_list)):
            all_paths_aprox = True
            time = []
            for j in range(len(vertex_list[i].Out_neighbors_)):
                if vertex_list[i].Out_neighbors_[j] not in visited:
                    all_paths_aprox = False
                    break
            if all_paths_aprox:
                for j in range(len(vertex_list[i].Out_neighbors_)):
                    time.append(
                        vertex_list[i].Out_neighbors_[j].late_ - graph[i][vertex_list[i].Out_neighbors_[j].index_])
                if vertex_list[i] not in visited:
                    visited.append(vertex_list[i])
                if len(time) == 0:
                    vertex_list[i].late_ = vertex_list[i].early_
                else:
                    vertex_list[i].late_ = min(time)
    vertex_list[start_idx].late_ = 0
    # analogicznie jak powyżej tylko szukane jest minimum


def critical_path(graph, vertex_list: list[Vertex]):
    path = []
    start_idx = None
    stop_idx = None
    for i in range(len(vertex_list)):
        if not vertex_list[i].In_neighbors_:
            start_idx = i
        if not vertex_list[i].Out_neighbors_:
            stop_idx = i
    # szukanie początku i końca grafu
    next_vertex_idx = start_idx
    next_vertex = vertex_list[next_vertex_idx]
    path.append(start_idx + 1)
    # przypisanie pierwszego wierzchołka do ścieżki
    while next_vertex_idx != stop_idx:
        for vtx in next_vertex.Out_neighbors_:
            if vtx.late_ == vtx.early_:
                next_vertex_idx = vtx.index_
                next_vertex = vertex_list[next_vertex_idx]
                break
        path.append(next_vertex_idx + 1)
    critical_length = 0
    # znalezienie kolejnego elementu ścieżki krytycznej
    # oba czasy najwcześniejszy i najpóźniejszy są takie same
    for i in range(len(path) - 1):
        critical_length += graph[path[i] - 1][path[i + 1] - 1]
    # zwiększenie długości ścieżki krytycznej
    return path, critical_length


def zapas(graph, vertexlist: list[Vertex]):
    zapas_mat = [inf for i in range(len(graph))]
    for i in range(len(graph)):
        zapas_mat[i] = [inf for i in range(len(graph))]
    # utworzenie macierzy zapełnionej wartościami inf
    for i in range(len(graph)):
        for j in range(len(graph)):
            if graph[i][j] != inf:
                zapas_mat[i][j] = vertexlist[j].late_ - vertexlist[i].late_ - graph[i][j]
    # wyznaczenie zapasu dla wszystkich istniejących krawędzi
    return zapas_mat


def gant(e):
    new_e = []
    for i in range(len(e)):
        new_e.append(e[-1-i])
    e = new_e
    strlist = ["(" + str(i.vert_in) + "," + str(i.vert_out) + ")" for i in e]
    beg1 = [i.erl_start for i in e]
    dl1 = [i.late_end - i.erl_start for i in e]
    beg2 = [i.erl_start for i in e]
    dl2 = [i.late_start - i.erl_start for i in e]
    beg3 = [i.erl_end for i in e]
    dl3 = [i.late_end - i.erl_end for i in e]
    beg4 = [i.late_end for i in e]
    # dl4 = [5 if (i.late_end + i.zapas) > 38 else i.zapas for i in e]
    dl4 = [i.zapas for i in e]
    fig, ax = plt.subplots(1, figsize=(16, 6))
    ax.barh(strlist, dl4, left=beg4,alpha=1,color='g',height=.8)
    ax.barh(strlist, dl1, left=beg1, alpha=1, color="b", height=.8)
    ax.barh(strlist, dl2, left=beg2, alpha=1, color="y", height=0.4, align='edge')
    ax.barh(strlist, dl3, left=beg3, alpha=1, color="r", height=0.4)
    c_dict = {'Zakres rozpoczęcia zadania': 'y', 'Zakres zakończenia zadania': 'r', 'Czas w którym zadanie powinno zostać wykonane': 'b','Zapas' :'g'}
    legend_elements = [Patch(facecolor=c_dict[i], label=i) for i in c_dict]
    plt.legend(handles=legend_elements)
    plt.grid(which='both')
    plt.show()
    # wyrysowanie wykresu Gantta

latest_time_approx(Graph, VertexList_)
erliest_time_approx(Graph, VertexList_)
for i in range(len(VertexList_)):
    print(VertexList_[i], ' e:', VertexList_[i].late_, ' l:', VertexList_[i].early_)
print(critical_path(Graph, VertexList_))

print(Graph)
Zapas = zapas(Graph, VertexList_)
print(Zapas)
e = []
for i in range(len(Graph)):
    for j in range(len(Graph)):
        if Graph[i][j] != inf:
            e.append(Edge(VertexList_[i], VertexList_[j], Graph[i][j], Zapas[i][j]))

for i in e:
    print('----------------------------------------------------------\n')
    print(i)
    print('\n----------------------------------------------------------\n')
gant(e)