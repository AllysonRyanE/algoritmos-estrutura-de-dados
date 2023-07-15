#BUSCA EM LARGURA (BFS)
class Grafo:
    def __init__(self):
        self.grafo = []  # Será uma lista de objetos da classe Node

    def amigos(self, valor, adjacentes):  # Informarei um usuário e uma lista com suas devidas conexões
        check = None # Preciso dessa estrutura para contornar repetições
        for n in self.grafo:  # A partir do momento que meu grafo tem algum valor em si, irei fazer comparações quando for adicionar o próximo para vê se o que desejo adicionar já não está presente
            if n.num == valor:
                check = n
        if check == None:  # Observe que ele não será vazio caso tenha sido igual a um elemento encontrado, logo não será adicionado no grafo
            check = Node(valor)
            self.grafo.append(check)
            for a in adjacentes: #Por fi m percorro todas os nós conectados e transformo-os realmente em nós
                a = Node(a)
                check.adjacentes.append(a) #Além de adiciona-los aos adjacentes do nó informado, estabeleço as conexões

    def busca(self, no): #Aqui eu percorro o grafo para quando for informado um número verificar se há um nó com aquele número e retornar onde está tal
        indice = None
        for i in self.grafo:
            if i.num == no:
                indice = self.grafo.index(i)
                break
        return indice

    def BFS(self, user, renda, rede, free=True):
        global marcados #Usaremos duas globais, uma para sendo a lista de nós já visitados e assim não repetir
        global id_user #Outra para sabermos qual o usuário. Faremos com globais para não perdermos os dados nas recursões
        add = 0
        user = self.grafo[user] #O user vai receber o objeto
        fila = []
        fila.append(user) #A fila começa com o próprio usuário, apesar de não entrar na lista de marcados
        if user.num!=id_user and user.num not in marcados:  #Se o objeto não for o usuário e ainda não estiver no marcado será adicionado
            marcados.append(user.num)
        while fila: #Enquanto a fila não estiver vazio
            user = fila.pop(0) #O pop é muito relevante, pois além de excluir da fila eu retorno o valor que precisa informar seus filhos que serão adicionados
            for a in user.adjacentes: #Vejo os vizinhos do que acabei de visualizar e caso não tenha sido visualizados antes, os adiciono na fila
                add = False
                if a.num not in marcados and a.num!=id_user: #Essas duas condições são verificados constantemente, essa primeira é para adicionar nos marcados e na fila apenas aqueles números que não estão em tais e que não seja o próprio usuário
                    if renda >= 5.25 and len(marcados)<rede: #Já essa é porquê só será adicionado e tratado algo enquanto houver rede e enquanto houver seguidores para serem alcançados
                        marcados.append(a.num)
                        fila.append(a)
                        add = True #Importante essa variável que só será atualizada quando tiver tido alguma adição de seguidor ao escopo
                    else:
                        break
                if not free and add: #Quando tiver ocorrido uma adição e não estiver ainda nos seguidores do primeiro nivel, no estado grátis, irei subtrair a renda
                  if renda>=5.25 and len(marcados)<rede:
                    renda -= 5.25
                  else:
                    break

            if free: #Quando acabar o modo gratuito, rodará essa parte do código só nesse estado
              for i in user.adjacentes: #Verificando os seguidores dos seguidores
                if renda>=5.25 and len(marcados)<rede:
                    renda = self.BFS(i.num, renda, rede, False) #Veja que já não é mais gratuito, a renda estará atualizando e o número passado será o adjacente
              j = 0
              while renda >= 5.25 and len(marcados)<rede: #Se ainda não tiver acabado a renda
                y = self.busca(user.adjacentes[j].num) #Verifica-se com auxilio de contador os seguidores dos seguidores do primeiro seguidor (se não for o bastante do segundo e assim por diante com ajuda do J)
                for u in self.grafo[y].adjacentes:
                    renda = self.BFS(u.num, renda, rede, False)
                j+= 1
            return renda #Para sempre atualizar a renda entre as recursões
class Node:
    def __init__(self, num):
        self.num = num  # Meu valor interno importante para as comparações númericas
        self.adjacentes = []  # Muito semelhante a uma árvore aqui há um encadeamento, porém não apenas do próximo nó, mas sim todos conectados ao vértice pela aresta, por isso necessita-se de uma lista por pode ser n-"amigos"

rede, id_user, boost, count = int(input()), int(input()), int(input()), 0
cingram = Grafo()
marcados = []
while count<rede:
    count+= 1
    linha = input()
    if linha[1]==" ":
        usuario = int(linha[0])
    else:
        usuario = int(linha[0]+linha[1])
    conexoes = list(map(int, linha[4:].split()))
    cingram.amigos(usuario, conexoes)
cingram.BFS(id_user, boost, rede)
print(list(map(str, marcados)))
