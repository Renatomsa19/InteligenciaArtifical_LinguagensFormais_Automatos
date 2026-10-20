# Atividade Pratica - Regex para validar e-mail

Disciplina: Inteligência Artificial, Linguagens Formais e Autômatos
Aluno: Renato

O programa `validador_email.py` pede 5 e-mails, valida com regex, separa os válidos e inválidos e mostra o motivo de cada inválido.

Para rodar:

```
python validador_email.py
```

## Regex usada (desafio)

```
[A-Za-z0-9_+-]+(\.[A-Za-z0-9_+-]+)*@([A-Za-z0-9]([A-Za-z0-9-]*[A-Za-z0-9])?\.)+[A-Za-z]{2,}
```

- antes do @: letras, números, `_`, `+` e `-`. O ponto só pode ficar no meio, então não deixa ponto no começo, antes do @ ou dois pontos seguidos
- depois do @: cada parte do domínio começa e termina com letra ou número, o hífen só no meio
- no final a extensão precisa ter pelo menos 2 letras

## Testes

Teste 1 (casos do tutorial):

```
E-mails validos:
maria@gmail.com
joao.silva@udf.edu.br
estudante_01@faculdade.com

E-mails invalidos:
pedro.gmail.com -> nao tem @
ana@dominio -> dominio sem extensao
```

Teste 2 (casos do desafio):

```
E-mails validos:
contato+curso@exemplo.com.br

E-mails invalidos:
.renato@gmail.com -> usuario comeca ou termina com ponto
re..nato@gmail.com -> tem dois pontos seguidos
renato@-udf.edu.br -> parte do dominio comeca ou termina com hifen
renato@gmail.c -> extensao com menos de 2 letras
```

## Limitações

A regex só verifica o formato, não sabe se o e-mail existe de verdade. Para isso teria que mandar um código de confirmação.
