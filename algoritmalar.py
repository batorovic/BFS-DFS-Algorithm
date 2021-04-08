class Graph:
    def __init__(self):
        self.nodes = []
        self.adjList = {}
        self.kenarSayisi = 0
        self.komsulukMatrix = []
        # for node in self.nodes:
        #     self.adjList[node] = []

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
        karakter = 65
        karakter1 = 65

        matrix = []

        for dosyaSatiri in f.read().splitlines():
            # matrix.append([int(x) for x in satir.split(' ')])
            matrisSutun = 0
            karakter1 = 65

            # self.adjList[chr(karakter)] = []  # satir
            # self.nodes.append(chr(karakter))  # satir

            self.adjList[matrisSatiri] = []  # satir
            self.nodes.append(matrisSatiri)  # satir
            for x in dosyaSatiri.split(' '):

                if x == "1":

                    # self.addEdge(chr(karakter), chr(karakter1))  # satir  sutun
                    self.addEdge(matrisSatiri, matrisSutun)  # satir  sutun

                    # graph.addEdge(matrisSatiri, matrisSutun)
                matrisSutun += 1
                karakter1 += 1
            matrisSatiri += 1
            karakter += 1
        f.close()

    def girisCikisSayilari(self, aranan):

        girisSayac = 0
        cikisSayac = 0

        cikisSayac += len(self.adjList[aranan])

        for key, item in self.adjList.items():

            # cevirimli kenar mi
            if aranan in item and aranan == key:
                girisSayac += 2
                cikisSayac += 1  # cevirimli kenar asagida lende bri tanesini icine aliyor buradad 1 +2 oldu
            if aranan in item:
                girisSayac += 1

        print("Cikis Derecesi: ", cikisSayac, " Giris Derecesi: ", girisSayac)

    def kenarSayilari(self):
        matrix = []
        kenarSayisi = 0
        sutun = 0

        with open("Komsuluk Matrisi.txt") as inputFile:
            for line in inputFile:
                matrix.append([int(x) for x in line.split(' ')])

        x = 0
        y = 0

        grafTuru = "YONLU"
        for x, row in enumerate(matrix):
            for y, column in enumerate(matrix):
                # son satirdan bır onceki satirda zaten son satiri kontrol ettim o yuzden satir sutun birbirine esit olmamalı.
                if matrix[x][y] == 1 and matrix[y][x] == 1 and y != x:
                    grafTuru = "YONSUZ"
            if grafTuru == "YONSUZ":
                break
        print(grafTuru)
        if grafTuru == "YONSUZ":
            for x, line in enumerate(matrix):
                # TXT olarak verilen komsulum matrisi yonsuz graf oldugu icin simetrik matris oluyor. Bunun icin kosegen uzerinde 1 varsa onu da kenar sayisina ekledim.
                if matrix[x][x] == 1:
                    kenarSayisi += 1
                # alt kosegenden kenar sayisini buldum.
                for y in range(sutun):
                    if matrix[x][y] == 1:
                        kenarSayisi += 1
                sutun += 1
            print("Kenar Sayisi : ", kenarSayisi)

        elif grafTuru == "YONLU":

            for x, row in enumerate(matrix):
                for y, column in enumerate(matrix):
                    if matrix[x][y] == 1:
                        kenarSayisi += 1
            print("kenar : ", kenarSayisi)

        inputFile.close()


def main():
    graph = Graph()

    graph.convertToAdjacenyList()
    graph.printAdj()
    print("--------")

    graph.girisCikisSayilari(0)  # aranan degeri parametre olarak veriyoruz.

    print("--------")

    graph.kenarSayilari()

    print("--------")

    # aranan = 3

    # cikisSayac = 0
    # girisSayac = 0

    # for key, item in graph.adjList.items():

    #     # cevirimli kenar mi
    #     if aranan in item and aranan == key:
    #         cikisSayac += 2
    #         girisSayac += 2
    #     elif aranan in item:
    #         cikisSayac += 1
    #     elif aranan == key:
    #         girisSayac += len(item)
    # print(cikisSayac)

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
