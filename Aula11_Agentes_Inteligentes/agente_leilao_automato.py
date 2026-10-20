"""
Síntese com autômatos — Atividade Agentes Inteligentes (Aula 11)
Disciplina: Inteligência Artificial, Linguagens Formais e Autômatos
Estudante: Renato (Renatomsa19)

Agente de lances em leilão modelado como autômato finito com saída
(máquina de Mealy): estado atual + percepção -> próximo estado e ação.

Estados   : SUPERADO (Q1), LIDERANDO (Q2), ENCERRADO (Q3)
Percepções: p1 rival <= limite, p2 rival > limite, p3 fim do tempo
Ações     : a1 dar lance, a2 arrematar, a3 desistir

Uso:
    python agente_leilao_automato.py            # roda os dois cenários de exemplo
    python agente_leilao_automato.py 350 20     # limite e incremento personalizados
"""

import sys

Q1, Q2, Q3 = "SUPERADO", "LIDERANDO", "ENCERRADO"
P1, P2, P3 = "p1", "p2", "p3"
A1, A2, A3, NADA = "dar lance", "arrematar", "desistir", "-"

# Tabela de transição: (estado, percepção) -> (próximo estado, ação)
TRANSICOES = {
    (Q1, P1): (Q2, A1),  # R1
    (Q1, P2): (Q3, A3),
    (Q1, P3): (Q3, A3),
    (Q2, P1): (Q2, A1),
    (Q2, P2): (Q3, A3),
    (Q2, P3): (Q3, A2),  # R2
    (Q3, P1): (Q3, NADA),
    (Q3, P2): (Q3, NADA),
    (Q3, P3): (Q3, NADA),
}


def brl(valor):
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


class AgenteLeilao:
    """Programa de agente: recebe UMA percepção por vez e guarda só o estado."""

    def __init__(self, limite, incremento):
        self.limite = limite
        self.incremento = incremento
        self.estado = Q1
        self.meu_lance = None

    def perceber(self, evento):
        """Converte o evento bruto do leilão em uma das três percepções."""
        if evento == "fim":
            return P3
        if evento + self.incremento <= self.limite:
            return P1
        return P2

    def agir(self, evento):
        percepcao = self.perceber(evento)
        anterior = self.estado
        self.estado, acao = TRANSICOES[(anterior, percepcao)]
        if acao == A1:
            self.meu_lance = evento + self.incremento
        return percepcao, anterior, acao


def descrever(evento, percepcao):
    if percepcao == P3:
        return "fim do tempo"
    return f"rival deu {brl(evento)}"


def simular(titulo, eventos, limite, incremento):
    agente = AgenteLeilao(limite, incremento)
    print(f"\n=== {titulo} ===")
    print(f"Limite do agente: {brl(limite)} | incremento: {brl(incremento)}")
    print(f"{'passo':>5} | {'percepção':<24} | {'estado -> próximo':<26} | ação")
    print("-" * 5 + "-+-" + "-" * 24 + "-+-" + "-" * 26 + "-+-" + "-" * 26)
    for i, evento in enumerate(eventos, start=1):
        percepcao, anterior, acao = agente.agir(evento)
        texto_acao = acao
        if acao == A1:
            texto_acao = f"dar lance de {brl(agente.meu_lance)}"
        elif acao == A3 and percepcao == P2:
            texto_acao = "desistir (passaria do limite)"
        print(f"{i:>5} | {descrever(evento, percepcao):<24} | "
              f"{anterior:<10} -> {agente.estado:<12} | {texto_acao}")
        if agente.estado == Q3:
            break
    if acao == A2:
        print(f"Resultado: ARREMATOU por {brl(agente.meu_lance)}")
    else:
        ultimo = brl(agente.meu_lance) if agente.meu_lance else "nenhum"
        print(f"Resultado: não arrematou — último lance do agente: {ultimo}")


if __name__ == "__main__":
    if len(sys.argv) == 3:
        limite, incremento = float(sys.argv[1]), float(sys.argv[2])
    else:
        limite, incremento = 300.0, 20.0

    # Cada número é o lance de um rival; "fim" é o cronômetro zerando.
    simular("Cenário 1 — rivais param antes do limite",
            [150, 190, 230, "fim"], limite, incremento)
    simular("Cenário 2 — rival passa do limite",
            [200, 240, 290, "fim"], limite, incremento)
