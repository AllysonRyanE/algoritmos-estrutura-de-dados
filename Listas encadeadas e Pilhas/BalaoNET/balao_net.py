#PILHA E LISTA DUPLAMENTE ENCADEADA
'''Usando POO, para fim de reutilização e escalabilidade do script, crio uma classe que tem como foco a criação dos nós'''


class Rope:
    def __init__(self, atual):
        self.atual = atual  # Dado tratado
        self.proximo = None  # Utilizado p/referenciar o próximo elemento
        self.anterior = None  # Como uma lista DUPLAMENTE encadeado tem link com o elemento anterior na lista, faço uma variável que terá o anterior


class LinkedList:
    def __init__(self):
        self.p_sair = None  # Variável que irá indicar o dado trabalhado mais recentemente, aquele que tem a preferencia na pilha p/sair
        self.tamanho = 0  # Grande auxiliador para tamanho da lista

    def __len__(
            self):  # Com uma função reservada __len__ conseguimos consultar o valor, obter o valor que esquematizamos para dizer o tamanho da lista
        return self.tamanho

    # Método para adicionar no objeto lista que possa ser criado, como é uma pilha a gente sempre deve ter em mente a analogia que um dado fica SOB o anterior
    # As ordens das variaveis e seus nomes importam muito para compreender e também para não perder elementos
    def push(self, adicionado):
        if self.tamanho == 0:  # Na primeira adição o tamanho da pilha ainda é nulo e suas referências, ASSEGURADAS PELOS ATRIBUTOS DA CLASSE "ROPE" ACIONADA ABAIXO, são vazias
            self.p_sair = Rope(
                adicionado)  # Assim que entra deve se tornar um nó e ter atributos de dupla ligação, além disso como é o único e mais recente é o preferencial para sair
        else:
            seta = self.p_sair  # Essa variavel resumidamente faz com que possamos nos deslocar pela lista e não perder dados, fará mais sentido com o tempo
            self.p_sair = Rope(
                adicionado)  # Tendo armazenado o site anterior na seta, agora podemos fazer que a nova entrada seja a preferencial p/sair, como deve ser em uma pilha
            seta.anterior = self.p_sair
            '''Lemos uma pilha de cima para baixo, do mais recente adicionado para o mais antigo, como um 
            histórico de navegação, o 2 está em cima do 1, lendo ela de cima para baixo chegaremos no 1 e como esse tem uma marcação, a seta, essa também tem os atributos de um nó,
            e antes dela podemos dizer que vem o 2, aquele que por ser mais recente é o preferido para sair'''
            self.p_sair.proximo = seta  # O próximo preferido a sair é o próprio 1 seguindo a ordem pilhada
        self.tamanho += 1

    # Remover um elemento de uma lista encadeada trata-se de reajustar ponteiros para que não haja mais nada, nenhuma variavél fazendo referência ao elemento
    def remove(self, excluido):
        # Em uma complexidade O(1) a gente pode ter o melhor caso sendo querer excluir aquilo que já está no topo da pilha
        if self.p_sair.atual == excluido and self.p_sair.proximo != None:
            self.tamanho -= 1
            self.p_sair = self.p_sair.proximo
            self.p_sair.anterior = None
            return True
        # Aqui estaria deixando a lista antes unitária agora vazia
        elif self.p_sair.atual == excluido and self.p_sair.proximo == None:
            self.p_sair = self.p_sair.proximo
            self.tamanho -= 1
        elif self.p_sair != excluido:
            seta = self.p_sair
            # Ajustar os ponteiros significa atualiza-los para que as referências do elemento excluido torne-se do seu sucessor e que seu sucessor tem um novo antecessor
            while (seta):
                if seta.atual == excluido:
                    if seta.proximo:
                        seta.proximo.anterior = seta.anterior
                    seta.anterior.proximo = seta.proximo
                    self.tamanho -= 1
                    return True
                seta = seta.proximo
        else:
            return None

    # Apenas uma simples função de percorrer a pilha com a seta até que haja o primeiro elemento a ter sido adicionado, identificamos ele pelo fato dele não ter um nó próximo
    def show(self):
        seta = self.p_sair
        while (seta):
            print(seta.atual)
            seta = seta.proximo

    # FIND é apenas remover um termo especifico fazendo todo ajuste de seta e logo em seguido adiciona-lo, pois assim ele estará no topo
    def first(self, deslocado):
        self.remove(deslocado)
        self.push(deslocado)


site = None
history = LinkedList()
while (site != "END"):
    site = input()

    if site[:3] == "ADD":
        history.push(site[4:])
    elif site[:3] == "REM":
        history.remove(site[4:])
    elif site[:4] == "EXIB":
        history.show()
    elif site[:3] == "END":
        break
    elif site[:4] == "FIND":
        history.first(site[5:])
    else:
        pass