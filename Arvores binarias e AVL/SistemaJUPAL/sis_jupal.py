#ARVORE AVL
class Node:
    def __init__(self, num):
        self.num = num
        self.esquerda = None
        self.direita = None
        self.progenitor = None
        self.nivel = 1


class ArvoreAVL:
    # Tenho nó e número pois será útil para quando for trabalhar subárvores no percuso em nivel
    def __init__(self, num=None, node=None):
        if node:  # Se for informado um nó será fixado tal como raiz e expresso sua subárvore, esse parâmetro acaba por ser como um recurso opcional que tem um padrão em case null
            self.raiz = node
        elif num:  # Mas o número sendo informado na criação dessa árvore já tem ali uma raiza
            # Já adotamos ele como um nó para podermos ter seu duplo cadeamento (R;L)
            node = Node(num)
            self.raiz = Node
        else:
            self.raiz = None
        self.tamanho = 0

    def altura(self, node=None): #Essa estrutura ela irá fazer um percurso recursivo pelos nós e então irá retornar qual a subárvore maior
        if node is None:
            node = self.raiz
        aleft = 0 #Consigo através dela percorrer esquerda e direita, após comparar qual é maior para retornar como tamanho da árvore, esse fator também funciona se eu repassar um ramo especifico
        aright = 0
        if node.esquerda: #OBS: A possibilidade de ter uma estrutura semelhante é grande, mas isso se deve ao fato dos alunos terem seguido a recomendação de um dos monitores, foi enviado video do canal Programação Dinâmica
            aleft = self.altura(node.esquerda) #Tentei até fazer por atributo, mas isso se complicava no balanceamento. No fim, eu sei como esse metódo funciona
        if node.direita:
            aright = self.altura(node.direita)
        if aright > aleft:
            return aright + 1
        return aleft + 1

    def profundidade(self, node=None):
        if not node:  # Se não for informado o nó que deve-se partir apenas retorna-se o tamanho da árvore, ainda que seja nulo
            return 0 #Mudei de ideia sobre o que disse acima, tava dando ruim
        else:
            return node.nivel  # Já aqui, informamos a profundidade do nó que foi requisitado

    def num_equilibrio(self, node=None):
        if not node:
            return 0  # O fator de equilibrio é a base inicial da AVL, em suma prezamos que ele seja == 1, ele basicamente é resultado da diferença de profundidade entre as folhas
        return self.profundidade(node.esquerda) - self.profundidade(node.direita)

    def colher(self, pesquisado, pai=None, ponteiro=0, encontrado=False):
        if self.raiz:
            if ponteiro == 0:  # Irei precisar dessa função principalmente para conseguir tornar um pesquisável para um nó e usufruir de seus atributos
                ponteiro = self.raiz  # Como vou caminhar toda árvore, começo da raiz
            # Semelhante a While, enquanto não encontrar o elemento faço com recursão o percurso
            if ponteiro and encontrado == False:
                pai = ponteiro
                if pesquisado < ponteiro.num:
                    ponteiro = self.colher(
                        pesquisado, ponteiro, ponteiro.esquerda, encontrado)
                    return ponteiro
                elif pesquisado > ponteiro.num:
                    ponteiro = self.colher(
                        pesquisado, ponteiro, ponteiro.direita, encontrado)
                    return ponteiro
                elif ponteiro.num == pesquisado:
                    encontrado = True
            if pesquisado < pai.num and encontrado:
                return pai
            elif pesquisado > pai.num and encontrado:
                return pai
            elif pai.num == pesquisado and encontrado:
                return pai
            else:
                return pai
        else:
            return "NAO ENCONTRADO"

    def maximo(self, ponteiro=0):
        if not self.raiz:
            return "ARVORE VAZIA"
        if ponteiro == 0:
            ponteiro = self.raiz
        while (ponteiro.direita):  # O maior valor é sempre aquele mais a direita e sem nenhum filho a direita (é até pleonasmo, se ele tivesse filho à direita não seria o maior)
            ponteiro = ponteiro.direita
        return ponteiro.num

    def minimo(self, ponteiro=0):
        if not self.raiz:
            return "ARVORE VAZIA"
        if ponteiro == 0:
            ponteiro = self.raiz
        while (ponteiro.esquerda):
            ponteiro = ponteiro.esquerda  # Mesma lógica anáfora do máximo
        return ponteiro

    def fim(self):
        nomes = []
        self._fim(self.raiz, nomes)
        return nomes

    def _fim(self, ponteiro, nomes): #Uso o _ para indicar funções bem distantes do ""usuário""
        if ponteiro == 0:
            ponteiro = self.raiz
        if ponteiro.esquerda:
            # Respeitando a lexicografia, a ordem a alfabética deve-se observar bem a estrutura da árvore e vemos um percurso EM ORDEM(esquerda->raiz->direita(recursivamente))
            self._fim(ponteiro.esquerda, nomes)
        nomes.append(ponteiro.num) #É com recursão que caminho a árvore toda, mas a garantia de impressão na posição certa parte da lista
        if ponteiro.direita:
            self._fim(ponteiro.direita, nomes)

    def in_order(self, node=0, evento=False, ponteiro=0): # Tenho a liberdade de dizer a partir de que nó imprimo a subárvore
        if node != 0 and evento == False:
            ponteiro = self.colher(node)
            evento = True #O evento é basicamente um contador para que não se entre nessa condicional mais vezes do que deveria o primeiro critério não seria suficiente
        if node == 0:
            ponteiro = self.raiz
        if ponteiro.esquerda:
            self.in_order(ponteiro.esquerda, evento, ponteiro.esquerda)
        print(ponteiro.num)
        if ponteiro.direita:
            self.in_order(ponteiro.direita, evento, ponteiro.direita)

    def encontrar(self, pesquisado, altura=0, pai=None, ponteiro=0, encontrado=False):
        if self.raiz:
            if ponteiro == 0:  # Irei precisar dessa função para identificar se há um valor apontado dentro da árvore, muito semelhante a função acima, mas aqui eu apenas retorno um booleano
                ponteiro = self.raiz  # Como vou caminhar toda árvore, começo da raiz
            # Semelhante a While, enquanto não encontrar o elemento faço com recursão o percurso
            if ponteiro and encontrado == False:
                pai = ponteiro
                if pesquisado < ponteiro.num:
                    ponteiro = self.encontrar(
                        pesquisado, altura, ponteiro, ponteiro.esquerda, encontrado)
                    return ponteiro
                elif pesquisado > ponteiro.num:
                    ponteiro = self.encontrar(
                        pesquisado, altura, ponteiro, ponteiro.direita, encontrado)
                    return ponteiro
                elif ponteiro.num == pesquisado:
                    encontrado = True
            if pesquisado < pai.num and encontrado:
                return encontrado
            elif pesquisado > pai.num and encontrado:
                return encontrado
            elif pai.num == pesquisado and encontrado:
                return encontrado
            else:
                return encontrado
        else:
            return encontrado

    def rota_direita(self, elemento):
        pai_esq = elemento.esquerda
        elemento.esquerda = pai_esq.direita
        pai_esq.direita = elemento

        elemento.nivel = 1 + \
            max(self.profundidade(elemento.esquerda),
                self.profundidade(elemento.direita))
        pai_esq.nivel = 1 + \
            max(self.profundidade(elemento.esquerda),
                self.profundidade(elemento.direita))

        return pai_esq

    def rota_esquerda(self, elemento):
        pai_direita = elemento.direita #Aqui armazenamos um filho que será excluido, sendo o pai do elemento que se tornará raiz quando o escopo passado for o avô ou o próprio elemento quando for o pai, fazemos isso pois logo ele irá perder a referência de ser direita de um nó
        elemento.direita = pai_direita.esquerda #Como disse, perderiamos
        pai_direita.esquerda = elemento
        elemento.nivel = 1 + \
            max(self.profundidade(elemento.esquerda),
                self.profundidade(elemento.direita))
        pai_direita.nivel = 1 + \
            max(self.profundidade(pai_direita.esquerda),
                self.profundidade(pai_direita.direita))

        return pai_direita

    def check_sum(self, node, elemento):
        equilibrio = self.num_equilibrio(node) #Meu fator de balanceamento
        if equilibrio > 1 and elemento < node.esquerda.num: #Temos aqui agora os casos que vão depender de dois aspectos, se meu fator retorna maior ou menor que 1 e a posição do meu nó, a qual decide as rotações, com isso combinamos esses dois critérios
            return self.rota_direita(node)

        if equilibrio < -1 and elemento > node.direita.num:
            return self.rota_esquerda(node)

        if equilibrio > 1 and elemento > node.esquerda.num:
            node.esquerda = self.rota_esquerda(node.esquerda)
            return self.rota_direita(node)

        if equilibrio < -1 and elemento < node.direita.num:
            node.direita = self.rota_direita(node.direita)
            return self.rota_esquerda(node)

        return node

    def check_sub(self, node, elemento):
        equilibrio = self.num_equilibrio(node)
        if equilibrio > 1 and self.num_equilibrio(node.esquerda) >= 0:
            return self.rota_direita(node)
        if equilibrio < -1 and self.num_equilibrio(node.direita) <= 0:
            return self.rota_esquerda(node)

        if equilibrio > 1 and self.num_equilibrio(node.esquerda) < 0:
            node.esquerda = self.rota_esquerda(node.esquerda)
            return self.rota_direita(node)

        if equilibrio < -1 and self.num_equilibrio(node.direita) > 0:
            node.direita = self.rota_direita(node.direita)
            return self.rota_esquerda(node)

        return node

    def novo_no(self, node, adicionado):
        if not self.encontrar(adicionado):
            if not node: #Parece estranho, mas como busco uma folha, eu basicamente adiciono o nó quando chego aqui, embaixo estou percorrendo pra pôr no lugar certo
                return Node(adicionado)
            elif adicionado < node.num:
                node.esquerda = self.novo_no(node.esquerda, adicionado)
            else:
                node.direita = self.novo_no(node.direita, adicionado)

            node.nivel = 1 + max(self.profundidade(node.esquerda),
                                 self.profundidade(node.direita))
            return self.check_sum(node, adicionado)
        else:
            return False

    def del_no(self, node, excluido):
        if self.encontrar(excluido):
            if not node:
                return node
            elif excluido < node.num:
                node.esquerda = self.del_no(node.esquerda, excluido)
            elif excluido > node.num:
                node.direita = self.del_no(node.direita, excluido)
            else: #Acima estava percorrendo recursivamente, aqui eu encontrei meu alvo e vou atualizar as referência de esquerda e direita para que ele seja isolado, não tem mais ponteiro para ele
                if node.esquerda is None:
                    alterado = node.direita
                    node = None
                    return alterado
                elif node.direita is None:
                    alterado = node.esquerda
                    node = None
                    return alterado
                #Em algumas situações de raiz o número que deve ocupar o lugar de um excluido para permanecer a lógica de uma busca binária é seu sucessor
                sucessor = self.minimo(node.direita)
                node.num = sucessor.num
                node.direita = self.del_no(node.direita, sucessor.num)

            if node is None:
                return node

            node.nivel = 1 + max(self.profundidade(node.esquerda),
                                 self.profundidade(node.direita)) #Atualizo o nivel usando a função que compara o maior entre dois parâmetros
            return self.check_sub(node, excluido) #No fim chamo meu balanceamento
        else:
            return False

    def add(self, adicionado):
        self.raiz = self.novo_no(self.raiz, adicionado)
        if self.raiz != False:
            return adicionado
        else:
            return False

    def remove(self, excluido):
        existe = self.encontrar(excluido)
        if existe != False:
            self.raiz = self.del_no(self.raiz, excluido) #Tenho que começar percursos pela raiz
            return excluido #Retorno o que foi requisitado para que seja printado
        else:
            return False

