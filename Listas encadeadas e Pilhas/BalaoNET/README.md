# Balão Net
Você foi contratado pela Balão NET para desenvolver um sistema de histórico de pesquisas em seu mais novo navegador, o "balão_explorer”. Para isso foi requisitada a utilização de uma lista duplamente encadeada para armazenar as pesquisas e também 4 funcionalidades básicas do sistema: busca, remoção, adição e exibição do histórico.

## Input
O programa receberá uma quantidade indefinida de entradas e deverá encerrar quando o comando final “END” for dado . Comandos :

ADD X (X poderá ser qualquer string)

REM X (X poderá ser qualquer string)

EXIB

FIND X (X poderá ser qualquer string , desde que contida na lista)

END

O comando ADD deverá inserir o elemento na sua lista duplamente encadeada

O comando REM deverá remover o elemento na sua lista duplamente encadeada

O comando EXIB deverá printar todo o histórico contido na lista

O comando FIND deverá localizar um elemento já existente na lista e colocá-lo na primeira posição dela

### Exemplo :

lista = d - b - c - a

FIND(“a”)

EXIB

resultado da lista = a - d - b - c

## Output

Após o comando EXIB será imprimido o histórico, exemplo:

site1.com.br

site2.com.br

## Exemplos

### Case: 1

### Input

ADD youtube.com 

ADD como-acabar-com-a-calvice

ADD jogo-do-bixo-como-ganhar?

ADD Dikastis.com.br

ADD Brazino777

FIND Dikastis.com.br

FIND youtube.com

REM Brazino777

EXIB

END

### Output

youtube.com

Dikastis.com.br

jogo-do-bixo-como-ganhar?

como-acabar-com-a-calvice

Case: 2

### Input

ADD 10-motivos-para-acreditar-na-terra-plana

ADD chat-gpt

ADD como-fazer-essa-questão-de-algoritmos

ADD como-ficar-rico-vendendo-brigadeiro

ADD rio-de-fevereiro-existe?

ADD pinguim-tem-joelho?

ADD manoel-gomes-blue-pen

ADD top-10-geladeiras-da-brastemp

FIND manoel-gomes-blue-pen

FIND chat-gpt

FIND como-fazer-essa-questão-de-algoritmos

EXIB

END

### Output

como-fazer-essa-questão-de-algoritmos

chat-gpt

manoel-gomes-blue-pen

top-10-geladeiras-da-brastemp

pinguim-tem-joelho?

rio-de-fevereiro-existe?

como-ficar-rico-vendendo-brigadeiro

10-motivos-para-acreditar-na-terra-plana
