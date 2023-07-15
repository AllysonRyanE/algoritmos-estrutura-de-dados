# Navegação Espacial

Imagine que você é um cientista espacial encarregado de organizar o armazenamento de dados em uma nave espacial gigantesca. Sua missão é garantir que as informações sejam acessadas rapidamente em caso de emergência. Para isso, você decide aplicar seus conhecimentos em algoritmos e estruturas de dados para organizar o centro de dados da nave.

A quantidade de espaço disponível na nave irá variar de acordo com o tipo de nave, mas uma coisa é certa - cada espaço pode armazenar apenas um conjunto de dados. Você receberá códigos que representam os dados e terá que distribuí-los de acordo com a seguinte lógica:

X mod N

Onde X é o código do dado e N é o número de espaços disponíveis no centro de dados da nave. Se um espaço já estiver ocupado, você precisará desenvolver um programa que possa encontrar um novo espaço para armazenar os dados.

Sua missão é garantir que os dados na nave espacial estejam armazenados e gerenciados de forma eficiente, para que a nave possa atender suas necessidades de missão com rapidez e precisão.

## COMANDOS:

ADD X -> Adiciona o código do dado X ao seu espaço de memoria correspondente.
SCH D -> Eventualmente você poderá consultar se um dado foi adicionado a memória, para isso você receberá o dado D para consulta.
CAP M -> Você poderá fazer consultas sobre o armazenamento daquele endereço de memória, para isso você receberá M representando o número de memória que precisará informar sua disponibilidade armazenamento.

## Input

Inicialmente teremos um valor N, o N informará a quantidade de espaços de memoria que o data center tem.

N

Logo em seguida, será dado um C informando quantos comandos serão executados.

C

Após isso, seguem C linhas com as operações "ADD X", "CAP M" ou "SEARCH D".

Comando 1

Comando 2

...

Comando C

## Output

Quando o dado é adicionado, você deverá imprimir o número da posição da memória no data center: " E: E".

Quando quiser saber consultar se um dado já se encontra armazenado (comando SCH) você devera imprimir "NE" (Quando não for encontrado) ou "E: E" (O endereço que foi encontrado).

Quando quiser saber consultar um espaço de memoria (comando CAP) você deverá imprimir, "D"(Se estiver disponível para armazenar) ou "A: D" (O dado no endereço).

Quando o Data center não tiver mais nenhum endereço de memória disponível, você deverá imprimir "Toda memoria utilizada" e será finalizado o programa.

### Exemplos

## Case: 1

## Input

10

15
 
ADD 25

ADD 79

ADD 62

CAP 9
 
ADD 70

ADD 41

CAP 2

ADD 86

CAP 3

CAP 0

CAP 5

SCH 41

SCH 70

CAP 1

SCH 9

### Output

E: 5

E: 9

E: 2

A: 79

E: 0

E: 1

A: 62

E: 6

D

A: 70

A: 25

E: 1

E: 0

A: 41

NE