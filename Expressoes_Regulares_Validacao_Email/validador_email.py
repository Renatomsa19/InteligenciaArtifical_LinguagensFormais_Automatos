# Atividade pratica - Regex para validar e-mail
# Aluno: Renato

import re

# regex do desafio
padrao = r"[A-Za-z0-9_+-]+(\.[A-Za-z0-9_+-]+)*@([A-Za-z0-9]([A-Za-z0-9-]*[A-Za-z0-9])?\.)+[A-Za-z]{2,}"


def motivo(email):
    if " " in email:
        return "tem espaco"
    if "@" not in email:
        return "nao tem @"
    if email.count("@") > 1:
        return "tem mais de um @"

    usuario, dominio = email.split("@")

    if usuario == "":
        return "nao tem usuario antes do @"
    if usuario.startswith(".") or usuario.endswith("."):
        return "usuario comeca ou termina com ponto"
    if ".." in email:
        return "tem dois pontos seguidos"
    if dominio == "":
        return "nao tem dominio"
    if "." not in dominio:
        return "dominio sem extensao"

    for parte in dominio.split("."):
        if parte.startswith("-") or parte.endswith("-"):
            return "parte do dominio comeca ou termina com hifen"

    if len(dominio.split(".")[-1]) < 2:
        return "extensao com menos de 2 letras"

    return "formato invalido"


validos = []
invalidos = []

for i in range(5):
    email = input("Digite o e-mail " + str(i + 1) + ": ")

    if re.fullmatch(padrao, email):
        validos.append(email)
    else:
        invalidos.append(email)

print("\nE-mails validos:")
for email in validos:
    print(email)

print("\nE-mails invalidos:")
for email in invalidos:
    print(email, "->", motivo(email))
