#PILHAS
'''DOM = 11
SEG = 22
TER = 33
QUA = 44
QUI = 55
SEX = 66
SAB = 77'''


# Aqui verifica-se a ordem e como retorno das comparações há uma variavél, caso encontre apenas um fator fora de ordem é o suficiente para encerrar o laço
def pilhaOrdenadaCheck(planilha):
    ordem_pri = None
    for x in range(len(planilha) - 1):
        if planilha[x] < planilha[x + 1]:
            ordem_pri = True
        elif planilha[x] > planilha[x + 1]:
            ordem_pri = False
            return ordem_pri
    return ordem_pri  # Essa variavél dirá em bool se a lista está em ordem ou não


def pilhaReserva(planilha, reserva,
                 ordem_loc):  # Além da pilha anterior e a nova locação será usado a variavél que aponta se está a pilha está ordenada ou não
    if ordem_loc:
        for y in range(len(planilha)):
            if reserva < planilha[
                y]:  # Estando em ordem compara-se elemento a elemento até encontrar um menor que a reserva e então o insera em sua posição, deslocando o anterior para frente junto com todos os seus sucessores
                planilha.insert(y, reserva)
                return planilha
    if ordem_loc == False:
        return "A pilha está um caos."


excel = input().split(",")
termo = input()
ordem_glo = pilhaOrdenadaCheck(excel)
print(pilhaReserva(excel, termo, ordem_glo))
