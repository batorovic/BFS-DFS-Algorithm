class Graph:
    def __init__(self):
        self.ulasmaIsleme = {}
        self.counter = 0
        self.visitedNodes = []
        self.nodes = []
        self.adjList = {}

    def grafiGoster(self):
        for node in self.nodes:
            print(node, ":", self.adjList[node])

    def addEdge(self, kose, kenar):
        self.adjList[kose].append(kenar)

    def convertToAdjacenyList(self):
        f = open("Komsuluk Matrisi.txt", "r")

        matrisSatiri = 0
        matrisSutun = 0

        # dosyadan okuma islemi
        for dosyaSatiri in f.read().splitlines():
            matrisSutun = 0

            self.adjList[matrisSatiri] = []
            self.nodes.append(matrisSatiri)

            # komsuluk matrisinden komsuluk listesi olusturdum.
            for x in dosyaSatiri.split(' '):
                if x == "1":
                    self.addEdge(matrisSatiri, matrisSutun)
                matrisSutun += 1
            matrisSatiri += 1
        f.close()

    def girisCikisSayilari(self, aranan):
        girisSayac = 0
        cikisSayac = 0

        cikisSayac += len(self.adjList[aranan])

        for key, item in self.adjList.items():

            # cevirimli kenar mi
            if aranan in item and aranan == key:
                girisSayac += 2
                # Cikis sayaci +1 yapmamin sebebi 41.satirda zaten koseden cikis yapanlarin sayisini almistim. Cevirimli kenar oldugu icin +1 yapmam yeterli oldu.
                cikisSayac += 1
            elif aranan in item:
                girisSayac += 1

        print(aranan, "dugumunun:", "\nGiris Derecesi:",
              girisSayac, "\nCikis Derecesi:", cikisSayac)

    def kenarSayilari(self):

        kenarSayisi = 0

        # grafta birbirne bagli olan koselerin kenar sayisini buldum.
        for value in self.adjList:
            kenarSayisi += len(self.adjList[value])

        print("\nKenar Sayisi :", kenarSayisi)

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

        self.visitedNodes.append(v)  # baslangic node'u
        print(v, end=" ")
        self.counter += 1
        self.ulasmaIsleme[v] = {
            "Ulaşma": self.counter, "İsleme": self.counter}

        # recursive bir sekilde grafta dolasma
        for komsu in self.adjList[v]:
            if komsu not in self.visitedNodes:
                self.DFS_Arama(komsu)
        self.counter += 1

        self.ulasmaIsleme[v]["İsleme"] = self.counter

    # bazi graflarda kendi halinde gruplu nodelar oluyor bu gruptan sadece cikis node lari mevcut oluyor bunun icin butun nodelar visit edildi mi kontrol etmem gerekiyor visited node larda yoksa o kısım dedigim grup oluyor orayı dfs ile ariyorum.
    def dfsCheckAllNodes(self):
        for komsu in self.adjList:
            if komsu not in self.visitedNodes:
                self.DFS_Arama(komsu)


def main():
    graph = Graph()
    graph.convertToAdjacenyList()  # komsuluk listesine ceviriyorum.

    while True:
        print("""
              1) Grafin komsuluk listesini goster.
              2) Giris cikis sayilari
              3) Graftaki toplam kenar sayisi
              4) BFS arama
              5) DFS arama
              e) Cikis yap.
              """)

        secim = input("Secim yapiniz : ")

        if secim == "1":
            graph.grafiGoster()

        elif secim == "2":
            print("\nMevcut dugumler : ", graph.nodes)
            node = input(
                "Hangi dugumun giris - cikis derecesini ogrenmek istiyorsunuz ? ")

            print()
            graph.girisCikisSayilari(int(node))
        elif secim == "3":
            graph.kenarSayilari()

        elif secim == "4":
            print("\nMevcut dugumler : ", graph.nodes)
            node = input(
                "Hangi dugumden aramaya baslamak istiyorsunuz : ")
            print()
            graph.BFS(int(node))

        elif secim == "5":
            print("\nMevcut dugumler : ", graph.nodes)
            node = input(
                "Hangi dugumden aramaya baslamak istiyorsunuz : ")
            print("\nDFS arama sonucu dolasma sirasi : ", end=" ")
            graph.DFS_Arama(int(node))

            graph.dfsCheckAllNodes()

            print("\n")

            # Ulasma isleme sayilarini ekrana yazdirma.
            for key, value in graph.ulasmaIsleme.items():
                print(key, ":", value)

        elif secim.lower() == "e":
            exit()
        else:
            print("\nGecerli secim yapiniz !")


if __name__ == "__main__":
    main()
