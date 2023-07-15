#SELECTION, BUBBLE, INSERTION, QUICK, SHELL

acoes_jogadores = []
acoes_quicksort = [] #Essa minha variável resolve um problema com sobrescrever contadores (comparações e trocas) dentro do quicksort, devido à recursão
def winner(jogador):
    global acoes_jogadores #Função para contornar repetição de processos na impressão do output e facilitar nas condicionais para definir vencedor
    acoes_jogadores.append(jogador[0]+jogador[1])

def selection(lista, incremento = None):
    comparacoes, trocas = 0, 0
    for pos in range(len(lista)-1): #Esse for serve para que seja feito em sublistas, minha primeira posição "disponivel", desatualizada será a lista[0], mas depois ela já esttará coerente
        menor = pos
        for i in range(pos+1, len(lista)): #Caminhando pelos indices da lista para obter o menor valor e armazenar seu index em uma variável, mas claro partindo não do inicio da lista, mas do posterior ao último elemento atualizado
            comparacoes += 1
            if incremento:
                if comparacoes + trocas >= incremento:
                    return lista
            if lista[i]<lista[menor]: #Comparo elemento por elemento da lista e vejo se algum é menor que o primeiro
                menor = i
        if lista[pos]>lista[menor]: #Uso da questão da integridade para operacionalizar as trocas, se quem está na primeira posição é maior do que quem está no indice capturado, deve haver um swap, uma troca
            lista[pos],lista[menor] = lista[menor], lista[pos]
            trocas += 1
            if incremento:
                if comparacoes + trocas >= incremento:
                    return lista
    if not incremento:
        return (comparacoes, trocas)
    else:
        return lista

def bubble(lista, incremento = None):
    comparacoes = trocas =  0
    for j in range(len(lista)-1): #Realizar a troca apenas uma vez não assegura que será retornado uma lista ordenada, isso seria um dos melhores casos, mas deve-se pensar de maneira geral, o pior caso exige complexidade O(n-1), após isso é assegurado que a lista está perfeitamente ordenada (Mas muitas vezes ela se ordena antes e isso acaba por ser um desperdicio)
        for i in range(0, len(lista)-j-1): #Tanto aqui quanto no select posso comparar até o penúltimo, pois já estará sendo comparado indiretamente o último
            if lista[i] > lista[i+1]: #Comparo elementos adjacentes
                trocas+= 1
                if incremento:
                    if comparacoes+trocas>= incremento:
                        return lista
                lista[i], lista[i+1] = lista[i+1], lista[i]
            comparacoes += 1
            if incremento:
              if comparacoes+trocas>= incremento:
                 return lista
    if not incremento:
        return (comparacoes, trocas)

def quick(lista, inicio, fim, incremento = None):
  global acoes_quicksort #Usarei para armazenar as comparações e trocas
  if inicio >= 0 and fim >= 0 and inicio < fim: #Enquanto não for todos elementos analisados
    p = partition(lista, inicio, fim)
    if not len(acoes_quicksort):
        acoes_quicksort.append(p[1])
        acoes_quicksort.append(p[2])
    else:
        acoes_quicksort[0] += p[1]
        acoes_quicksort[1] += p[2]
    quick(lista, inicio, p[0])#Recursão na sublista à esquerda (menores) referenciando até o meio da lista (o pivô)
    quick(lista, p[0]+1, fim)#Recursão na sublista à direita (maiores) começando pelo meio, pelo pivô
    if not incremento:
        return (acoes_quicksort[0], acoes_quicksort[1])
    else:
        return lista

