#BACKTRACKING
class Bkt():
    def __init__(self, n):
        self.n = n #Quantidade de espectadores
        self.possibilidades = [] #Lista manipulada que vai receber as combinações sem permutações

    def backtrack(self, atual=None, soma_nupla=0, add=1):
        if not atual:
            atual = [] #Combinação atual
        if soma_nupla == self.n:
            self.possibilidades.append(atual[:]) #Quando completar a distribuição das cinco pessoas ele adiciona como uma cópia
            return
        #Se eu já tenho um subconjunto com 3 elementos e n=5, então eu só posso adicionar uma quantia n - soma do subconjunto
        final = n - soma_nupla+1
        for i in range(add, final): #A quantia será contabilizada a partir do último valor adicionado assim assegura uma ordem crescente e evito permutas
            atual.append(i)
            self.backtrack(atual, soma_nupla + i, i)
            atual.pop() #Resetando a variável para tratar a próxima combinação

n = int(input())
cinema = Bkt(n)
cinema.backtrack()

print("Uma sessão com", n, "pessoas pode ter sua audiência nos seguintes subgrupos:")
for j in cinema.possibilidades:
    print(j)
