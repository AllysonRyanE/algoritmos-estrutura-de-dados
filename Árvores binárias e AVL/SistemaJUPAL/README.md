# Sistema JUPAL

Depois de tanto exercitar suas habilidades de programação no primeiro período de SI, chegou a hora de cursar a temida matéria de Algoritmos e Estruturas de Dados. Nessa peneira, você sabe que deverá se esforçar ao máximo para conseguir compreender os assuntos passados pelo professor e ainda realizar as atividades práticas no prazo estipulado. No entanto, todos sabem que a vida é uma experiência colaborativa, e para os estudantes isso não é diferente.

Para garantir que você e seus amigos tenham a experiência mais proveitosa possível, vocês decidem criar uma rede de ajuda mútua na qual os membros ajudam uns aos outros a passar pelos desafios que o período propõe. Para isso, você desenvolve um sistema para cadastrar cada um dos participantes dessa organização de maneira a gerenciar qual sua posição na árvore social e quais outros alunos cada um deve ajudar.

O sistema, chamado carinhosamente de JUPAL, possui três funções básicas: buscar, inserir e remover o nome de um integrante. Já no início da implementação do sistema, você percebe que a situação de alguns alunos “do topo” rapidamente se torna insustentável, pois muitas pessoas começam a depender deles, e o sistema se torna desbalanceado. Para agilizar esses processos e garantir a estabilidade emocional de todos os envolvidos, você decide utilizar uma estrutura famosa na engenharia de software que é perfeita para essa situação: a árvore balanceada AVL.

Como você bem sabe, árvores AVL fazem um balanceamento automático de suas folhas todas as vezes que é feita uma inserção ou remoção de maneira a sempre manter a altura de todas mais ou menos igual. Seguindo esse raciocínio, o sistema é capaz de manter todos os integrantes felizes, sem sobrecargas acontecendo de um lado ou de outro da árvore.

## DESCRIÇÃO DA IMPLEMENTAÇÃO

Você deve implementar uma árvore balanceada AVL, com um fator de balanceamento estável, tal que, para todos os nós da árvore: -1 <= f.b. <= 1. Para isso, estipula-se que o fator de balanceamento de cada dado nó é definido como: f.b(Nó) = altura(Nó->direita) - altura(Nó->esquerda). Alguns pontos importantes:

A altura de um nó nulo é dada como 0;
A altura de uma folha é 1;
A altura de um nó qualquer é o valor máximo entre a altura do nó a sua direita e do nó a sua esquerda, somado 1.
Cada aluno da sua árvore deverá ser representado por uma string que corresponde ao seu nome, e a ordenação dos nós deverá seguir a prioridade padrão de strings (alfabética, lexicográfica).

## Input

Seu programa deverá ler entradas repetidamente até que o comando FIM seja chamado. A lista de comandos possíveis é a seguinte:

• INSERIR nome : Insere um nó com o valor nome

• DELETAR nome : Deleta um nó com o valor nome

• MINIMO : Retorna a string com o menor valor lexicográfico

• MAXIMO : Retorna a string com o maior valor lexicográfico

• ALTURA : Retorna a altura total da árvore, partindo da raiz

• FIM : Finaliza o programa

## Output

Cada comando da lista anterior terá um retorno específico, como a seguir:

• INSERIR nome:

Caso nome não exista na árvore: nome INSERIDO

Caso nome já exista na árvore: nome JA EXISTE

• DELETAR nome:

Caso nome exista na árvore: nome DELETADO

Caso nome não exista na árvore: nome NAO ENCONTRADO

• MINIMO:

Caso a árvore não esteja vazia: MENOR: nome

Caso a árvore esteja vazia: ARVORE VAZIA

• MAXIMO:

Caso a árvore não esteja vazia: MAIOR: nome

Caso a árvore esteja vazia: ARVORE VAZIA

• ALTURA:

ALTURA: alturadaarvore

• FIM:

Caso a árvore não esteja vazia: <lista dos nós restantes da árvore, em ordem>

Caso a árvore esteja vazia: ARVORE VAZIA