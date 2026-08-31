12. Atividades Práticas — Resolução

Atividade 1 — Prefixos e Sufixos


Palavra considerada: ab

Pergunta:
Liste os prefixos e sufixos.

Resolução:
- Prefixos são todas as subcadeias iniciais da palavra, incluindo a palavra vazia (ε) e a própria palavra.
  - Tamanho 0: ε
  - Tamanho 1: a
  - Tamanho 2: ab
  Conjunto de Prefixos: {ε, a, ab}

- Sufixos são todas as subcadeias finais da palavra, incluindo a palavra vazia (ε) e a própria palavra.
  - Tamanho 0: ε
  - Tamanho 1: b
  - Tamanho 2: ab
  Conjunto de Sufixos: {ε, b, ab}

Atividade 2 — Gramática

Gramática considerada:
G = ({S}, {a}, {S → aS | ε}, S)

Pergunta:
Liste 3 palavras geradas.

Resolução:
A partir do símbolo inicial S e aplicando as regras de produção R = {S → aS, S → ε}:

1. Aplicação direta do fim da recursão:
   S ⇒ ε

2. Uma iteração da regra recursiva:
   S ⇒ aS ⇒ aε ⇒ a

3. Duas iterações da regra recursiva:
   S ⇒ aS ⇒ aaS ⇒ aaε ⇒ aa

Três palavras geradas pela gramática G:
- ε
- a
- aa

(Outras opções válidas seriam: aaa, aaaa, aaaaa, etc.)
