# Atividade Agentes Inteligentes - sintese com automatos
# Agente de leilao

transicoes = {
    ("SUPERADO", "p1"): ("LIDERANDO", "dar lance"),
    ("SUPERADO", "p2"): ("ENCERRADO", "desistir"),
    ("SUPERADO", "p3"): ("ENCERRADO", "desistir"),
    ("LIDERANDO", "p1"): ("LIDERANDO", "dar lance"),
    ("LIDERANDO", "p2"): ("ENCERRADO", "desistir"),
    ("LIDERANDO", "p3"): ("ENCERRADO", "arrematar"),
}


def simular(lances_rivais, limite, incremento):
    estado = "SUPERADO"
    meu_lance = 0

    print("Limite:", limite, "| Incremento:", incremento)

    for lance in lances_rivais:
        if lance == "fim":
            percepcao = "p3"
        elif lance + incremento <= limite:
            percepcao = "p1"
        else:
            percepcao = "p2"

        anterior = estado
        estado, acao = transicoes[(estado, percepcao)]

        if acao == "dar lance":
            meu_lance = lance + incremento

        print(lance, "|", percepcao, "|", anterior, "->", estado, "|", acao)

        if estado == "ENCERRADO":
            break

    if acao == "arrematar":
        print("Arrematou por", meu_lance)
    else:
        print("Nao arrematou")
    print()


simular([150, 190, 230, "fim"], 300, 20)
simular([200, 240, 290, "fim"], 300, 20)
