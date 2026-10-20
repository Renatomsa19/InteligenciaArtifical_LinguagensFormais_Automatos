"""
Atividade Prática — Usando Regex para representar e validar um e-mail
Disciplina: Inteligência Artificial, Linguagens Formais e Autômatos
Estudante: Renato (Renatomsa19)

O programa:
  1. solicita cinco endereços de e-mail;
  2. valida cada um com uma Regex;
  3. guarda separadamente os válidos e os inválidos;
  4. mostra os dois grupos ao final;
  5. explica por que cada entrada inválida foi rejeitada.

Também compara a Regex básica do tutorial com a Regex aprimorada do Desafio.

Uso:
    python validador_email.py          # digita os 5 e-mails
    python validador_email.py --teste  # usa os casos de teste do tutorial + desafio
"""

import re
import sys

# Regex do tutorial (versão didática)
REGEX_BASICA = r"[A-Za-z0-9._+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

# Regex do Desafio, montada por partes para ficar legível
PARTE_USUARIO = r"[A-Za-z0-9_+-]+(?:\.[A-Za-z0-9_+-]+)*"   # ponto só ENTRE blocos
ROTULO_DOMINIO = r"[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?"  # sem hífen nas pontas
EXTENSAO = r"[A-Za-z]{2,}"
REGEX_DESAFIO = rf"{PARTE_USUARIO}@(?:{ROTULO_DOMINIO}\.)+{EXTENSAO}"

CASOS_TUTORIAL = [
    "maria@gmail.com",
    "joao.silva@udf.edu.br",
    "estudante_01@faculdade.com",
    "pedro.gmail.com",
    "ana@dominio",
]

CASOS_DESAFIO = [
    "contato+curso@exemplo.com.br",
    ".renato@gmail.com",
    "renato.@gmail.com",
    "re..nato@gmail.com",
    "renato@-udf.edu.br",
    "renato@udf-.edu.br",
    "renato@udf..edu.br",
    "renato@gmail.c",
    "@gmail.com",
    "renato @gmail.com",
    "renato@udf@edu.br",
]


def motivo_rejeicao(email):
    """Explica, em português, a primeira regra que o e-mail viola."""
    if email.strip() == "":
        return "entrada vazia"
    if " " in email:
        return "contém espaço"
    if email.count("@") == 0:
        return "não possui o símbolo @"
    if email.count("@") > 1:
        return "possui mais de um @"

    usuario, dominio = email.split("@")

    if usuario == "":
        return "não possui usuário antes do @"
    if usuario.startswith("."):
        return "usuário começa com ponto"
    if usuario.endswith("."):
        return "usuário termina com ponto (ponto imediatamente antes do @)"
    if ".." in usuario:
        return "usuário possui dois pontos consecutivos"
    if re.search(r"[^A-Za-z0-9._+-]", usuario):
        return "usuário possui caractere não permitido"

    if dominio == "":
        return "não possui domínio depois do @"
    if "." not in dominio:
        return "domínio sem extensão (ex.: .com, .br)"
    if ".." in dominio:
        return "domínio possui dois pontos consecutivos"

    *rotulos, extensao = dominio.split(".")
    for rotulo in rotulos:
        if rotulo.startswith("-"):
            return f"parte do domínio '{rotulo}' começa com hífen"
        if rotulo.endswith("-"):
            return f"parte do domínio '{rotulo}' termina com hífen"
    if not re.fullmatch(r"[A-Za-z]+", extensao):
        return "extensão deve conter apenas letras"
    if len(extensao) < 2:
        return "extensão possui só uma letra (mínimo 2)"

    return "formato não reconhecido pela Regex"


def validar(emails, padrao):
    validos, invalidos = [], []
    for email in emails:
        if re.fullmatch(padrao, email):
            validos.append(email)
        else:
            invalidos.append((email, motivo_rejeicao(email)))
    return validos, invalidos


def mostrar(validos, invalidos):
    print(f"\nE-mails VÁLIDOS ({len(validos)}):")
    for email in validos:
        print(f"  [OK] {email}")
    print(f"\nE-mails INVÁLIDOS ({len(invalidos)}):")
    for email, motivo in invalidos:
        print(f"  [X]  {email:<32} -> {motivo}")


def comparar(emails):
    """Mostra lado a lado o resultado da Regex básica e da Regex do Desafio."""
    print("\nComparação Regex básica x Regex do Desafio")
    print(f"{'e-mail':<32} | {'básica':<8} | {'desafio':<8}")
    print("-" * 32 + "-+-" + "-" * 8 + "-+-" + "-" * 8)
    for email in emails:
        b = "válido" if re.fullmatch(REGEX_BASICA, email) else "inválido"
        d = "válido" if re.fullmatch(REGEX_DESAFIO, email) else "inválido"
        marca = "  <- diferença" if b != d else ""
        print(f"{email:<32} | {b:<8} | {d:<8}{marca}")


def main():
    if "--teste" in sys.argv:
        print("Regex do Desafio:", REGEX_DESAFIO)
        print("\n### Casos de teste do tutorial")
        mostrar(*validar(CASOS_TUTORIAL, REGEX_DESAFIO))
        print("\n### Casos extras do Desafio")
        mostrar(*validar(CASOS_DESAFIO, REGEX_DESAFIO))
        comparar(CASOS_TUTORIAL + CASOS_DESAFIO)
        return

    emails = [input(f"Digite o {i}º e-mail: ").strip() for i in range(1, 6)]
    mostrar(*validar(emails, REGEX_DESAFIO))


if __name__ == "__main__":
    main()
