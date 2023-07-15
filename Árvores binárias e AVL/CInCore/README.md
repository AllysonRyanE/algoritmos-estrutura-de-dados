# CIN CORE

Os processadores modernos utilizam vários níveis de cache para acelerar o acesso à memória RAM. Esses caches armazenam as informações mais utilizadas pelo processador, favorecendo consultas a posições de memória que se repetem durante a execução de um processo. Isso diminui a latência média entre o processador e a memória RAM, melhorando significativamente o desempenho geral do sistema.

O processador CIn Core é um exemplo de processador que possui essa característica e utiliza uma estrutura de dados reativa a consultas repetitivas, ou seja, quanto mais um dado é requisitado, mais fácil é obtê-lo, pois ele estará armazenado em um dos níveis de cache do processador. Isso reduz ainda mais a latência e melhora a velocidade de processamento. Como entusiasta de processadores, você deseja explicar essa tecnologia para seus amigos Matheus, Isabelle e Arthur, para que eles entendam como ela pode melhorar o desempenho de seus sistemas.

Para conseguir explicar aos seus amigos, você chega a conclusão que o melhor a ser feito é utilizar uma estrutura de árvore, onde a cada consulta na estrutura além da entrega de dados o dado consultado deve ir para o topo. No trecho abaixo, pode-se observar o nó de valor 5 subindo na árvore.

## Observações:

1: A entrada não terá elementos repetidos.

2: A estrutura a ser utilizada é a árvore de busca binária.

3: Não é permitido o uso de bibliotecas.

## Input

Várias linhas com as seguintes operações:

ADD V - Adiciona um valor V na estrutura.

SCH V - Procura pelo valor V na estrutura.

## Output

Para a operação de ADD:

CL(current level) - Onde CL representa o nível em que o dado V foi inserido.
Para a operação de SCH:

PL(previous level) - Onde PL representa em que nível o dado V estava antes de ir para o topo ou -1 caso o valor não exista na estrutura.


# Examples

## Case: 1

### Input

ADD 165544
ADD 11623
SCH 165544
SCH 165544
SCH 11623

### Output

0
1
0
0
1

## Case: 2

### Input

ADD 100
ADD 50
ADD 25
ADD 10
SCH 10
SCH 55
SCH 50
SCH 50

### Output

0
1
2
3
3
-1
2
0