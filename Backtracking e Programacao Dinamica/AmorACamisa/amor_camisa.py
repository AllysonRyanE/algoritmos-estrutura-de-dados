#PROGRAMAÇÃO DINÂMICA
class Arquibancada:
    def __init__(self, list):
        self.list = list  # Lista com a quantia de torcedores em cada setor
        self.atual = int  # Variável que atualiza para no fim armazenar o maior valor

    def max(self):
        termo_f = self.list[0]  # Armazena o valor máximo considerando apenas o primeiro setor
        termo_s = None
        if self.list[0] > self.list[1]:  # Comparação entre o primeiro e o segundo
            termo_s = self.list[0]
        else:
            termo_s = self.list[1]
        for j in self.list[2:]:  # Comparaç a partir do terceiro elemento
            if j + termo_f > termo_s:  # Termo que está sendo tratado (j) e valor máximo até agora ou o segundo maior valor até agora
                self.atual = j + termo_f
            else:
                self.atual = termo_s
            termo_f, termo_s = termo_s, self.atual
        return self.atual


setores = int(input())
tcd = list(map(int, input().split()))
final = Arquibancada(tcd)
print(f"{final.max()} torcedores podem ser fotografados.")