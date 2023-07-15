#ARVORE BST(BUSCA BINÁRIA)
class Node:  # Apesar de estruturar uma árvore a ideia de nó aqui é muito presente
    def __init__(self, num):
        self.num = num
        self.esquerda = None
        self.direita = None
        self.progenitor = None
        self.altura = None


class ArvoreBB:
    def __init__(self, num=None, node=None):  # Tenho nó e número pois será útil para quando for trabalhar subárvores no percuso em nivel
        if node:  # Se for informado um nó será fixado tal como raiz e expresso sua subárvore, esse parâmetro acaba por ser como um recurso opcional que tem um padrão em case null
            self.raiz = node
        elif num:  # Mas o número sendo informado na criação dessa árvore já tem ali uma raiza
            node = Node(num)  # Já adotamos ele como um nó para podermos ter seu duplo cadeamento (R;L)
            self.raiz = Node
        else:
            self.raiz = None

    def add(self, adicionado, altura= 0, pai= None, ponteiro = 0):
      if ponteiro == 0: #A primeira adição entrará nessa condição como qualquer outra, mas a raiz será None
        ponteiro = self.raiz #Estratégia padrão de ponteiro para deslocar-se pela árvore sem perder informações, esse processo deve começar pela raiz
      if ponteiro:
        pai = ponteiro  # Pai aqui se refere a quem será o pai do adicionado e ele guardará o valor final do ponteiro
        if adicionado < ponteiro.num:  # Se o número que eu quiser adicionar for menor que o número que o ponteiro tá apontado eu vou mover esse pointer p/esquerda
            altura += 1
            ponteiro = self.add(adicionado, altura, ponteiro, ponteiro.esquerda) #Recursão passando os dados atualizados como parâmetro, inclusive o ponteiro indo p/esquerda pelo num adicionado ser menor
            return ponteiro
        elif adicionado > ponteiro.num:
            altura += 1
            ponteiro = self.add(adicionado, altura, ponteiro, ponteiro.direita)
            return ponteiro
      if pai is None:  # Para unicamente uma primeira adição onde ainda não há raiz, pois se pai é vazio significa que sequer entramos na recursão
        self.raiz = Node(adicionado)
        return altura
      elif adicionado < pai.num:  # Mesmo lógica anterior, mas agora realmente adicionando o nó, a qual só foi possivel com o armazenamento do deslocamento do pointer
        pai.esquerda = Node(adicionado)
        pai.esquerda.progenitor = pai
        return altura #Retornar altura é bem relevante pois vai ser o que vai ser printado
      elif adicionado > pai.num:
        pai.direita = Node(adicionado)
        pai.direita.progenitor = pai
        return altura

    def encontrar(self, pesquisado, altura=0, pai=None, ponteiro=0, encontrado=False):
        if ponteiro == 0: #Irei precisar dessa função principalmente para conseguir tornar um pesquisável para um nó e usufruir de seus atributos
            ponteiro = self.raiz #Como vou caminhar toda árvore, começo da raiz
        if ponteiro and encontrado == False: #Semelhante a While, enquanto não encontrar o elemento faço com recursão o percurso
            pai = ponteiro
            if pesquisado < ponteiro.num:
                altura += 1
                ponteiro = self.encontrar(pesquisado, altura, ponteiro, ponteiro.esquerda, encontrado)
                return ponteiro
            elif pesquisado > ponteiro.num:
                altura += 1
                ponteiro = self.encontrar(pesquisado, altura, ponteiro, ponteiro.direita, encontrado)
                return ponteiro
            elif ponteiro.num == pesquisado:
                ponteiro.altura = altura #Assim que encontro minha altura/profundidade até o nó, tá atualizada, logo atualizo o atributo, isso será útil pois será printada pro user
                encontrado = True
        if pesquisado < pai.num and encontrado:
            return ponteiro
        elif pesquisado > pai.num and encontrado:
            return ponteiro
        elif pai.num == pesquisado and encontrado:
            return ponteiro
        else:
           return -1

    def rotacao_direita(self, elemento):
        pai_esq = elemento.esquerda
        elemento.esquerda = pai_esq.direita
        if pai_esq.direita:
            pai_esq.direita.progenitor = elemento
        pai_esq.progenitor = elemento.progenitor
        if not elemento.progenitor:
            self.raiz = pai_esq
        elif elemento == elemento.progenitor.direita:
            elemento.progenitor.direita = pai_esq
        else:
            elemento.progenitor.esquerda = pai_esq
        pai_esq.direita = elemento
        elemento.progenitor = pai_esq

    def rotacao_esquerda(self, elemento):
        pai_dir = elemento.direita #Aqui armazenamos um filho que será excluido, sendo o pai do elemento que se tornará raiz quando o escopo passado for o avô ou o próprio elemento quando for o pai, fazemos isso pois logo ele irá perder a referência de ser direita de um nó
        elemento.direita = pai_dir.esquerda #Como disse perderiamos
        if pai_dir.esquerda: #Verificamos se existe o elemento que estamos manipulando tem filhos
            pai_dir.esquerda.progenitor = elemento

        pai_dir.progenitor = elemento.progenitor #Atualizando referências
        if not elemento.progenitor: #Isso aqui é o passo final para atualizarmos os atributos da árvore
            self.raiz = pai_dir
        elif elemento == elemento.progenitor.esquerda: #Se ainda não tiver no topo vemos se o elemento é filho esquerdo ou direito e fazemos as atualizações
            elemento.progenitor.esquerda = pai_dir
        else:
            elemento.progenitor.direita = pai_dir
        pai_dir.esquerda = elemento
        elemento.progenitor = pai_dir

    def cache (self, pesquisado, altura= 0, pai = None, ponteiro = 0):
        elemento = self.encontrar(pesquisado)
        if elemento != -1:
            nivel = elemento.altura
            # Pesquisando se existe o pai do pai, pois se não houver avô estamos tratando de um nó que está no nivel, ele só precisará fazer um movimento:
            while (elemento!=self.raiz): #Não acontecerá nenhuma rotação se o elemento pesquisado já for a raiz e mais nenhuma quando ele passar a ser
                    avo = elemento.progenitor.progenitor
                    if not elemento.progenitor.progenitor:
                        if elemento == elemento.progenitor.esquerda: #Vou ver agora se é filho da esquerda ou da direita
                            self.rotacao_direita(elemento.progenitor)
                        else:
                            self.rotacao_esquerda(elemento.progenitor)
                    elif elemento == elemento.progenitor.esquerda and elemento.progenitor == avo.esquerda: #Uma das maiores dificuldades da questão é observar os casos, esse segundo (ou terceiro se considerar o elemento já está na raiz) seria SE O NÓ É UM FILHO A ESQUERDA *E* SE SEU PAI É UM FILHO A ESQUERDA
                        self.rotacao_direita(elemento.progenitor) #Esse caso é um dos espelhos, antes tinha uma árvore que basicamente tratava-se de uma diagonal esquerda e agora devido ao elemento que está mais embaixo, o menor ser a raiz, o resultado deve ser uma diagonal direita
                        self.rotacao_direita(avo)
                    elif elemento == elemento.progenitor.direita and elemento.progenitor == avo.direita:
                        self.rotacao_esquerda(avo)
                        self.rotacao_esquerda(elemento.progenitor)
                    elif elemento == elemento.progenitor.direita and elemento.progenitor == avo.esquerda:
                        self.rotacao_esquerda(elemento.progenitor)
                        self.rotacao_direita(avo)
                    else:
                        self.rotacao_direita(elemento.progenitor)
                        self.rotacao_esquerda(avo)
            return nivel
        else:
            return -1


processador = ArvoreBB()
while True:
    try:
        comandos = input().split()
        if comandos[0] == "ADD":
            print(processador.add(int(comandos[1])))
        elif comandos[0]=="SCH":
            print(processador.cache(int(comandos[1])))
    except EOFError:
        break