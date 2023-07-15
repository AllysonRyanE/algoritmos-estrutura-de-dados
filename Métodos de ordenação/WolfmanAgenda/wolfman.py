#HEAPSORT
def heapify_max(lista, n, i):
    maior = i #Essa variável armazena o último pai da árvore e será substituida, caso um de seus filhos seja maior(representando desordem)
    # Aqui eu obtenho o que seria na árvore o filho do último nó com filhos, logo esse não tem filhos
    esquerda = 2 * i + 1 #"Fórmula" p/conseguir o indice do filho à esquerda
    direita = 2 * i + 2 #"Fórmula" p/conseguir o indice do filho à direita

    #Verifica se o filho da esquerda existe e se é maior que o pai
    if esquerda < n and lista[esquerda] > lista[maior]:
        maior = esquerda

    #Verifica se o filho da direita existe e se é maior que o pai
    if direita < n and lista[direita] > lista[maior]:
        maior = direita

    #Se o maior foi alterado é porquê um dos filhos foi maior e agora essa variável tem seu index
    if maior != i:  #Troco suas posições
        lista[i], lista[maior] = lista[maior], lista[i]

def heapsort_max(lista):
    n = len(lista)
    #A parametrização desse 'for' pode parecer complexa, mas isso se dá por ser fruto de uma "estratégia". O HeapSort consiste em ordenar uma lista tratando-a como uma Árvore Binária Heap(Com o valor dos nós crescendo ou diminuindo até se ter o máx ou min na raiz(Conhecida ordem crescente ou decrescente quando tido em uma lista))
    #Quando sob a lista for tratado HeapSort, ou seja quero organiza-lá de maneira que seja coerente a visualização de uma Árvore Bi. Heap, deve-se visitar todos os nós(elementos da lista) que tem filhos e a partir dessas visitas fazer as trocas de index
    for i in range(n // 2 - 1, -1, -1): #Para isso deve-se saber qual o último nó com filhos(index: n//2 - 1) e ir vendo seus antecedentes(a incrementação do i vai i-=1, como apontado no for) até a raiz(como apontado no final do range que é -1, logo vai até 0(raiz))
        heapify_max(lista, n, i) #Vou fazer esse processo para cada pai dessa maneira
    return lista[0]

sequencia = list(map(int, input().split()))
constante = int(input())
count = 0
k = 0
while len(sequencia)>0:
    count += 1
    maximo = heapsort_max(sequencia)
    minimo = sequencia[len(sequencia)//2]
    for x in range((len(sequencia)//2+1), len(sequencia)):
        if sequencia[x]<minimo:
            minimo = sequencia[x]
    sequencia.pop(sequencia.index(maximo))
    min_const = minimo*constante
    if min_const<0:
        min_const *= -1
    k = maximo - min_const
    if k>0:
        sequencia.append(k)
print(f"{count} rodadas, partindo para a próxima!")