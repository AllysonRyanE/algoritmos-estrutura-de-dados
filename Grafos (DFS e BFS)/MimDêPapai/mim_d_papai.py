#BUSCA EM PROFUNDIDADE (DFS)
class Grafo:
    def __init__(self):
        self.grafo = []  # Será uma lista de objetos da classe Node

    def amigos(self, valores):  # Informarei uma lista de tuplas, sendo cada tupla o estabelecimento de dois vértices e também já de suas conexões, sem visar ainda os nós isolados
        for x in valores:  # Irei analisar cada conexão, cada tupla
            node_esq, node_dir = x[0], x[1]  # Duas variavéis cada uma recebendo um valor da tupla
            nodeF, nodeS = None, None  # Preciso dessa estrutura para contornar repetições
            for n in self.grafo:  # A partir do momento que meu grafo tem algum valor em si, irei fazer comparações quando for adicionar o próximo para vê se o que desejo adicionar já não está presente
                if n.num == node_esq:
                    nodeF = n
                elif n.num == node_dir:
                    nodeS = n
            if nodeF == None:  # Observe que ele não será vazio caso tenha sido igual a um elemento encontrado, logo não será adicionado no grafo
                nodeF = Node(node_esq)
                self.grafo.append(nodeF)
            if nodeS == None:
                nodeS = Node(node_dir)
                self.grafo.append(nodeS)
            nodeF.adjacentes.append(nodeS)  # Estabeleço a aresta, a conexão, adicionando cada um a lista de adjacentes do outro, pois se estão em uma mesma tupla, é isso que significa
            nodeS.adjacentes.append(nodeF)  # Isso funcionará ainda que sejam nós que já foram adicionados, pois posso querer apenas estabelecer uma conexão
        return self.grafo

    def busca(self, no):
        indice = None #Essa função serve para retorna o indice de um valor qualquer procurado
        for i in self.grafo:
            if i.num == no:
                indice = self.grafo.index(i)
                break
        if indice is None: #Caso ele não seja encontrado significa na verdade que ele é um nó isolado que ainda assim faz parte do grafo, logo transformo-o em nó e adiciono
            no = Node(no)
            self.grafo.append(no)
        return indice

    def DFS(self, user, marcados):
        pilha = [user] #Minha pilha começa pelo meu nó dado, o primeiro usuário que entra em contato
        while pilha: #Enquanto houver elementos na pilha há ainda percurso
            user = pilha.pop() #Após retirar da pilha, significa que já visualizei, logo adiciono nos marcados
            if user not in marcados:
                marcados.append(user)
                for a in user.adjacentes: #Vejo os vizinhos do que acabei de visualizar e caso não tenha sido visualizados antes, os adiciono na pilha
                    if a not in marcados:
                        pilha.append(a) #O pop é muito relevante, pois além de excluir da pilha eu retorno o valor que precisa informar seus filhos que serão adicionados

    def visitados(self, no):
        marcados = [] #Essa é a lista que vai evitar que seja revisitado algum nó, sem ela o percurso torna-se até ilógico
        indice = self.busca(no) #Busco meu elemento
        if indice != None: #Ele tendo ao menos uma conexão vejo se já visualizei ele em algum momento
            elemento = self.grafo[indice] #Armazeno meu objeto
            if elemento not in marcados: #Caso não tenha ainda sido explorado ai posso começar a busca
                self.DFS(elemento, marcados) #O objeto que é repassado
            return len(marcados)
        else:
            return 1 #Caso não tenha conexão o único usuário alcançado é ele mesmo


class Node:
    def __init__(self, num):
        self.num = num  # Meu valor interno importante para as comparações númericas
        self.adjacentes = []  # Muito semelhante a uma árvore aqui há um encadeamento, porém não apenas do próximo nó, mas sim todos conectados ao vértice pela aresta, por isso necessita-se de uma lista por pode ser n-"amigos"

rede = input().split()
usuarios, arestas = int(rede[0]), int(rede[1])
rede.clear()
while True:
    try:
        conexao = tuple(map(int, input().strip().split()))
        rede.append(conexao)
    except EOFError:
        break
algoritmo = Grafo()
algoritmo.amigos(rede)
for x in range(1, usuarios+1):
  if x!= usuarios:
    print(algoritmo.visitados(x), end = " ")
  else:
    print(str(algoritmo.visitados(x)).strip())
