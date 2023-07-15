# Café Pass

O Centro de Informática estava enfrentando um problema sério com a cafeteira de sua sala de convivência. Alguns alunos estavam consumindo quantidades excessivas de café, deixando pouco para os demais. Para resolver o problema, o time de desenvolvimento do Helpdesk CIn-UFPE, liderado por Charles do Helpdesk, decidiu criar um sistema de autorização experimental chamado "CaféPass" para validar se uma aluna(o) pode acessar a cafeteira da sala de convivência na semana.

## Funcionamento:

Toda Segunda o sistema carrega CPFs dos alunos e forma um array a partir de seus dígitos multiplicado por 10 :

ex.: 72290379050 => [70, 20, 20, 90, 0, 30, 70, 90, 0, 50, 0]

Caso o CPF tenha dígitos repetidos, então deve-se reduzir esse array somando os valores duplicados:

ex.: [70, 20, 20, 90, 0, 30, 70, 90, 0, 50, 0] => [140, 40, 180, 0, 30, 50]

Por último, é gerado um número aleatório (Magic Number) entre 30 e 990 para cada CPF. Dessa forma, se a soma de dois elementos distintos do array final for igual ao número aleatório, então a aluna(o) ganha permissão de acessar a sala de convivência para usar a cafeteira na semana.

Pode usar lista (Python List)
Não pode usar dicionário (Python dict)
Atenção com o uso excessivo de trechos com O(nˆ2)
Obrigatório usar Tabela Hash

## Input

N - Onde N é o número de operações da entrada

Várias linhas com a seguinte informação:

CPF MN - Calcula autorização considerando um CPF e um (magic number) MN.

Limites de Input

len(CPF) = 11
30 <= MN <= 990

## Output

RESPONSE - Onde pode ser UP Permission se o usuário receber a permissão ou NOT Permission, caso não esteja autorizado na semana.

## Exemplos

### Case: 1

### Input

34

91768586847 840

90602345231 610

54233491316 920

95530921533 380

26895832721 230

86210927981 90

11267567802 530

71672503009 950

82624173631 410

36495538311 420

81378912222 350

63474328094 750

09640259658 580

37352571409 900

16295125542 370

28790746481 980

23821750530 120

50609853551 610

96388978882 90

01548336519 110

28305723908 520

04883397671 310

89098505430 560

88205872558 390

64237721813 790

62810522551 560

88618387558 690

05402172033 930

97729901249 180

36537587624 280

36841748254 760

70746441091 390

02740802454 470

20283942340 280

### Output

NOT Permission

NOT Permission

NOT Permission

NOT Permission

UP Permission

UP Permission

NOT Permission

NOT Permission

NOT Permission

NOT Permission

NOT Permission

NOT Permission

NOT Permission

NOT Permission

NOT Permission

NOT Permission

UP Permission

NOT Permission

UP Permission

UP Permission

NOT Permission

NOT Permission

NOT Permission

UP Permission

NOT Permission

NOT Permission

NOT Permission

NOT Permission

UP Permission

NOT Permission

NOT Permission

NOT Permission

NOT Permission

NOT Permission
