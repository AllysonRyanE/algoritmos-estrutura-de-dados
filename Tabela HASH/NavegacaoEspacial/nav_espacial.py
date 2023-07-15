class Hash:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tabela = [[] for i in range(self.tamanho)]
        self.memory_slot = -1 #A diferença para a questão A nos atributos é apenas esse que será usado como condição de parada repentina

    def espalhamento(self, chave, index=None): #A inserção é idêntica a da A, pois lá já usava % e na mesma eu explico mais detalhadamente
        fator_carga = chave % self.tamanho
        contador = False
        if index is None:
            index = fator_carga
        if len(self.tabela[index]) == 0:
            self.memory_slot += 1 #O atributo indicará se minha tabela já chegou em seu máximo
            self.tabela[index].append(chave)
            contador = True
            return 'E: ' + str(index)
        else:
            if not contador:
                if index != len(self.tabela) - 1:
                    index += 1
                    blank = self.espalhamento(chave, index)
                    return 'E: ' + str(index)
                else:
                    index = 0
                    blank = self.espalhamento(chave, index)
                    return 'E: ' + str(index)

    def sch(self, number):
        valor =  number%self.tamanho #Caso não tenha ocorrido uma colisão com o elemento esperado, executaremos em complexidade O(1)
        check = None #Pois faremos uma "engenharia reversa" pondo sob o pesquisado a função de inserção
        if number in self.tabela[valor]: #Através dela a tabela Hash mostra sua utilidade, pois essa função, o fator de carga me diz em que indice o elemento deve estar não precisando que eu busque na lista toda em O(n)
          check = self.tabela.index(self.tabela[valor])
        else: #Mas caso não esteja veremos se há colisão ou se o elemento realmente não foi inserido
          elemento = [number]
          for x in self.tabela:
              if x == elemento:
                  check = self.tabela.index(x)
                  break #Um sistema de busca muito simples que será encerrado assim que se encontra o elemento
        if check != None: #Essa variavel armazena a posição, o index
            return 'E: ' + str(check)
        else:
            return 'NE'

    def cap(self, number):
        if len(self.tabela[number]) == 1:
            return 'A: ' + str(self.tabela[number][0]) #Aqui a Hash se faz útil, pois sei que só um elemento por célula e assim não precisa sequer de uma busca, só vejo se tem algum ali e retorno qual é
        else:
            return 'D'


tamanho = int(input())
nave = Hash(tamanho)
lin = int(input())
count = 0
while (count != lin):
    count += 1
    comando = input().split()
    if comando[0] == "ADD":
        print(nave.espalhamento(int(comando[1])))
    elif comando[0] == "SCH":
        print(nave.sch(int(comando[1])))
    elif comando[0] == "CAP":
        print(nave.cap(int(comando[1])))
    if nave.memory_slot == len(nave.tabela):
        print("Toda memoria utilizada")
        break