def partition(lista, inicio, fim, incremento = None):
  comparacoes, trocas = 0, 0
  pivo = lista[(inicio + fim) // 2] #Não posso usar len, pois irei tratar sublistas
  i = inicio #Esses são os ponteiros, vão servir para que ponha todos os elementos maiores que o pivô à sua direita e menor à esquerda, como isso é feito recursivamente em sublistas têm-se uma ordenação
  j = fim #Eles criam delimitações com os elementos que estão entre os mesmos sendo maiores que o pivô, quando encontra-se um elemento menor que tal se avança o ponteiro mais recuado(o J) e troca as posições do primeiro elemento entre os ponteiros e o menor elemento encontrado, ficando esse antes dos ponteiros
  while True:
    if i >= j: #Quando meus ponteiros se encontram significa que analisei e fiz as trocas devidas na lista
      return (j, comparacoes, trocas) #Meu return desempenha também papel de break
    while lista[i] < pivo:
      comparacoes+= 1 #O elemento está no lado correto, posso avançar com o ponteiro que tem começo no inicio da lista tratada
      i += 1
    while lista[j] > pivo:
      comparacoes+= 1 #Mesma ideia, mas com o ponteiro que tem inicio no fim da lista
      j -= 1
    lista[i], lista[j] = lista[j], lista[i] #Troco após visualizar que o meu elemento mais à extrema direita é menor e a outra ponta é maior, caracteristicas não coerentes para o ordenamento
    trocas += 1

def insert(lista, incremento = None):
    comparacoes, trocas = 0, 0
    for i in range(1, len(lista)): #O primeiro elemento não é alvo *primário* de comparações, pois não vem nada antes dele para que seja comparado e os todos os posteriores serão analisados, tanto isso que uma lista unitária já está ordenada
        ponteiro = lista[i]
        esq_ponteiro = i - 1
        while esq_ponteiro >=0 and lista[esq_ponteiro]>ponteiro: #Enquanto houver elementos à esquerda quero que ocorra a comparação, tendo como parada a ordem, ou seja que esse elemento à esquerda seja menor ou igual
            comparacoes+= 1
            if incremento:
                if comparacoes + trocas >= incremento:
                    return lista
            lista[esq_ponteiro+1] = lista[esq_ponteiro] #Avanço o maior valor
            esq_ponteiro -= 1
            trocas += 1
            if incremento:
                if comparacoes + trocas >= incremento:
                    return lista
        lista[esq_ponteiro+1] = ponteiro #Coloco o menor valor na posição que estava o maior
        if esq_ponteiro >= 0:
            comparacoes+= 1
            if incremento:
                if comparacoes + trocas >= incremento:
                    return lista
    if not incremento:
        return (comparacoes, trocas)
    else:
        return lista

def shell(lista, incremento = None):
    distancia = len(lista)//2 #Diferente do insertion sort onde há comparações de adjacentes aqui há uma distância mutável entre os elementos comparados
    comparacoes, trocas = 0, 0
    while distancia>0: #Não há comparações quando os ponteiros, as referências retornam o mesmo elemento
        i = distancia #Meu primeiro ponteiro começa no metade da lista
        while i < len(lista): #Entrar aqui é não ter acabado o ordenamento, por não ter ainda analisado todos elementos
            ponteiro = lista[i] #Recebe o valor do index indicado no ponteiro para substituição sem perder valor
            check = False
            j = i - distancia #Como J depende de I, incrementar I é incrementar J
            while j >= 0 and lista[j] > ponteiro:
                comparacoes += 1
                trocas += 1
                if incremento:
                    if comparacoes+trocas>= incremento:
                        return lista
                lista[j + distancia] = lista[j] #O elemento do ponteiro mais recuado é empurrado para o centro da lista
                check = True
                j -= distancia #Esse ponteiro ficando negativo significa que não há elementos anteriores a tal
            if check:
                lista[j + distancia] = ponteiro #Resgato o valor que foi sobrescrito em uma posição mais coerente, ordenada
            i += 1 #O ponteiro que inicia em len()//2 agora é incrementado
            if j>=0:
                comparacoes+=1
                if incremento:
                    if comparacoes+trocas>= incremento:
                        return lista
        distancia //= 2 #Aqui começo a comparar elementos adjacentes para finalizar a ordenação, mas já haverá uma lista bem mais favorável
    if not incremento:
        return (comparacoes, trocas)
    else:
        return lista

livros = list(map(int, input().split()))
caca_rato = bubble(livros[:])
winner(caca_rato)
grafite = selection(livros[:])
winner(grafite)
lacraia = insert(livros[:])
winner(lacraia)
toninho = quick(livros[:], 0, len(livros)-1)
winner(toninho)
rivaldo = shell(livros[:])
winner(rivaldo)
print(f"Caça-Rato ordena a lista com {caca_rato[0]} comparações e {caca_rato[1]} trocas.")
print(f"Grafite ordena a lista com {grafite[0]} comparações e {grafite[1]} trocas.")
print(f"Lacraia ordena a lista com {lacraia[0]} comparações e {lacraia[1]} trocas.")
print(f"Rivaldo ordena a lista com {rivaldo[0]} comparações e {rivaldo[1]} trocas.")
print(f"Toninho ordena a lista com {toninho[0]} comparações e {toninho[1]} trocas.")

minimo_vencedor = acoes_jogadores[1]
for x in range(1, len(acoes_jogadores)):
  if acoes_jogadores[x]< minimo_vencedor:
    minimo_vencedor = acoes_jogadores[x] #Já tem todas as ações de cada jogador, preciso do menor número

if minimo_vencedor== caca_rato[0]+caca_rato[1]:
    print(f"-VENCEDOR DA RODADA-\nO vencedor da rodada é Caça-Rato, com {minimo_vencedor} ações.")
    print("-Toninho está a dormir...-\nOs outros estagiários retornam as seguintes listas com essa quantidade de ações:")
    grafite = selection(livros[:], minimo_vencedor)
    print(f"Com {minimo_vencedor} ações, Grafite ordena a lista assim: {grafite}")
    lacraia = insert(livros[:], minimo_vencedor)
    print(f"Com {minimo_vencedor} ações, Lacraia ordena a lista assim: {lacraia}")
    rivaldo = shell(livros[:], minimo_vencedor)
    print(f"Com {minimo_vencedor} ações, Rivaldo ordena a lista assim: {rivaldo}")
elif minimo_vencedor== grafite[0]+grafite[1]:
    print(f"-VENCEDOR DA RODADA-\nO vencedor da rodada é Grafite, com {minimo_vencedor} ações.")
    print("-Toninho está a dormir...-\nOs outros estagiários retornam as seguintes listas com essa quantidade de ações:")
    caca_rato = bubble(livros[:], minimo_vencedor)
    print(f"Com {minimo_vencedor} ações, Caça-Rato ordena a lista assim: {caca_rato}")
    lacraia = insert(livros[:], minimo_vencedor)
    print(f"Com {minimo_vencedor} ações, Lacraia ordena a lista assim: {lacraia}")
    rivaldo = shell(livros[:], minimo_vencedor)
    print(f"Com {minimo_vencedor} ações, Rivaldo ordena a lista assim: {rivaldo}")
elif minimo_vencedor== lacraia[0]+lacraia[1]:
    print(f"-VENCEDOR DA RODADA-\nO vencedor da rodada é Lacraia, com {minimo_vencedor} ações.")
    print("-Toninho está a dormir...-\nOs outros estagiários retornam as seguintes listas com essa quantidade de ações:")
    caca_rato = bubble(livros[:], minimo_vencedor)
    print(f"Com {minimo_vencedor} ações, Caça-Rato ordena a lista assim: {caca_rato}")
    grafite = selection(livros[:], minimo_vencedor)
    print(f"Com {minimo_vencedor} ações, Grafite ordena a lista assim: {grafite}")
    rivaldo = shell(livros[:], minimo_vencedor)
    print(f"Com {minimo_vencedor} ações, Rivaldo ordena a lista assim: {rivaldo}")
elif minimo_vencedor== toninho[0]+toninho[1]:
    print(f"-VENCEDOR DA RODADA-\nO vencedor da rodada é Toninho, com {minimo_vencedor} ações.")
    print("-Toninho está a dormir...-\nOs outros estagiários retornam as seguintes listas com essa quantidade de ações:")
    caca_rato = bubble(livros[:], minimo_vencedor)
    print(f"Com {minimo_vencedor} ações, Caça-Rato ordena a lista assim: {caca_rato}")
    grafite = selection(livros[:], minimo_vencedor)
    print(f"Com {minimo_vencedor} ações, Grafite ordena a lista assim: {grafite}")
    lacraia = insert(livros[:], minimo_vencedor)
    print(f"Com {minimo_vencedor} ações, Lacraia ordena a lista assim: {lacraia}")
    rivaldo = shell(livros[:], minimo_vencedor)
    print(f"Com {minimo_vencedor} ações, Rivaldo ordena a lista assim: {rivaldo}")
else:
    print(f"-VENCEDOR DA RODADA-\nO vencedor da rodada é Rivaldo, com {minimo_vencedor} ações.")
    caca_rato = bubble(livros[:], minimo_vencedor)
    print(f"Com {minimo_vencedor} ações, Caça-Rato ordena a lista assim: {caca_rato}")
    grafite = selection(livros[:], minimo_vencedor)
    print(f"Com {minimo_vencedor} ações, Grafite ordena a lista assim: {grafite}")
    lacraia = insert(livros[:], minimo_vencedor)
    print(f"Com {minimo_vencedor} ações, Lacraia ordena a lista assim: {lacraia}")