pessoas = ArvoreAVL()
while True:
    comandos = input().split()
    if comandos[0] == "INSERIR":
        novo = pessoas.add(comandos[1])
        if novo != False:
            print(f"{novo} INSERIDO")
        elif not novo:
            print(f"{comandos[1]} JA EXISTE")
    elif comandos[0] == "VER":
        if len(comandos) == 1:
            pessoas.fim()
        elif len(comandos) > 1:
            pessoas.in_order(comandos[1])
    elif comandos[0] == "ALTURA":
        print(f"ALTURA: {pessoas.altura()}")
    elif comandos[0] == "MAXIMO":
        if pessoas.raiz:
            print(f"MAIOR: {pessoas.maximo()}")
        else:
            print("ARVORE VAZIA")
    elif comandos[0] == "MINIMO":
        if pessoas.raiz:
            print(f"MENOR: {pessoas.minimo().num}")
        else:
            print("ARVORE VAZIA")
    elif comandos[0] == "DELETAR":
        removido = pessoas.remove(comandos[1])
        if removido != False: #Ele retorna falso apenas quando aquele elemento não foi encontrado dentro da função faz isso através do metódo "encontrar", a lógica anáfora vale para o add
            print(f"{comandos[1]} DELETADO")
        else:
            print(f"{comandos[1]} NAO ENCONTRADO")
    elif comandos[0] == "FIM":
        if pessoas.raiz:
            print(' '.join(pessoas.fim())) #Afim de corrigir a verticalidade e ter o espaçamento correto uso o join
        else:
            print("ARVORE VAZIA")
        break
