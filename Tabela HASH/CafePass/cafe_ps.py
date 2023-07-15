class Hash: #Crio uma classe que faz uso de uma tabela hash a qual varia em tamanho de acordo com a necessidade
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tabela = [[] for i in range(self.tamanho)]

    def espalhamento(self, chave, index=None): #Diferentemente de uma lista comum, aqui tenho uma criterização para inserção, esse algoritmo faria-se ainda mais útil caso pretendesse buscar um elemento, pois precisaria apenas executar a função hash sob o pesquisado e retornaria minha possivel posição, executando um O(1)'''
      fator_carga = chave % self.tamanho #Meu fator de carga é meu critério, ele vai de acordo com o tamanho da minha lista, o mesmo não impede colisões, porém por ser um número primo é bem útil'''
      contador = False #Esse contador servirá como uma condição de parada
      if index is None: #Se meu index for vazio ou seja fruto de uma não-recursão eu irei assumi-lo como o resultado da minha operação feita no fator de carga
        index = fator_carga #O resultado da operação indicará em que posição deve ser adicionado
      if len(self.tabela[index]) == 0: #Verifico se não há elementos ali
        self.tabela[index].append(chave)
        contador = True #Logo após adicionar indico isso pela variavél bool
        return contador
      else: #Mas se estiver ocorrendo uma colisão...
        if not contador: #Irei fazer uma recursão até encontrar um espaço vazio e adicionar o meu elemento, é por isso que o Hash aqui é bem útil eu faço uso dos espaços vazios como condições de parada para processos que poderiam demorar mais, assim como os ponteiros caminhas nas árvores em busca de folhas, para saber quando adicionar um nó, aqui            busco esses espaços vazios, mesmo tendo elementos posteriores, dessa maneira minha inserção exige menos processamento'''
          if index != self.tamanho-1:
            index += 1 #Vou usando meu index como ponteiro e não partindo do começo da lista, mas sim da posição que deveria estar, mas está preenchida, o index serve como o ponteiro ou um cabeçote deslocável'''
            blank = self.espalhamento(chave, index)
          else: #Mas caso a colisão esteja acontecendo na última posição, eu volto para o começo da tabela
            index = 0
            blank = self.espalhamento(chave, index)

    def magic_number(self, number):
        soma = None
        check = False #Usarei para dar meu retorno correto, apontando se o Magic Number foi obtido ou não
        for j in range(len(self.tabela)): #Com essa estrutura todos os números vão somar um com os outros
            for x in range(len(self.tabela)):
                if x != j: #Para não somar um número com ele mesmo
                    if len(self.tabela[j]) and len(self.tabela[x])==1: #Mas se aproveitando novamente dá técnica Hash, essa soma só acontecerá entre os valores que realmente tem algum número ocupando, reduzindo o número de operações
                        soma = self.tabela[j][0] + self.tabela[x][0]
                if soma == number: #Verifico a cada soma se foi o Magic Numbermber
                    check = True
                    break #Se já obtive já encerro, não preciso de mais verificações
        if check:
            return "UP Permission"
        else:
            return "NOT Permission"


lin = int(input())
count = 0
while (count != lin):
    cafe_pass = Hash(11)
    count += 1 #Só ira executar uma quantidade de vocês igual a informada
    comando = input().split()
    random_number = int(comando[1])
    digitos = []
    for x in comando[0]:
        digitos.append(int(x) * 10) #Multiplicando todos por 10 após converte-los para inteiro
    digitos_duplos = digitos[:]
    digitos_hash = []
    for x in digitos:
        eventos = digitos_duplos.count(x) #Conto as aparições
        if eventos == 1: #Mesmo que a duplicata ainda esteja na lista do input que foi *10 estou operacionalizando com uma cópia modificada e o resultado final só agregará a primeira aparição já que a condição de adicionar nesse é exisir ao menos uma vez e o número já foi deletado
            digitos_hash.append(x) #Sendo apenas uma já adiciono na minha entrada tratada que irá para a tabela
        elif eventos > 1:
            digitos_hash.append(x * eventos) #Se não, multiplico de acordo com as aparições antes
            for y in range(eventos):
                digitos_duplos.pop(digitos_duplos.index(x))  #Irei eliminar da minha lista que faço análise de quantias as duplicatas do número para que ele não seja nem tratado e nem adicionado no valor final, já que sua existência já foi comprimida na primeira apariçaõ sendo multiplicada
                #Esse metódo não trará o problema de somar duplicatas com números nativos, pois o meu resultado das duplicatas está sendo armazenado em outra variável
    for x in digitos_hash:
        cafe_pass.espalhamento(x) #Chamo minha função Hash pra cada elemento os posicionamento devidamente
    print(cafe_pass.magic_number(random_number))








