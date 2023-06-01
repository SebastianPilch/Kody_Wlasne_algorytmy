import math

inf = math.inf


class Vertex:
    def __init__(self, key, brightness=None, ):
        self.key_ = key
        self.brightness = brightness

    def __eq__(self, other):
        return True if self.key_ == other.key_ else False

    def __hash__(self):
        return hash(self.key_)

    def __str__(self):
        return self.key_


class Edge:
    def __init__(self, Vertex1, Vertex2, edge=1):
        self.Vertex_out_ = Vertex1
        self.Vertex_in_ = Vertex2
        self.length_ = edge

    def __eIntree__(self, other):
        if (self.Vertex_in_ == other.Vertex_in_) and (self.Vertex_out_ == other.Vertex_out_):
            return True
        else:
            return False

    def __str__(self):
        # return str(self.Vertex_out_) + ' -> ' + str(self.Vertex_in_) + ' (' + "{:5^.0f}".format(self.length_) + ')'
        return str(self.Vertex_out_) + ' -> ' + str(self.Vertex_in_)

class NeighborMarix:

    def __init__(self):
        self.VertexList = []
        self.Matrix = [[]]
        self.VertexDict = {}

    def __str__(self):
        str_mat = '------GRAPH------,' + str(self.order()) + '\n'
        for i in range(len(self.Matrix)):
            row = '['
            for j in range(len(self.Matrix)):
                if self.Matrix[i][j] is None:
                    row += str(0) + '              '
                else:
                    row += str(self.Matrix[i][j]) + ' '
            str_mat += row + ']' '\n'
        str_mat += '-------------------'

        return str_mat

    def InsertVertex(self, vertex):
        self.VertexDict[vertex] = self.order()
        if self.order() != 0:
            self.Matrix.append([None for i in range(self.order())])
        for i in range(len(self.Matrix)):
            self.Matrix[i].append(None)
        self.VertexList.append(vertex)

    def InsertEdges(self, vertex1, vertex2, edge):
        idx_1 = self.getVertexIdx(vertex1)
        idx_2 = self.getVertexIdx(vertex2)
        self.Matrix[idx_1][idx_2] = Edge(self.getVertex(idx_1), self.getVertex(idx_2), edge)

    def deleteVertex(self, vertex):
        v_id = self.getVertexIdx(vertex)
        for i in range(len(self.Matrix)):
            if self.Matrix[i][v_id] is not None:
                self.Matrix[i][v_id] = None
        del self.Matrix[v_id]
        del self.VertexList[v_id]
        del self.VertexDict[vertex]
        for i in self.VertexDict.keys():
            if self.VertexDict[i] > v_id:
                self.VertexDict[i] -= 1

    def deleteEdge(self, vertex1, vertex2):
        if self.Matrix[self.getVertexIdx(vertex1)][self.getVertexIdx(vertex2)] is not None:
            self.Matrix[self.getVertexIdx(vertex1)][self.getVertexIdx(vertex2)] = None

    def getVertexIdx(self, vertex):
        return self.VertexDict[vertex]

    def getVertex(self, vertex_id):
        return self.VertexList[vertex_id]

    def neighbours(self, vertex_id):
        neighbours = []
        for i in range(self.order() - 1):
            if self.Matrix[vertex_id][i] is not None and i not in neighbours:
                neighbours.append(self.getVertex(i))
            if self.Matrix[i][vertex_id] is not None and i not in neighbours:
                neighbours.append(self.getVertex(i))
        return neighbours

    def size(self):
        return len(self.edges())

    def order(self):
        return len(self.VertexList)

    def edges(self):
        lst = []
        for i in range(self.order()):
            for j in range(self.order()):
                if self.Matrix[i][j] is not None:
                    t = self.Matrix[i][j].Vertex_out_.key_, self.Matrix[i][j].Vertex_in_.key_
                    lst.append(t)

        return lst


