class Graph:
    def __init__(self):
        self.girisCikislar = {}
        self.counter = 0
        self.visitedNodes = []
        self.deneme = {'A': ["F", "G"],
                       "B": ["A", "I"],
                       "C": ["A", "D"],
                       "D": ["C", "F"],
                       "E": ["C", "D", "G"],
                       "F": ["E"],
                       "G": [],
                       "H": ["B"],
                       "I": ["H"]}
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
            elif aranan in item:  # normal ifdi
                girisSayac += 1

        print("Cikis Derecesi: ", cikisSayac, " Giris Derecesi: ", girisSayac)

    def kenarSayilari(self):
        matrix = []
        kenarSayisi = 0
        sutun = 0

        with open("Komsuluk Matrisi.txt") as inputFile:
            for line in inputFile:
                matrix.append([int(x) for x in line.split(' ')])

        # x = 0
        # y = 0

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

    def BFS(self, baslangicNode):

        que = []
        visitedNodes = []

        que.append(baslangicNode)
        visitedNodes.append(baslangicNode)

        while que != []:  # kuyruk bos olmayıncaya kadar
            # dict'e key veriyorum. Gonderdigim key node oluyor. O node on komsularina bakiyorum.
            for x in self.adjList[que[0]]:
                if x not in visitedNodes:
                    visitedNodes.append(x)
                    que.append(x)
            que.pop(0)
        print(visitedNodes)

    def DFS_Arama(self, v):
        # nested_dict = {1: {'Giriş Derecesi': 1, 'Cikis Derecesi': 2}}
        # alo[0] = {"Giris": 1, "Cikis": 2}

        self.visitedNodes.append(v)  # baslangic node'u
        print(v, end=" ")
        # print(v, " ulasma : ", self.counter + 1)
        self.counter += 1
        self.girisCikislar[v] = {
            "Ulaşma": self.counter, "İsleme": self.counter}

        for komsu in self.adjList[v]:
            if komsu not in self.visitedNodes:
                self.DFS_Arama(komsu)
            # print("xxx")
        self.counter += 1
        # print(v, " Cikis : ", self.counter)

        self.girisCikislar[v]["İsleme"] = self.counter

    def dfsCheckAllNodes(self):
        for komsu in self.adjList:
            if komsu not in self.visitedNodes:
                self.DFS_Arama(komsu)


def main():
    graph = Graph()

    graph.convertToAdjacenyList()
    graph.printAdj()
    print("--------")

    graph.girisCikisSayilari(1)  # aranan degeri parametre olarak veriyoruz.

    print("--------")

    graph.kenarSayilari()

    print("--------")

    graph.BFS(0)  # aramaya baslama node u

    print("--------")

    graph.DFS_Arama(0)  # aramaya baslanacak dugum
    # bazi graflarda kendi halinde gruplu nodelar oluyor bu gruptan sadece cikis node lari mevcut oluyor bunun icin butun nodelar visit edildi mi kontrol etmem gerekiyor yoksa visitedlarda o kısım dedigim grup oluyor orayı dfs ile ariyorum.
    graph.dfsCheckAllNodes()

    print("\n--------")

    for key, value in graph.girisCikislar.items():
        print(key, value)

    # nested_dict = {1: {'Giriş Derecesi': 1, 'Cikis Derecesi': 2}}


#     sozluk = {}

#     nested_dict = {'Giriş Dereceleri': {'key_1': 'value_1'},
#                 'Cikis Dereceleri': {'key_2': 'value_2'}}
#    for node in graph.nodes:
#         sozluk[node] = [{"Giris: :", []}]

#     print(sozluk)

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
