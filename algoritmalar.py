class Graph:
    def __init__(self, Nodes):
        self.nodes = Nodes
        self.adjList = {}
        for node in self.nodes:
            self.adjList[node] = []

    def printAdj(self):
        for node in self.nodes:
            print(node, ":", self.adjList[node])

    def addEdge(self, kose, kenar):
        self.adjList[kose].append(kenar)
        # self.adjList[kenar].append(kose)

    def convertToAdjacenyList(self):

        f = open("Komsuluk Matrisi.txt", "r")

        matrisSatiri = 0
        matrisSutun = 0

        for dosyaSatiri in f.read().splitlines():
            # matrix.append([int(x) for x in satir.split(' ')])
            matrisSutun = 0
            for x in dosyaSatiri.split(' '):
                if(x == "1"):

                    self.addEdge(matrisSatiri, matrisSutun)
                    #graph.addEdge(matrisSatiri, matrisSutun)
                matrisSutun += 1
            matrisSatiri += 1
        f.close()


def main():
    # matrisin 5x5 oldugu icin
    nodes = [0, 1, 2, 3, 4]
    graph = Graph(nodes)

    graph.convertToAdjacenyList()
    graph.printAdj()

    # f = open("Komsuluk Matrisi.txt", "r")
    # matrix = []
    # matrisSatiri = 0
    # matrisSutun = 0
    # for dosyaSatiri in f.readlines():
    #     # matrix.append([int(x) for x in satir.split(' ')])
    #     matrisSutun = 0
    #     for x in dosyaSatiri.split(' '):
    #         if(x == "1" or x == "1\n"):

    #             graph.addEdge(matrisSatiri, matrisSutun)
    #         matrisSutun += 1
    #     matrisSatiri += 1

    # for x in range(5):
    #     for y in range(5):
    #         if(matrix[x][y] == 1):
    #             graph.addEdge(x, y)


if __name__ == "__main__":
    main()
