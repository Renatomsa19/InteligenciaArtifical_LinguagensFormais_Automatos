# Atividade Prática — Regex para validar e-mail

> **Disciplina:** Inteligência Artificial, Linguagens Formais e Autômatos
> **Material:** *Tutorial — Usando Regex para representar e validar um e-mail* (Profa. Kadidja Valéria, 14/09/2026)
> **Estudante:** Renato (Renatomsa19)

## Arquivos

| Arquivo | Conteúdo |
|---|---|
| [`validador_email.py`](validador_email.py) | Programa da atividade (5 e-mails, válidos × inválidos, motivo de rejeição) + Desafio |

## Como executar

```bash
python validador_email.py          # pede 5 e-mails pelo teclado
python validador_email.py --teste  # roda os casos do tutorial e do desafio automaticamente
```

## Requisitos da atividade × implementação

| # | Requisito | Onde está no código |
|---|---|---|
| 1 | Solicitar cinco endereços | `main()` — `input()` dentro de um laço de 5 repetições |
| 2 | Validar cada endereço com Regex | `validar()` — `re.fullmatch(REGEX_DESAFIO, email)` |
| 3 | Guardar válidos e inválidos separadamente | listas `validos` e `invalidos` |
| 4 | Apresentar os dois grupos | `mostrar()` |
| 5 | Explicar por que cada inválido foi rejeitado | `motivo_rejeicao()` — testa as regras uma a uma e devolve a primeira violada |

## As duas Regex

**Básica (tutorial):**

```regex
[A-Za-z0-9._+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}
```

**Aprimorada (Desafio)** — montada em três partes no código para ficar legível:

```regex
[A-Za-z0-9_+-]+(?:\.[A-Za-z0-9_+-]+)*  @  (?:[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?\.)+  [A-Za-z]{2,}
└──────────── usuário ────────────┘     └──────────── rótulos do domínio ────────────┘   └ extensão ┘
```

| Trecho | O que garante |
|---|---|
| `[A-Za-z0-9_+-]+(?:\.[A-Za-z0-9_+-]+)*` | O ponto **saiu** do conjunto de caracteres e só aparece **entre** dois blocos. Isso impede, ao mesmo tempo, ponto no início, ponto antes do `@` e `..` no usuário. |
| `[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?\.` | Cada parte do domínio começa e termina com letra/número; o hífen só pode ficar no meio. Como cada parte termina em `\.`, `..` no domínio também é rejeitado. |
| `(?: ... )+` | Uma ou mais partes de domínio: aceita `gmail.com` e `udf.edu.br`. |
| `[A-Za-z]{2,}` | Extensão final com pelo menos duas letras. |
| `re.fullmatch` | A Regex precisa casar com o texto **inteiro** (dispensa `^` e `$`). |

**Ideia principal do Desafio:** em vez de "proibir" casos ruins com *lookaheads* (`(?!...)`), a Regex é escrita de forma que os casos ruins **não consigam ser gerados** pela estrutura — o mesmo raciocínio de uma gramática: se não existe regra que produza `..`, a cadeia não pertence à linguagem.

## Saída real (`--teste`)

```text
Regex do Desafio: [A-Za-z0-9_+-]+(?:\.[A-Za-z0-9_+-]+)*@(?:[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?\.)+[A-Za-z]{2,}

### Casos de teste do tutorial

E-mails VÁLIDOS (3):
  [OK] maria@gmail.com
  [OK] joao.silva@udf.edu.br
  [OK] estudante_01@faculdade.com

E-mails INVÁLIDOS (2):
  [X]  pedro.gmail.com                  -> não possui o símbolo @
  [X]  ana@dominio                      -> domínio sem extensão (ex.: .com, .br)

### Casos extras do Desafio

E-mails VÁLIDOS (1):
  [OK] contato+curso@exemplo.com.br

E-mails INVÁLIDOS (10):
  [X]  .renato@gmail.com                -> usuário começa com ponto
  [X]  renato.@gmail.com                -> usuário termina com ponto (ponto imediatamente antes do @)
  [X]  re..nato@gmail.com               -> usuário possui dois pontos consecutivos
  [X]  renato@-udf.edu.br               -> parte do domínio '-udf' começa com hífen
  [X]  renato@udf-.edu.br               -> parte do domínio 'udf-' termina com hífen
  [X]  renato@udf..edu.br               -> domínio possui dois pontos consecutivos
  [X]  renato@gmail.c                   -> extensão possui só uma letra (mínimo 2)
  [X]  @gmail.com                       -> não possui usuário antes do @
  [X]  renato @gmail.com                -> contém espaço
  [X]  renato@udf@edu.br                -> possui mais de um @

Comparação Regex básica x Regex do Desafio
e-mail                           | básica   | desafio 
---------------------------------+----------+---------
maria@gmail.com                  | válido   | válido  
joao.silva@udf.edu.br            | válido   | válido  
estudante_01@faculdade.com       | válido   | válido  
pedro.gmail.com                  | inválido | inválido
ana@dominio                      | inválido | inválido
contato+curso@exemplo.com.br     | válido   | válido  
.renato@gmail.com                | válido   | inválido  <- diferença
renato.@gmail.com                | válido   | inválido  <- diferença
re..nato@gmail.com               | válido   | inválido  <- diferença
renato@-udf.edu.br               | válido   | inválido  <- diferença
renato@udf-.edu.br               | válido   | inválido  <- diferença
renato@udf..edu.br               | válido   | inválido  <- diferença
renato@gmail.c                   | inválido | inválido
@gmail.com                       | inválido | inválido
renato @gmail.com                | inválido | inválido
renato@udf@edu.br                | inválido | inválido
```

As linhas marcadas com `<- diferença` mostram exatamente o que o Desafio corrigiu em relação à Regex básica.

## Relação com Linguagens Formais

A Regex define uma **linguagem regular** *L* sobre o alfabeto dos caracteres do teclado:

```text
E-MAIL  = USUÁRIO · @ · (RÓTULO · .)⁺ · EXTENSÃO
USUÁRIO = BLOCO (· BLOCO)*        BLOCO = [A-Za-z0-9_+-]⁺
RÓTULO  = AN ( [A-Za-z0-9-]* AN )?   AN = [A-Za-z0-9]
EXTENSÃO = [A-Za-z]{2,}
```

Toda linguagem regular é reconhecida por um **autômato finito**. Para essa Regex, um autômato com poucos estados basta: *lendo usuário → leu ponto no usuário → leu @ → lendo rótulo → leu hífen → leu ponto no domínio → lendo extensão*. Validar um e-mail é, portanto, perguntar se a cadeia pertence a *L*.

## Limitações

- A Regex verifica **formato**, não existência: não garante que o domínio esteja registrado nem que a caixa de entrada exista. A confirmação real exige enviar um link/código.
- Não cobre todas as regras da RFC 5322 (por exemplo, usuários entre aspas ou domínios com acentos/IDN). Uma Regex rígida demais pode recusar e-mails válidos e pouco comuns.
- No formulário HTML, o atributo `pattern` ajuda, mas a validação também precisa ser feita no servidor.
