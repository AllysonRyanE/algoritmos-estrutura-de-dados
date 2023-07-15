# Paciência Infinita

Chegada a segunda-feira, cinco estagiários da biblioteca imaginária do CIn foram encarregados de ordenar os novos livros disponibilizados pela reitoria do campus para decorar as prateleiras da instituição com infinito conhecimento.

Sendo cada um deles uma entidade incorpórea, uma inteligência artificial, um figmento de insônia, eles resolvem criar uma competição que analisa qual o método mais eficiente para ordenar cada pilha, através de algoritmos diferentes que foram estudados na matéria IF969.

O primeiro estagiário, Caça-Rato, irá executar o método Bubble Sort.
O segundo estagiário, Grafite, irá executar o método Selection Sort.
O terceiro estagiário, Lacraia, irá executar o método Insertion Sort.
O quarto estagiário, Rivaldo, irá executar o método Shell Sort.
O quinto estagiário, Toninho, irá executar o método Quicksort (Hoare partition).
Para cada rodada da competição, os estagiários devem ordenar a mesma pilha de livros com o método delegado a eles, contando a quantidade de vezes que eles fazem uma comparação entre dois livros e a quantidade de vezes que eles trocam a posição de dois livros. Ao final da rodada, é definido o vencedor da rodada de acordo com a quantidade total de ações realizadas (comparações + trocas) para ordenar a pilha.

Após isso, os estagiários mais lentos tentam novamente ordenar a pilha, mas executando apenas a quantidade de ações que foram necessárias para o vencedor concluir a tarefa. Toninho, no entanto, não estava muito disposto a participar dessa etapa, então decidiu ficar de fora.

## Input

Para facilitar minha vida, os livros serão representados por números inteiros.

O código terá apenas uma linha de input, uma string de números únicos (sem repetições) separados por um espaço.

Exemplo:
4 5 8 7 14 2 3 6 21 32 52 0 2156 23

## Output

Na primeira etapa, deve ser retornado o resultado da ordenação da seguinte maneira para cada um dos estagiários:

<nomeEstagiário&gt; ordena a lista com <númeroComp&gt; comparações e <númeroTrocas&gt; trocas.

Após os cinco estagiários realizarem suas tarefas, devem ser retornado o nome do vencedor:

"-VENCEDOR DA RODADA-"

O vencedor da rodada é <nomeEstagiário&gt;, com <númeroAções&gt; ações.

Para a segunda etapa, lembre-se que Toninho não irá participar, então:

Os outros estagiários retornam as seguintes listas com essa quantidade de ações:

-Toninho está a dormir...-

Com <númeroAções&gt; ações <nomeEstagiário&gt; ordena a lista assim: <listaInterrompida&gt; para cada um dos outros 4 estagiários (menos o vencedor, caso ele esteja entre os quatro).

## Exemplo:

### Case 1:
### Input:

863 399 632 305 599 943 244 859 893 564

### Output:

Caça-Rato ordena a lista com 45 comparações e 22 trocas.
Grafite ordena a lista com 45 comparações e 6 trocas.
Lacraia ordena a lista com 28 comparações e 22 trocas.
Rivaldo ordena a lista com 32 comparações e 16 trocas.
Toninho ordena a lista com 27 comparações e 17 trocas.
-VENCEDOR DA RODADA-
O vencedor da rodada é Toninho, com 44 ações.
-Toninho está a dormir...-
Os outros estagiários retornam as seguintes listas com essa quantidade de ações:
Com 44 ações, Caça-Rato ordena a lista assim: [305, 399, 244, 599, 632, 859, 564, 863, 893, 943]
Com 44 ações, Grafite ordena a lista assim: [244, 305, 399, 564, 599, 632, 863, 859, 893, 943]
Com 44 ações, Lacraia ordena a lista assim: [244, 305, 399, 599, 632, 859, 863, 863, 893, 943]
Com 44 ações, Rivaldo ordena a lista assim: [244, 305, 399, 564, 599, 632, 863, 859, 893, 943]

### Case: 2
### Input

48 53 156 225 240 253 286 315 341 401 436 501 559 572 680 696 760 767 959 993

### Output
Caça-Rato ordena a lista com 190 comparações e 0 trocas.
Grafite ordena a lista com 190 comparações e 0 trocas.
Lacraia ordena a lista com 19 comparações e 0 trocas.
Rivaldo ordena a lista com 62 comparações e 0 trocas.
Toninho ordena a lista com 69 comparações e 19 trocas.
-VENCEDOR DA RODADA-
O vencedor da rodada é Lacraia, com 19 ações.
-Toninho está a dormir...-
Os outros estagiários retornam as seguintes listas com essa quantidade de ações:
Com 19 ações, Caça-Rato ordena a lista assim: [48, 53, 156, 225, 240, 253, 286, 315, 341, 401, 436, 501, 559, 572, 680, 696, 760, 767, 959, 993]
Com 19 ações, Grafite ordena a lista assim: [48, 53, 156, 225, 240, 253, 286, 315, 341, 401, 436, 501, 559, 572, 680, 696, 760, 767, 959, 993]
Com 19 ações, Rivaldo ordena a lista assim: [48, 53, 156, 225, 240, 253, 286, 315, 341, 401, 436, 501, 559, 572, 680, 696, 760, 767, 959, 993]

### Case: 3

### Input
9 8 7 6 5 4 3 2 1 0

### Output
Caça-Rato ordena a lista com 45 comparações e 45 trocas.
Grafite ordena a lista com 45 comparações e 5 trocas.
Lacraia ordena a lista com 45 comparações e 45 trocas.
Rivaldo ordena a lista com 27 comparações e 13 trocas.
Toninho ordena a lista com 25 comparações e 14 trocas.
-VENCEDOR DA RODADA-
O vencedor da rodada é Toninho, com 39 ações.
-Toninho está a dormir...-
Os outros estagiários retornam as seguintes listas com essa quantidade de ações:
Com 39 ações, Caça-Rato ordena a lista assim: [6, 5, 7, 4, 3, 2, 1, 0, 8, 9]
Com 39 ações, Grafite ordena a lista assim: [0, 1, 2, 3, 5, 4, 6, 7, 8, 9]
Com 39 ações, Lacraia ordena a lista assim: [4, 5, 6, 6, 7, 8, 9, 2, 1, 0]
Com 39 ações, Rivaldo ordena a lista assim: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
