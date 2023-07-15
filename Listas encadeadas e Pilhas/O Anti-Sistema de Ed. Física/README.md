# O Anti-Sistema de Ed. Física

Não é fácil ser estagiário administrativo do departamento de educação física. Apesar dos seus melhores esforços, o setor no qual você trabalha é muito pouco capacitado tecnologicamente, e ao invés de criarem um sistema online para a locação de espaços e equipamentos todo esse controle ainda é feito a mão, em planilhas de papel em pilhas que só crescem, e são horríveis de manusear.

Em todas as ocasiões que você recebe uma solicitação de locação de um espaço, você deve manualmente receber o documento e alinhá-lo corretamente na pilha da semana, em um tempo curto para que não cause mais estresse no seu chefe. A pilha é organizada sequencialmente, com os compromissos mais próximos no início.

Cada locação possui um código numérico de 6 dígitos que se refere ao seu dia e horário de início, de maneira que a pilha é ordenada como em uma série comum de inteiros:

Domingo = 11

Segunda = 22

Terça = 33

…

Sábado = 77

Os horários seguem o mesmo padrão, começando da manhã até a noite:

6 da manhã = 0600

6 e meia da manhã = 0630

…

11 da noite = 2300

11 e meia da noite = 2330

No entanto, além de colocar novas locações nos lugares corretos do registro, você também tem que lidar com o estresse de que, às vezes, alguns professores tentam fazer isso sozinhos e acabam bagunçando a pilha, tirando tudo da ordem que você tinha tão meticulosamente mantido.

**Nesse contexto, desenvolva uma função novaLocacao(pilha, codigo) que adiciona, em tempo O(n) o valor inteiro ‘codigo’ na sua posição apropriada da pilha ‘pilha’ (vetor), se a pilha estiver ordenada. A função deve retornar um novo vetor com a nova locação adicionada. Mas, atenção, antes disso você deve executar uma função pilhaImaculada(pilha) que checa em tempo O(n) se ela estava na ordem certa, antes de fazer a inserção.**

## Input

A entrada do programa é composta por duas linhas. A primeira representa o vetor que se refere à pilha de solicitações, com números inteiros (códigos de locação) separados por vírgula e sem espaço, no formato a,b,c. A segunda linha é o código da nova locação, que é um inteiro simples que deverá ser inserido na lista, se esta estiver ordenada.

## Output

Você deve produzir uma única linha de saída. Caso a pilha tenha sido encontrada ordenada e a nova solicitação tenha sido inserida nela, deve-se imprimir a nova pilha de solicitações, no mesmo formato da entrada (['a','b','c']). Caso a pilha tenha sido encontrada desordenada, imprima a expressão “A pilha está um caos.”.

# Exemplos

## Case: 1

Input:
110600,110730,221830,221900,331100,331130,441900
222100

Output:
['110600', '110730', '221830', '221900', '222100', '331100', '331130', '441900']

## Case: 2

Input:
110600,551600,110730,221830,221900,331100,331130,441900
222100

Output:
A pilha está um caos.