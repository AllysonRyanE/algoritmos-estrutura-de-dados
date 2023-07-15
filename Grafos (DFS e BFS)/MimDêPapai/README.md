# MIM DÊ PAPAI

Você é o gerente de marketing da Indústria Farinha na Cumbuca e precisa lançar um novo produto nas redes sociais, até que chegue no lobisomem pidão. Para isso, você precisa desenvolver uma estratégia eficiente de distribuição de informações, de forma a atingir o maior número possível de pessoas em um curto período de tempo.

Para elaborar essa estratégia, você precisa entender como funciona a dinâmica de compartilhamento de informações nas redes sociais. Em uma rede social com N usuários (vértices) e M conexões de amizade (arestas), o processo de distribuição de notícias funciona da seguinte maneira:

Um usuário i (1 <= i <= n) recebe a notícia de alguma fonte.
Esse usuário passa a notícia para seus amigos.
Os amigos repassam para seus amigos e assim em diante.
O processo acaba quando não há um par de amigos em que um sabe a notícia e o outro não.
Seu objetivo é determinar a quantidade de usuários que saberiam a notícia se cada usuário i (1 <= i <= n) iniciasse a distribuição. Para isso, você deve desenvolver um algoritmo que receba como entrada n, m e uma lista de conexões entre os usuários, e retorne uma lista com n inteiros, onde o i-ésimo inteiro representa o número de usuários que saberiam a notícia se o usuário i começar distribuindo-a. Utilize a busca em profundidade para verificar todos os nós adjacentes.


## Input

Na primeira linha você vai receber 2 valores N e M , onde N representa o número de usuários e M o número de conexões entre os usuários.

Seguido por X linhas com 2 inteiros U e V representando os usuários conectados.

## Output

Imprima N inteiros. O i-th inteiro deve ser igual ao número de usuários que saberiam a notícia se o usuário i começar distribuindo-a.

## Exemplos

### Case: 1

### Input

7 5

1 7

4 1

3 6

4 6

2 5


### Output

5 2 5 5 2 5 5

### Case: 2

### Input

10 6

9 5

2 7

6 5

4 5

9 6

4 10


### Output

1 2 1 5 5 5 2 1 5 5