class NeighborList:
    def __init__(self):
        self.VertexList = []
        self.Dict_ = {}
        self.VertexDict = {}

    def __str__(self):
        str_mat = '------GRAPH------,' + str(self.order()) + '\n'
        for i in self.Dict_.keys():
            str_mat += '[' + str(i) + ': '
            for j in range(len(self.Dict_[i])):
                str_mat += str(self.Dict_[i][j])
                if j != len(self.Dict_[i]) - 1:
                    str_mat += ',  '
            str_mat += ']\n'
        return str_mat + '-------------------'

    def InsertVertex(self, vertex):
        self.VertexDict[vertex] = self.order()
        self.Dict_[vertex] = []
        self.VertexList.append(vertex)

    def InsertEdges(self, vertex1, vertex2, edge):
        idx_1 = self.getVertexIdx(vertex1)
        idx_2 = self.getVertexIdx(vertex2)
        self.Dict_[vertex1].append(Edge(self.getVertex(idx_1), self.getVertex(idx_2), edge))

    def deleteVertex(self, vertex):
        v_id = self.getVertexIdx(vertex)
        del self.Dict_[vertex]
        self.VertexList.remove(vertex)
        del self.VertexDict[vertex]
        for i in self.VertexDict.keys():
            if self.VertexDict[i] > v_id:
                self.VertexDict[i] -= 1
            for j in range(len(self.Dict_[i])):
                if self.Dict_[i][j].Vertex_in_ == vertex:
                    del self.Dict_[i][j]
                    break

    def deleteEdge(self, vertex1, vertex2):
        edge = Edge(vertex1, vertex2, None)
        for i in range(len(self.Dict_[vertex1])):
            if self.Dict_[vertex1][i] == edge:
                del self.Dict_[vertex1][i]
                break

    def getVertexIdx(self, vertex):
        return self.VertexDict[vertex]

    def getVertex(self, vertex_id):
        return self.VertexList[vertex_id]

    def neighbours(self, vertex_id):
        neighbours = []
        vertex = self.getVertex(vertex_id)
        for i in self.Dict_.keys():
            for edge in self.Dict_[i]:
                if edge.Vertex_in_ == vertex and edge.Vertex_out_ not in neighbours:
                    neighbours.append(edge.Vertex_out_)
                if edge.Vertex_out_ == vertex and edge.Vertex_in_ not in neighbours:
                    neighbours.append(edge.Vertex_in_)
        return neighbours

    def size(self):
        return len(self.edges())

    def order(self):
        return len(self.VertexList)

    def edges(self):
        lst = []
        for i in self.Dict_.keys():
            for j in range(len(self.Dict_[i])):
                E: Edge = self.Dict_[i][j]
                E_tuple = E.Vertex_out_.key_, E.Vertex_in_.key_
                lst.append(E_tuple)
        return lst


def Prims_Algorithm(G: NeighborList, s: Vertex):
    sum_ = 0
    path = []
    parent = [0 for i in range(len(G.VertexList))]
    distance = [inf for i in range(len(G.VertexList))]
    Intree = [G.VertexList[i] for i in range(len(G.VertexList))]
    distance[G.getVertexIdx(s)] = 0
    Intree.remove(s)
    u_prim = s
    while len(Intree) > 0:
        for u in Intree:
            for edge in G.Dict_[u_prim]:
                if edge.length_ < distance[G.getVertexIdx(edge.Vertex_in_)]:
                    parent[G.getVertexIdx(edge.Vertex_in_)] = u_prim
                    distance[G.getVertexIdx(edge.Vertex_in_)] = edge.length_
        min_ = inf
        for u in Intree:
            if distance[G.getVertexIdx(u)] < min_:
                min_ = distance[G.getVertexIdx(u)]
                u_prim = u
        Intree.remove(u_prim)
        for u in G.Dict_[parent[G.getVertexIdx(u_prim)]]:
            if u.Vertex_in_ == u_prim:
                sum_ += u.length_
                path.append(Edge(parent[G.getVertexIdx(u_prim)], u_prim, u.length_))
    return path, sum_

Nei_lst = NeighborList()
#Nei_mat = NeighborMarix()

graf = [('A', 'B', 4), ('A', 'C', 1), ('A', 'D', 4),
        ('B', 'E', 9), ('B', 'F', 9), ('B', 'G', 7), ('B', 'C', 5),
        ('C', 'G', 9), ('C', 'D', 3),
        ('D', 'G', 10), ('D', 'J', 18),
        ('E', 'I', 6), ('E', 'H', 4), ('E', 'F', 2),
        ('F', 'H', 2), ('F', 'G', 8),
        ('G', 'H', 9), ('G', 'J', 8),
        ('H', 'I', 3), ('H', 'J', 9),
        ('I', 'J', 9)]
ver_keys = []
for edges in graf:
    if edges[0] not in ver_keys:
        ver_keys.append(edges[0])
    if edges[1] not in ver_keys:
        ver_keys.append(edges[1])
for ver in ver_keys:
    Nei_lst.InsertVertex(Vertex(ver))
for edges in graf:
    Nei_lst.InsertEdges(Vertex(edges[0]), Vertex(edges[1]), edges[2])
    Nei_lst.InsertEdges(Vertex(edges[1]), Vertex(edges[0]), edges[2])
print(Nei_lst)

mst, sum_ = Prims_Algorithm(Nei_lst, Vertex('A'))
print(sum_)
Mst_graph = NeighborList()
for ver in ver_keys:
    Mst_graph.InsertVertex(Vertex(ver))
for edges in mst:
    Mst_graph.InsertEdges(edges.Vertex_in_, edges.Vertex_out_, edges.length_)
    Mst_graph.InsertEdges(edges.Vertex_out_, edges.Vertex_in_, edges.length_)
print(Mst_graph)
