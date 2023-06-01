import math

import polska


class Vertex:
    def __init__(self, key, x=None, y=None):
        self.key_ = key
        self.x = x
        self.y = y

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

    def __eq__(self, other):
        if (self.Vertex_in_ == other.Vertex_in_) and (self.Vertex_out_ == other.Vertex_out_):
            return True
        else:
            return False

    def __str__(self):
        return str(self.Vertex_out_) + ' -> ' + str(self.Vertex_in_) + ' (' + "{:5.1f}".format(self.length_) + ')'


class NeighborMarix:

    def __init__(self):
        self.VertexList = []
        self.EdgesList = []
        self.Matrix = [[]]
        self.VertexDict = {}

    def __str__(self):
        str_mat = ''
        for i in range(len(self.Matrix)):
            row = '['
            for j in range(len(self.Matrix)):
                if self.Matrix[i][j] is None:
                    row += str(0) + '              '
                else:
                    row += str(self.Matrix[i][j]) + ' '
            str_mat += row + ']' '\n'

        return str_mat

    def InsertVertex(self, vertex):
        self.VertexDict[vertex] = self.order()
        if self.order() != 0:
            self.Matrix.append([None for i in range(self.order())])
        for i in range(len(self.Matrix)):
            self.Matrix[i].append(None)
        self.VertexList.append(vertex)

    def InsertEdges(self, vertex1, vertex2, edge):
        self.Matrix[self.getVertexIdx(vertex1)][self.getVertexIdx(vertex2)] = Edge(vertex1, vertex2, edge)
        self.EdgesList.append(Edge(vertex1, vertex2, edge))

    def deleteVertex(self, vertex):
        v_id = self.getVertexIdx(vertex)
        vertex_ = []
        for i in range(len(self.Matrix)):
            if self.Matrix[i][v_id] is not None:
                vertex_.append(Edge(self.getVertex(i), vertex, None))
                vertex_.append(Edge(vertex, self.getVertex(i), None))
            del self.Matrix[i][v_id]
        del self.Matrix[v_id]
        del self.VertexList[v_id]
        del self.VertexDict[vertex]
        for i in self.VertexDict.keys():
            if self.VertexDict[i] > v_id:
                self.VertexDict[i] -= 1
        d = 0
        for i in range(len(self.EdgesList)):
            if self.EdgesList[i - d] in vertex_:
                del self.EdgesList[i - d]
                d += 1

    def deleteEdge(self, vertex1, vertex2):
        self.Matrix[self.getVertexIdx(vertex1)][self.getVertexIdx(vertex2)] = None
        del_e = Edge(vertex1, vertex2, 0)
        for i in range(len(self.EdgesList)):
            if self.EdgesList[i] == del_e:
                del self.EdgesList[i]
                break

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
        return len(self.EdgesList)

    def order(self):
        return len(self.VertexList)

    def edges(self):
        lst = []
        for i in range(self.size()):
            E: Edge = self.EdgesList[i]
            E_tuple = E.Vertex_out_, E.Vertex_in_
            lst.append(E_tuple)
        return lst


class NeighborList:
    def __init__(self):
        self.EdgesList = []
        self.VertexList = []
        self.Dict_ = {}
        self.VertexDict = {}

    def __str__(self):
        str_mat = '{\n'
        for i in self.Dict_.keys():
            str_mat += '[' + str(i) + ': '
            for j in range(len(self.Dict_[i])):
                str_mat += str(self.Dict_[i][j])
                if j != len(self.Dict_[i]) - 1:
                    str_mat += ',  '
            str_mat += ']\n'
        return str_mat + '}'

    def InsertVertex(self, vertex):
        self.VertexDict[vertex] = self.order()
        self.Dict_[vertex] = []
        self.VertexList.append(vertex)

    def InsertEdges(self, vertex1, vertex2, edge):
        self.Dict_[vertex1].append(Edge(vertex1, vertex2, edge))
        self.EdgesList.append(Edge(vertex1, vertex2, edge))

    def deleteVertex(self, vertex):
        v_id = self.getVertexIdx(vertex)
        edges_lst = []
        for i in range(len(self.EdgesList)):
            if self.EdgesList[i].Vertex_in_ == vertex:
                edges_lst.append(self.EdgesList[i].Vertex_out_)
            if self.EdgesList[i].Vertex_out_ == vertex:
                edges_lst.append(self.EdgesList[i].Vertex_in_)
        for vertex_ in edges_lst:
            self.deleteEdge(vertex, vertex_)
            self.deleteEdge(vertex_, vertex)
        del self.Dict_[vertex]
        del self.VertexList[self.getVertexIdx(vertex)]
        del self.VertexDict[vertex]
        for i in self.VertexDict.keys():
            if self.VertexDict[i] > v_id:
                self.VertexDict[i] -= 1

    def deleteEdge(self, vertex1, vertex2):
        edge = Edge(vertex1, vertex2, None)
        for i in self.Dict_.keys():
            for j in range(len(self.Dict_[i])):
                if self.Dict_[i][j] == edge:
                    del self.Dict_[i][j]
                    break
        for i in range(len(self.EdgesList)):
            if self.EdgesList[i] == edge:
                del self.EdgesList[i]
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
        return len(self.EdgesList)

    def order(self):
        return len(self.VertexList)

    def edges(self):
        lst = []
        for i in range(self.size()):
            E: Edge = self.EdgesList[i]
            E_tuple = E.Vertex_out_, E.Vertex_in_
            lst.append(E_tuple)
        return lst


# Testy grafu

Nei_lst = NeighborList()
Nei_mat = NeighborMarix()
vertexlist = []
for i in range(len(polska.polska)):
    Nei_mat.InsertVertex(Vertex(polska.polska[i][2],polska.polska[i][0],polska.polska[i][1]))
    Nei_lst.InsertVertex(Vertex(polska.polska[i][2],polska.polska[i][0],polska.polska[i][1]))

for i in range(len(polska.graf)):
    distance = math.sqrt((polska.slownik[polska.graf[i][0]][0] - polska.slownik[polska.graf[i][1]][0]) ** 2 + (
                polska.slownik[polska.graf[i][0]][1] - polska.slownik[polska.graf[i][1]][1]) ** 2)
    Nei_mat.InsertEdges(Vertex(polska.graf[i][0]), Vertex(polska.graf[i][1]), distance)
    Nei_lst.InsertEdges(Vertex(polska.graf[i][0]), Vertex(polska.graf[i][1]), distance)

Nei_mat.deleteEdge(Vertex('W'), Vertex('E'))
Nei_mat.deleteEdge(Vertex('E'), Vertex('W'))
Nei_mat.deleteVertex(Vertex('K'))

print(Nei_mat, '\n\n')
mat_edges = Nei_mat.edges()

Nei_lst.deleteEdge(Vertex('W'), Vertex('E'))
Nei_lst.deleteEdge(Vertex('E'), Vertex('W'))
Nei_lst.deleteVertex(Vertex('K'))

print(Nei_lst, '\n\n')
lst_edges = Nei_lst.edges()

polska.draw_map(lst_edges)
# polska.draw_map(mat_edges)
