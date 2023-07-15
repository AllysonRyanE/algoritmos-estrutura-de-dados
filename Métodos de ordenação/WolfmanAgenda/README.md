# Wolfman Agenda

Ao viajar no verão para a casa do seu bom e velho tio Guillhermo Totoro, ele te ensina um antigo jogo desenvolvido nos tempos medievais para crianças passarem o tempo e evitarem caminhar por florestas escuras em busca de aventuras insalubres.

No início da partida, o jogador recebe uma sequência de inteiros e uma constante. A cada rodada, algumas operações devem ser realizadas:

Remover o maior valor da sequência

K = maximo - | minimo * constante |

Se K for maior que zero, insere K na sequência

O jogo deve acabar quando todos os números da sequência forem removidos.

*ATENÇÃO: Usar Heap! Obviamente, é proibido usar comandos como max(), min() e sort().*
## Input

Serão dadas duas linhas de entrada, referentes à sequência de números e à constante.

Exemplo:

5 5 8 11

2


## Output

O retorno do programa deve ser a quantidade de rodadas necessárias para que a partida acabe.

Exemplo:

12 rodadas, partindo para a próxima!

## Exemplos 

Case: 1

### Input

5 5 8 11

2

### Output

12 rodadas, partindo para a próxima!

<hr>

### Input

8 3 4 4 5 5 1 7

2

### Output

21 rodadas, partindo para a próxima!

### Case: 2

### Input

8 3 4 4 5 5 1 7

2

### Output

21 rodadas, partindo para a próxima!