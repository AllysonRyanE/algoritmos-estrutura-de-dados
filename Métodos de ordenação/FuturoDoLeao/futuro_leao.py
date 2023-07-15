#MERGESORT
class StackMerged:  #Irei criar uma classe para que consiga organizar atributos que serão posteriormente úteis
    def __init__(self, sport, europeu):
        self.sport = sport #Minhas listas são os únicos valores que devem ser informado
        self.europeu = europeu
        self.ordenada = None #posteriormente armazenará meu resultado
        self.inicio = 0
        self.meio = 0
        self.fim = 0
        self.mediana = 0

    def merge(self): #Usarei os valores recebidos na criação do objeto
        ordem = []
        i = j = 0
        while i < len(self.sport) and j < len(self.europeu): #Ambas a listas precisam ser analisadas
            if self.sport[i] <= self.europeu[j]: #Os ponteiros conceituam-se em visualizar e comparar o topo das listas, em uma ideia semelhante a oilhas. Vejo o primeiro elemento adicionado, o primeiro indice de uma lista e de outra, comparo-os e então a lista que tever o menor elemento tem seu ponteiro avançado
                ordem.append(self.sport[i])
                i += 1
            else:
                ordem.append(self.europeu[j])
                j += 1
        ordem += self.sport[i:]
        ordem += self.europeu[j:] #Receber o último elemento que não terá adjacente
        self.ordenada = ordem
        return ordem

    def calculo_mediana(self):
        n = len(self.ordenada)
        if not n % 2:
            mediana = (self.ordenada[n // 2 - 1] + self.ordenada[n // 2]) / 2
        else:
            mediana = self.ordenada[n // 2]
        self.mediana = mediana

sport = list(map(int, input().strip().split()))
europeu = list(map(int, input().strip().split()))
proposta = StackMerged(sport, europeu) #Adotando uma visão sabendo que as listas estão ordenados basta apenas que informe como atributos
proposta.merge()
proposta.calculo_mediana()
print("O salário sugerido por Juba na primeira negociação será de {:.2f} mil reais.".format(proposta.mediana))
