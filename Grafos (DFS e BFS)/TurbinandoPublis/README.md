# Turbinando Publicações

Dado uma rede social com N usuários, quando um usuário faz uma publicação, a mensagem alcança seus seguidores imediatos e, em seguida, os seguidores dos seus seguidores, ou seja, o alcance na rede é medido em largura. Para calcular quantos seguidores essa publicação pode alcançar, é necessário pagar um "boost" para chegar aos seguidores dos seguidores.

Por exemplo, se um usuário tem 3 seguidores e cada um deles tem 2 seguidores, a publicação chegará aos seus 3 seguidores diretos gratuitamente, mas para chegar aos seguidores dos seguidores será necessário pagar um "boost". O custo do "boost" é calculado por uma função que multiplica a quantidade de seguidores que deseja alcançar por R$5,25.

Se o usuário deseja alcançar mais 3 usuários fora do seu nível de seguidores, ele precisará pagar por 3 x R$5,25 = R$15,75 para que a publicação alcance esses seguidores. Caso o usuário tenha apenas R$15,00 para investir, a publicação alcançará apenas os seguidores imediatos dos seus seguidores.

O exemplo de cima de forma ilustrada:

alaaa

OBS: É proibido utilizar qualquer biblioteca.

## Input

N - Onde N é o número de usuários na rede social

U - Onde U é o id do user

B - Onde B é o valor investido em boost

Em seguida: Várias linhas com a representação da relação de seguidores dos usuários da rede social:

ID s[] - ID do usuário + ID dos seguidores

## Output

[Usuários atingidos] - Lista com o ID dos seguidores alcançados

## Exemplos
### Case: 1

### Input

17

0

16

0 : 6 8 4

1 : 5 4 14 9 0 3 2

2 : 6 5 4 12 14 1 11 8

3 : 1 14 16 9 3 15

4 : 3 6 16

5 : 14 8 5

6 : 15 13 4 0

7 : 5 4 16 13 2

8 : 5 14 1 10 0 3 11 7

9 : 4 12 1 10 0 3 11 8 2 7

10 : 4 12 1 3 8 7

11 : 5 14 1 0 3 8

12 : 9 2 7

13 : 5 4 12 14 1 10 16 0 15 11

14 : 4 13 9 3 15 8 7

15 : 6 5 14 1 9 0 3 7

16 : 5 4 1 16 13 3 7


### Output

['6', '8', '4', '15', '13', '5']

### Case: 2

### Input

41

30

158

0 : 11 21 27

1 : 3 28 29 15 19 38 35

2 : 15 21 40 18 1

3 : 12 13 40 36 6 19 39 5 23 22 4

4 : 29 21 18 17 33 19 38 37 35 9

5 : 12 18 17 37 9 30 14 4

6 : 1 27

7 : 27 15 40 39 36 33 6 21 1 26

8 : 29 14 3

9 : 32 15 11 18 38 37 22

10 : 13 17 33 38 14 9

11 : 0 13 10 18 33

12 : 9 30

13 : 1 4 33

14 : 32 3 7 0 10 36 17 26

15 : 36 20 28

16 : 31 7 25 19 2 5

17 : 24 4 26

18 : 27 15 21 39 2 9

19 : 12 37 5 23 14 4

20 : 32 11 0 21 13 1 35 16 14

21 : 12 15 13 19 38 2

22 : 27 0 15 11 13 40 6 24 30

23 : 20 13 37 5 14 22

24 : 2 34 13 18

25 : 27 28 29 0 24 5 26 30

26 : 8 0 21 40 33 19 6 16 30 14 4

27 : 31 7 0 15 40 37 23 16

28 : 31 32 12 10 38 37 2 35 24 22

29 : 3 7 11 17 33 1 24 23 30 22

30 : 25 29 39 33 2 34

31 : 29 22 6

32 : 3 21 2 37 24 26 9

33 : 31 3 8 12 29 15 18 36 35 26 30 34

34 : 15 18 39 36 35 5 26 9

35 : 7 20 23 30 14 22

36 : 28 21 40 22 4

37 : 15 40 24

38 : 32 12 40 13 17 6 2 37 16 22

39 : 8 28 29 10 35 14 9

40 : 31 15 27


### Output

['25', '29', '39', '33', '2', '34', '27', '28', '0', '24', '5', '26', '3', '7', '11', '17', '1', '23', '22', '8', '10', '35', '14', '9', '31', '12', '15', '18', '36', '21', '40', '37', '16', '32', '38', '13']