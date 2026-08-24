atividade 24/08

exercício 1:

Σ=a,b,c

Quantos símbolos existem no alfabeto?3
Quais são os símbolos?a, b, c
O símbolo a pertence ao alfabeto? sim
O símbolo d pertence ao alfabeto? nâo
Escreva uma palavra formada por símbolos desse alfabeto. ab. aa. ba...

exercício 2:

Σ=0,1

Classifique cada sequência como palavra válida ou não válida:

Sequência	Válida?	Justificativa
0101		Valida, a palavra 0101 pertence ao alfabeto Σ=0,1
00110		valida, a palavra 00110 pertence ao alfabeto Σ=0,1
012		invalida, não temos o símbolo 2 do palavra 012 no alfabeto Σ=0,1
111		valido, a palavra 111 pertence ao alfabeto Σ=0,1
10a		invalido, não temos o símbolo a no nosso alfabeto Σ=0,1

exercício 3:

Σ=0,1

Determine se as afirmações são verdadeiras ou falsas:

0 ∈ Σ   : verdadeiro, o símbolo 0 pertence a sigma
1 ∈ Σ   : verdadeiro, o símbolo 1 pertence a sigma
01 ∈ Σ  : verdadeiro, 01 pertence ao conjunto de todas as palavras da sigma
01 ∈ Σ∗ : verdadeiro, 01 pertence ao conjunto de todas as palavras da sigma
2 ∈ Σ   : falso, o símbolo 2 não pertence a sigma
101 ∈ Σ∗: verdadeiro, 101 pertence ao conjunto de todas as palavras da sigma

exercício 4:

Determine se cada palavra pertence à linguagem:

0 ∈ L    : 0 pertence à linguagem L
01 ∈ L   : 01 pertence à linguagem L
0111 ∈ L : 0111 pertence à linguagem L
10 ∈ L   : 10 não pertence à linguagem L
111 ∈ L  : 110 não pertence à linguagem L
011 ∈ L  : 011 pertence à linguagem L


exercício 5:

L=bn∣n≥1

Escreva as cinco primeiras palavras. b, bb, bbb, bbbb, bbbbb.
Explique o significado de bn. b elevado a n, exemplo b elevado a 3 = bbb
A palavra bbbbbb pertence à linguagem? sim
A palavra vazia (ε) pertence à linguagem? não 

exercício 6:


Explique, com suas próprias palavras, a diferença entre:

A: L=∅
B: L=ε

Qual delas possui uma palavra? B
Qual delas não possui nenhuma palavra? A
Qual é o comprimento da palavra ε? comprimento zero

exercício 7:

Considere:
G=(S,A,0,1,P,S)

com:
P=S→0A, A→1

O conjunto de variáveis. {S, A}
O conjunto de terminais.{0, 1}
O conjunto de produções. $S \to 0A$$A \to 1$
O símbolo inicial. S
Qual palavra pode ser gerada por essa gramática? 01

exercicio 8:

Considere:
S→0S

Começando com S:

Aplique a regra uma vez. 0S
Aplique a regra duas vezes. 00S
Aplique a regra três vezes. 000S
Escreva a sequência completa de derivação. $$S \Rightarrow 0S \Rightarrow 00S \Rightarrow 000S$$


EXERCICO 9:

Utilizando:

G:{S→aSS→b

gere:
aaab

Escreva todos os passos da derivação.

$$S \Rightarrow aS \Rightarrow aaS \Rightarrow aaaS \Rightarrow aaab$$

EXERCICIO 10:

Considere novamente:
G:{S→0SS→1

Determine se cada palavra pode ser gerada:

1    : Pode, $S \Rightarrow 1$
01   : Pode, $S \Rightarrow 0S \Rightarrow 01$
001  : pode, $S \Rightarrow 0S \Rightarrow 00S \Rightarrow 001$
0001 : pode, $S \Rightarrow 0S \Rightarrow 00S \Rightarrow 000S \Rightarrow 0001$
101  : Não pode ser gerada
1001 : Não pode ser gerada
Para as palavras que podem ser geradas, apresente a derivação completa.
