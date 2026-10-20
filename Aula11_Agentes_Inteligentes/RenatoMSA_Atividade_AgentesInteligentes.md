# Atividade — Agentes Inteligentes (Capítulo 2)

> **Disciplina:** Inteligência Artificial, Linguagens Formais e Autômatos
> **Aula:** 19/10/2026 · **Professora:** Kadidja Valéria · **Instituição:** UDF
> **Estudante:** Renato (Renatomsa19) · **Turma:** _[preencher]_
> **Material-base:** Russell & Norvig — Capítulo 2, *Agentes inteligentes*

Resolução dos exercícios 2.3, 2.4 e 2.5, seguida da síntese com autômatos. Junto deste arquivo está o script [`agente_leilao_automato.py`](agente_leilao_automato.py), que **executa** o autômato descrito na síntese.

---

## Sumário

1. [Exercício 2.3 — Verdadeiro ou falso](#exercício-23--verdadeiro-ou-falso)
2. [Exercício 2.4 — PEAS e propriedades dos ambientes](#exercício-24--peas-e-propriedades-dos-ambientes)
3. [Quadro-resumo das classificações](#quadro-resumo-das-classificações)
4. [Comparação final](#comparação-final)
5. [Exercício 2.5 — Conceitos](#exercício-25--conceitos)
6. [Síntese com autômatos](#síntese-com-autômatos)
7. [Referências](#referências)

---

## Exercício 2.3 — Verdadeiro ou falso

> Lembrete usado em todas as respostas: um agente é **racional** quando, para cada sequência de percepções, escolhe a ação que **maximiza o desempenho esperado**, dado o que percebeu e o conhecimento prévio que possui. Racional ≠ onisciente ≠ sempre vitorioso.

### a. Um agente que detecta apenas informações parciais sobre o estado não pode ser perfeitamente racional.

- **Julgamento:** **F**
- **Hipóteses:** a medida de desempenho é avaliada em *valor esperado*; o agente conhece as probabilidades relevantes do jogo.
- **Justificativa:** a definição de racionalidade não exige ver o estado inteiro; exige fazer o melhor possível **com o que foi percebido**. Se o agente usa corretamente a informação parcial que tem, ele é perfeitamente racional — o que ele não é, é onisciente.
- **Contraexemplo:** um agente que joga **truco** não vê as cartas do adversário, mas pode escolher quando pedir truco ou correr com base nas cartas que tem na mão, nas que já saíram e no comportamento do oponente. Essa política pode ser a melhor possível dadas as percepções.

### b. Existem ambientes de tarefa nos quais nenhum agente reativo puro pode comportar-se racionalmente.

- **Julgamento:** **V**
- **Hipóteses:** ambiente parcialmente observável, em que **a mesma percepção** aparece em situações que exigem ações diferentes.
- **Justificativa:** o agente reativo puro é uma tabela *percepção atual → ação*. Se duas situações diferentes geram a mesma percepção, ele é obrigado a responder igual nas duas, e portanto erra em pelo menos uma.
- **Exemplo:** um robô num **labirinto com dois corredores idênticos**: em ambos o sensor lê "parede à frente, passagem à direita". Num deles o certo é virar à direita; no outro, virar à direita leva de volta ao início. Sem memória do caminho já feito, o robô entra em ciclo — e nenhuma tabela reativa resolve os dois casos ao mesmo tempo.

### c. Existe um ambiente de tarefa em que todo agente é racional.

- **Julgamento:** **V**
- **Hipóteses:** a medida de desempenho atribui **o mesmo valor** a qualquer sequência de estados que o agente possa produzir.
- **Justificativa:** se todas as ações levam ao mesmo desempenho, então qualquer ação maximiza o desempenho esperado. Logo, qualquer agente (mesmo um que não faça nada) é racional nesse ambiente. É um caso degenerado, mas existe.
- **Exemplo:** um "jogo" em que o agente escolhe a cor de um LED de um painel que ninguém olha e cuja pontuação é sempre 0, seja qual for a cor.

### d. A entrada para o programa de agente é a mesma que a entrada para a função de agente.

- **Julgamento:** **F**
- **Hipóteses:** definições do livro — função de agente *f : P\* → A*; programa de agente roda em ciclos sobre a arquitetura.
- **Justificativa:** a **função** é um objeto matemático que recebe **toda a sequência de percepções** até o instante. O **programa** recebe, a cada ciclo, **só a percepção atual**; se precisar do passado, ele mesmo tem que guardar (estado interno).
- **Exemplo:** num termostato inteligente, a função seria "dado o histórico [22 °C, 24 °C, 26 °C] → ligar o ar". O programa, no último ciclo, recebe apenas "26 °C" e consulta a variável onde guardou que a temperatura vinha subindo.

### e. Toda função de agente é implementável por uma combinação de programa/máquina.

- **Julgamento:** **F**
- **Hipóteses:** "programa/máquina" = procedimento computável executado em uma arquitetura física, com memória finita.
- **Justificativa:** uma função de agente é qualquer mapeamento de sequências para ações; nada impede de definir mapeamentos **não computáveis**. Além disso, a arquitetura real tem memória finita, o que já impede implementar funções que exigem contar sem limite.
- **Contraexemplos:**
  1. Função "dada a sequência de percepções que descreve um programa, responda *parar* se ele termina e *continuar* se ele roda para sempre" → é o **problema da parada**, que nenhuma Máquina de Turing decide.
  2. Ligação com Linguagens Formais: a função "responda *aceitar* se a sequência de percepções até agora tem a forma **aⁿbⁿ**" exige contar sem limite; **nenhum autômato finito** (uma máquina de memória finita) a implementa, porque aⁿbⁿ não é linguagem regular.

### f. Suponha que um agente selecione sua ação uniformemente ao acaso do conjunto de ações possíveis. Existe um ambiente de tarefa determinista em que esse agente é racional.

- **Julgamento:** **V**
- **Hipóteses:** ambiente determinístico em que **todas as ações disponíveis têm o mesmo desempenho**.
- **Justificativa:** se não há diferença entre as ações, sortear uma delas também maximiza o desempenho esperado. O ambiente ser determinístico não atrapalha: só garante que cada ação leva sempre ao mesmo resultado.
- **Exemplo:** um agente precisa chegar ao 5º andar e há **dois elevadores idênticos**, parados no térreo, com o mesmo tempo de viagem. Escolher ao acaso entre "elevador 1" e "elevador 2" é tão bom quanto qualquer outra regra.

### g. É possível para um dado agente ser perfeitamente racional em dois ambientes de tarefa distintos.

- **Julgamento:** **V**
- **Hipóteses:** os dois ambientes são diferentes, mas a **política ótima** de cada um coincide.
- **Justificativa:** racionalidade é uma relação entre agente e ambiente. Se a mesma regra de decisão é ótima nos dois, o agente é perfeitamente racional nos dois.
- **Exemplo:** um agente que sempre escolhe **o anúncio de menor preço total entre produtos idênticos** é racional tanto num mercado online de livros quanto num de peças de computador, desde que nos dois a medida de desempenho seja "pagar o menor valor por um item equivalente".

### h. Todo agente é racional em um ambiente não observável.

- **Julgamento:** **F**
- **Hipóteses:** o agente não tem sensores úteis, mas possui conhecimento prévio sobre o ambiente.
- **Justificativa:** sem percepções, o agente ainda pode usar o conhecimento prévio para escolher uma **sequência de ações** boa (planejamento "às cegas"). Agentes que fazem escolhas piores continuam sendo irracionais.
- **Contraexemplo:** um aspirador **sem sensores** sabe que a casa tem apenas as salas A e B. A sequência *aspirar → ir para B → aspirar* garante as duas salas limpas. Um aspirador que fica parado para sempre também não observa nada, mas obtém desempenho pior — logo, não é racional.

### i. Um agente jogador de pôquer perfeitamente racional nunca perde.

- **Julgamento:** **F**
- **Hipóteses:** pôquer é estocástico (cartas embaralhadas) e parcialmente observável (cartas fechadas do oponente).
- **Justificativa:** o agente racional maximiza o **ganho esperado**, não garante o resultado de cada mão. Sorte e informação oculta fazem parte do ambiente.
- **Contraexemplo:** o agente vai *all-in* com par de ases contra um par de 7 (≈ 80% de chance de vitória). No *river* sai o terceiro 7 e ele perde a mão — mesmo tendo tomado a decisão correta.

---

## Exercício 2.4 — PEAS e propriedades dos ambientes

Em todos os casos o agente foi delimitado como um **agente artificial** (robô ou software), para deixar sensores e atuadores concretos. As classificações valem **para as hipóteses declaradas** em cada caso.

### Caso 1 — Jogar futebol

- **Agente analisado:** robô atacante de um time de futebol de robôs (estilo RoboCup).
- **Objetivo e hipóteses:** partida completa 5×5 em campo real, com regras oficiais; os robôs do próprio time trocam mensagens por rede sem fio.
- **P — Medida de desempenho:** saldo de gols do time, vitórias, passes certos, finalizações no alvo, poucas faltas, bateria suficiente até o fim da partida.
- **E — Ambiente:** campo, linhas, traves, bola, robôs companheiros, robôs adversários, árbitro, iluminação.
- **A — Atuadores:** motores das pernas/rodas, mecanismo de chute, giro do corpo, rádio para mensagens ao time.
- **S — Sensores:** câmeras, giroscópio e acelerômetro, odometria, sensor de contato com a bola, receptor de rádio (sinais do árbitro e do time).

| Propriedade | Classificação | Justificativa |
|---|---|---|
| Observabilidade | Parcialmente observável | A câmera tem campo de visão limitado; jogadores atrás do robô e intenções dos adversários não são percebidos. |
| Número de agentes | Multiagente — cooperativo **e** competitivo | Coopera com o próprio time (passes, cobertura) e compete com o time adversário. |
| Previsibilidade | Estocástico (e estratégico) | Quiques da bola, escorregões e, principalmente, as escolhas dos adversários tornam o resultado incerto. |
| Dependência entre decisões | Sequencial | Um passe errado agora vira contra-ataque depois; cada jogada muda as opções futuras. |
| Mudança durante a decisão | Dinâmico | Bola e jogadores continuam em movimento enquanto o robô decide. |
| Natureza dos elementos | Contínuo (com eventos discretos) | Posições, velocidades e tempo são contínuos; placar, faltas e escanteios são discretos. |
| Conhecimento do funcionamento | Conhecido | Regras e física básica do jogo são conhecidas pelo projetista; o que é incerto é o comportamento dos outros, não as regras. |

### Caso 2 — Explorar os oceanos subterrâneos de Titã *(cenário hipotético)*

- **Agente analisado:** criorrobô submarino autônomo que perfura o gelo e navega no oceano abaixo dele.
- **Objetivo e hipóteses:** missão de longa duração; comunicação com a Terra leva mais de uma hora e fica indisponível em vários períodos, então o robô decide sozinho. Não há outros agentes no oceano.
- **P — Medida de desempenho:** volume mapeado, número e qualidade das amostras coletadas, dados enviados com sucesso, integridade do casco, energia restante, descoberta de compostos de interesse.
- **E — Ambiente:** camada de gelo, oceano escuro de composição incerta, correntes, pressão elevada, leito rochoso, eventuais fontes térmicas.
- **A — Atuadores:** propulsores, lemes, lastro (subir/descer), broca térmica, braço coletor, holofotes, antena de transmissão.
- **S — Sensores:** sonar, câmeras com iluminação, sensores de pressão, temperatura e salinidade, espectrômetro químico, IMU (inércia) para navegação, medidor de bateria.

| Propriedade | Classificação | Justificativa |
|---|---|---|
| Observabilidade | Parcialmente observável | Escuridão total e alcance limitado do sonar; o robô só "vê" a região próxima. |
| Número de agentes | Agente único | Não há outro agente tomando decisões no oceano (os controladores na Terra praticamente não intervêm). |
| Previsibilidade | Estocástico | Correntes e propriedades do fluido são incertas; o mesmo comando de propulsão pode levar a posições diferentes. |
| Dependência entre decisões | Sequencial | A rota escolhida consome energia e define quais regiões ainda poderão ser exploradas. |
| Mudança durante a decisão | Dinâmico | As correntes continuam deslocando o robô enquanto ele planeja. |
| Natureza dos elementos | Contínuo | Profundidade, pressão, temperatura, posição e energia variam continuamente. |
| Conhecimento do funcionamento | Desconhecido | Ninguém conhece com precisão a dinâmica daquele oceano; o robô precisa aprender o efeito das próprias ações. |

### Caso 3 — Comprar livros usados de IA na Internet

- **Agente analisado:** bot comprador que pesquisa em sebos e marketplaces online.
- **Objetivo e hipóteses:** comprar *um* exemplar de um livro de IA indicado pelo usuário, com orçamento máximo definido e pagamento previamente autorizado.
- **P — Medida de desempenho:** preço total (livro + frete) baixo, estado de conservação adequado, prazo de entrega, reputação do vendedor, respeito ao orçamento, ausência de compras duplicadas.
- **E — Ambiente:** sites de sebos e marketplaces, anúncios, vendedores, outros compradores, sistema de frete, meio de pagamento.
- **A — Atuadores:** buscas e filtros, envio de perguntas ao vendedor, inclusão no carrinho, cálculo de frete por CEP, confirmação de pedido.
- **S — Sensores:** leitura das páginas/APIs: título, edição, preço, fotos, descrição do estado, avaliações do vendedor, estoque e respostas às perguntas.

| Propriedade | Classificação | Justificativa |
|---|---|---|
| Observabilidade | Parcialmente observável | O estado físico real do livro (grifos, páginas soltas) e o estoque verdadeiro só são conhecidos pela descrição do vendedor. |
| Número de agentes | Multiagente — competitivo | Outros compradores disputam o mesmo exemplar; vendedores perseguem o próprio interesse. |
| Previsibilidade | Estocástico | O anúncio pode sumir, o vendedor pode não responder ou cancelar, o frete pode atrasar. |
| Dependência entre decisões | Sequencial | Pesquisar → comparar → perguntar → comprar; comprar um exemplar elimina as outras opções e consome o orçamento. |
| Mudança durante a decisão | Dinâmico | Enquanto o bot compara, alguém pode comprar o exemplar ou o preço pode mudar. |
| Natureza dos elementos | Discreto | Anúncios, cliques, estados da compra e preços (em centavos) são valores discretos e finitos. |
| Conhecimento do funcionamento | Conhecido (regras) / parcialmente desconhecido (qualidade) | O funcionamento dos sites é conhecido; a confiabilidade de cada vendedor precisa ser estimada. |

### Caso 4 — Jogar uma partida de tênis

- **Agente analisado:** robô tenista em partida simples contra um oponente humano.
- **Objetivo e hipóteses:** partida oficial com regras da ITF, quadra externa (sujeita a vento).
- **P — Medida de desempenho:** pontos, games e sets vencidos; porcentagem de primeiro saque; poucos erros não forçados; vitória na partida.
- **E — Ambiente:** quadra, linhas, rede, bola, raquete, adversário, árbitro, vento e sol.
- **A — Atuadores:** braço articulado com a raquete, sistema de locomoção, mecanismo de lançamento da bola no saque.
- **S — Sensores:** câmeras de alta velocidade (trajetória e giro da bola), sensores de força no braço, IMU, odometria.

| Propriedade | Classificação | Justificativa |
|---|---|---|
| Observabilidade | Parcialmente observável | O giro exato da bola e a intenção do adversário (para onde vai bater) não são percebidos diretamente. |
| Número de agentes | Multiagente — competitivo | O oponente tenta, de propósito, colocar a bola onde o robô não alcança. |
| Previsibilidade | Estocástico (e estratégico) | Vento, quiques irregulares e as escolhas do oponente tornam o resultado de cada golpe incerto. |
| Dependência entre decisões | Sequencial | A posição após uma rebatida condiciona a próxima; dentro do ponto as decisões se encadeiam. |
| Mudança durante a decisão | Dinâmico | A bola e o oponente se movem enquanto o robô calcula o golpe. |
| Natureza dos elementos | Contínuo (placar discreto) | Trajetórias, ângulos e velocidades são contínuos; o placar é discreto. |
| Conhecimento do funcionamento | Conhecido | Regras e física da bola são conhecidas. |

### Caso 5 — Praticar tênis contra uma parede

- **Agente analisado:** o mesmo robô tenista, agora em treino individual.
- **Objetivo e hipóteses:** paredão liso em quadra coberta (sem vento); a meta é treinar consistência.
- **P — Medida de desempenho:** maior sequência de rebatidas sem erro, precisão em um alvo pintado na parede, regularidade de ritmo.
- **E — Ambiente:** parede, piso, bola, raquete, alvo pintado.
- **A — Atuadores:** braço com a raquete e sistema de locomoção.
- **S — Sensores:** câmeras de alta velocidade, sensores de força, IMU.

| Propriedade | Classificação | Justificativa |
|---|---|---|
| Observabilidade | Totalmente observável (na prática) | Em espaço pequeno e sem adversário, as câmeras enxergam a bola e a parede o tempo todo; não há intenções ocultas. |
| Número de agentes | Agente único | A parede não tem objetivos nem toma decisões. |
| Previsibilidade | Praticamente determinístico | A reflexão da bola segue a física; restam apenas pequenos ruídos do próprio golpe. |
| Dependência entre decisões | Sequencial | Onde e com que força a bola bate na parede define o próximo golpe. |
| Mudança durante a decisão | Dinâmico | A bola continua em movimento enquanto o robô decide. |
| Natureza dos elementos | Contínuo | Posição, velocidade e tempo são contínuos. |
| Conhecimento do funcionamento | Conhecido | O comportamento da bola ao bater na parede é bem modelado pela física. |

### Caso 6 — Realizar um salto de altura

- **Agente analisado:** robô bípede saltador (ou o sistema de controle de um atleta robótico).
- **Objetivo e hipóteses:** analisamos **uma tentativa** (corrida + impulsão + transposição + queda), com sarrafo em altura fixa, em pista coberta.
- **P — Medida de desempenho:** transpor o sarrafo sem derrubá-lo, maior altura alcançada na competição, queda segura no colchão, número de tentativas usadas.
- **E — Ambiente:** pista de aproximação, sarrafo e postes, colchão, gravidade.
- **A — Atuadores:** motores das articulações (pernas, quadril, braços, tronco).
- **S — Sensores:** câmera/LIDAR para distância até o sarrafo, IMU, sensores de pressão nos pés, encoders das articulações.

| Propriedade | Classificação | Justificativa |
|---|---|---|
| Observabilidade | Totalmente observável | Em ambiente controlado, a posição do sarrafo e do próprio corpo é medida pelos sensores. |
| Número de agentes | Agente único | Durante a tentativa nenhum outro competidor atua; os rivais saltam em outros turnos. |
| Previsibilidade | Determinístico (aprox.) | Em pista coberta, o resultado depende basicamente da mecânica do próprio salto. |
| Dependência entre decisões | Sequencial **dentro** da tentativa; episódico **entre** tentativas | Cada passada define a impulsão; mas cada nova tentativa recomeça do zero, quase independente da anterior. |
| Mudança durante a decisão | Dinâmico | O corpo está em movimento durante todo o processo de decisão. |
| Natureza dos elementos | Contínuo | Ângulos, velocidade e altura são contínuos; "derrubou/não derrubou" é o único resultado discreto. |
| Conhecimento do funcionamento | Conhecido | Biomecânica do salto e regras da prova são conhecidas. |

### Caso 7 — Participar de um leilão de um item, realizando lances

- **Agente analisado:** bot de lances em um leilão online ascendente (estilo inglês).
- **Objetivo e hipóteses:** um único item, valor-limite definido pelo usuário, incremento mínimo fixo, prazo de encerramento; o item tem o mesmo valor para o usuário qualquer que seja o vencedor.
- **P — Medida de desempenho:** arrematar o item; pagar o menor valor possível; nunca passar do limite; não perder o prazo.
- **E — Ambiente:** plataforma do leilão, item, regras, cronômetro, lances públicos, concorrentes (humanos ou bots).
- **A — Atuadores:** enviar lance (valor atual + incremento), aguardar, desistir/encerrar participação.
- **S — Sensores:** lance atual e quem o fez, histórico público de lances, tempo restante, notificações de encerramento.

| Propriedade | Classificação | Justificativa |
|---|---|---|
| Observabilidade | Parcialmente observável | O limite máximo e a estratégia de cada concorrente são ocultos; só os lances já dados são visíveis. |
| Número de agentes | Multiagente — competitivo | Todo lance do agente é um lance a mais que os rivais precisam cobrir, e vice-versa. |
| Previsibilidade | Estocástico (e estratégico) | Não se sabe se, quando ou quanto os outros vão ofertar; há lances de última hora (*sniping*). |
| Dependência entre decisões | Sequencial | Cada lance eleva o preço para todos os passos seguintes. |
| Mudança durante a decisão | Dinâmico | O cronômetro corre e os rivais podem dar lances enquanto o agente decide. |
| Natureza dos elementos | Discreto | Lances em incrementos fixos, número finito de participantes e estados ("liderando", "superado", "encerrado"). |
| Conhecimento do funcionamento | Conhecido | As regras do leilão (incremento, prazo, desempate) são públicas. |

### Quadro-resumo das classificações

| Caso | Observ. | Agentes | Previs. | Episód./Seq. | Est./Din. | Disc./Cont. | Conhecido? |
|---|---|---|---|---|---|---|---|
| Futebol | Parcial | Multi (coop + comp) | Estocástico | Seq. | Dinâmico | Contínuo | Conhecido |
| Titã | Parcial | Único | Estocástico | Seq. | Dinâmico | Contínuo | **Desconhecido** |
| Livros usados | Parcial | Multi (comp) | Estocástico | Seq. | Dinâmico | **Discreto** | Conhecido* |
| Tênis (partida) | Parcial | Multi (comp) | Estocástico | Seq. | Dinâmico | Contínuo | Conhecido |
| Tênis (parede) | **Total** | **Único** | **Determ.** | Seq. | Dinâmico | Contínuo | Conhecido |
| Salto em altura | Total | Único | Determ. | Seq./Episód. | Dinâmico | Contínuo | Conhecido |
| Leilão | Parcial | Multi (comp) | Estocástico | Seq. | Dinâmico | **Discreto** | Conhecido |

\* regras conhecidas; confiabilidade dos vendedores precisa ser estimada.

### Comparação final

1. **Tênis contra uma pessoa × contra a parede.** Muda principalmente o **número de agentes**: a parede não tem objetivo, então o ambiente deixa de ser multiagente competitivo e vira agente único. Com isso ele também fica **praticamente determinístico** e **totalmente observável**, porque some a parte mais imprevisível — a intenção do adversário. O que não muda: continua **sequencial**, **dinâmico** e **contínuo**, porque a bola segue em movimento e cada golpe prepara o próximo.

2. **Livros usados e informação incompleta.** O agente decide a partir de **descrições feitas pelo vendedor** — fotos selecionadas, "bom estado" sem detalhe, estoque que pode estar desatualizado. Ele não pode inspecionar o livro antes de pagar. Por isso precisa estimar riscos (reputação do vendedor, histórico de avaliações), fazer perguntas antes de comprar e aceitar que a decisão ótima é a de melhor **valor esperado**, não a de resultado garantido.

3. **Outros agentes no futebol e no leilão.** No **futebol**, os outros agentes aparecem dos dois lados: companheiros exigem **coordenação** (passes, posicionamento) e adversários **bloqueiam e antecipam** as jogadas, mudando o estado do campo a cada instante. No **leilão** a influência é puramente **competitiva e estratégica**: cada lance rival muda o preço e o agente precisa decidir se cobre ou desiste, sem conhecer o limite dos outros. Nos dois casos, prever só o ambiente "físico" não basta: é preciso modelar o comportamento dos outros agentes.

---

## Exercício 2.5 — Conceitos

| Termo | Definição (com minhas palavras) | Exemplo |
|---|---|---|
| **Agente** | Qualquer coisa que percebe o ambiente por sensores e age sobre ele por atuadores. Pode ser pessoa, robô ou programa — o que importa é o ciclo *perceber → decidir → agir*. | Um app de trânsito que recebe a posição dos carros (sensores) e muda a rota sugerida na tela (atuador). |
| **Função de agente** | Descrição abstrata do comportamento: para **cada sequência possível** de percepções, diz qual ação o agente executa. É uma especificação matemática, não um código. | A tabela "histórico [A: sujo] → aspirar; [A: limpo] → ir para B; …" de um aspirador de duas salas. |
| **Programa de agente** | Implementação concreta da função, que roda numa arquitetura real. Recebe uma percepção por vez e guarda em memória o que precisar do passado. | O código Python [`agente_leilao_automato.py`](agente_leilao_automato.py) que lê um evento do leilão e devolve uma ação. |
| **Racionalidade** | Escolher, a cada momento, a ação com o **maior desempenho esperado**, considerando a medida de desempenho, o conhecimento prévio, as ações possíveis e as percepções até agora. Não é acertar sempre. | Levar guarda-chuva quando a previsão é 70% de chuva é racional, mesmo que no fim não chova. |
| **Autonomia** | Quanto o comportamento do agente depende da **própria experiência** em vez de apenas do conhecimento colocado pelo projetista. Mais autonomia = melhor adaptação a situações não previstas. | Um robô de entregas que aprende sozinho que um corredor do prédio vive bloqueado e passa a evitá-lo. |
| **Agente reativo** | Decide olhando **só a percepção atual**, com regras *se condição então ação*. É simples e rápido, mas falha quando o ambiente não é totalmente observável. | Porta automática: *se* sensor detecta presença *então* abre. |
| **Agente baseado em modelo** | Mantém um **estado interno** que resume o que não está visível agora, atualizado com um modelo de como o mundo evolui e de como as próprias ações o afetam. | Um robô de limpeza que guarda o mapa das áreas já limpas e não volta a elas. |
| **Agente baseado em objetivos** | Além do estado do mundo, conhece uma **meta** e escolhe ações pensando no futuro (busca/planejamento) para chegar até ela. | Um GPS que calcula a sequência de ruas para chegar ao campus. |
| **Agente baseado em utilidade** | Compara estados por uma **função de utilidade** que mede *quão bom* é cada resultado, permitindo pesar objetivos conflitantes e risco. | Um app de transporte que escolhe entre ônibus, metrô ou carro pesando preço, tempo e conforto. |
| **Agente com aprendizagem** | Tem um elemento que **melhora o próprio desempenho** com o tempo: um crítico avalia os resultados, um elemento de aprendizagem ajusta as regras e um gerador de problemas sugere experimentar coisas novas. | Um filtro de spam que melhora cada vez que o usuário marca uma mensagem como "não é spam". |

---

## Síntese com autômatos

**Caso escolhido:** Caso 7 — **leilão de um item** (bot de lances com valor-limite *L*).

O agente é modelado como um **autômato finito com saída** (estilo máquina de Mealy): cada transição lê uma percepção e, ao mudar de estado, emite uma ação.

**Três estados internos**

| Estado | Significado (o que ele "lembra") |
|---|---|
| **Q1 — SUPERADO** | O último lance válido **não é meu** (ou ainda não dei lance). |
| **Q2 — LIDERANDO** | O lance mais alto atual **é meu**. |
| **Q3 — ENCERRADO** | Não participo mais: arrematei, desisti ou o leilão acabou. *(estado final)* |

**Três percepções**

| Percepção | Descrição |
|---|---|
| **p1 — rival ≤ limite** | Um concorrente deu lance e *lance + incremento ≤ L*. |
| **p2 — rival > limite** | Um concorrente deu lance e cobrir ultrapassaria *L*. |
| **p3 — fim do tempo** | O cronômetro zerou. |

**Três ações**

| Ação | Descrição |
|---|---|
| **a1 — dar lance** | Enviar *lance atual + incremento*. |
| **a2 — arrematar** | Confirmar a compra do item ao fim do leilão. |
| **a3 — desistir** | Sair do leilão sem o item. |

**Regras de transição** (*estado atual + percepção → próximo estado e ação*)

- **R1:** `Q1 + p1 → Q2 , a1` — estou superado e ainda cabe no limite: dou um lance e passo a liderar.
- **R2:** `Q2 + p3 → Q3 , a2` — o tempo acabou comigo liderando: arremato o item.

Regras complementares (para o autômato ficar completo):

| Estado \ Percepção | p1 — rival ≤ limite | p2 — rival > limite | p3 — fim do tempo |
|---|---|---|---|
| **Q1 — SUPERADO** | Q2 , a1 *(R1)* | Q3 , a3 | Q3 , a3 |
| **Q2 — LIDERANDO** | Q2 , a1 *(cubro e sigo liderando)* | Q3 , a3 | Q3 , a2 *(R2)* |
| **Q3 — ENCERRADO** | Q3 , — | Q3 , — | Q3 , — |

```text
                         p1 / a1
                        ┌───────┐
              p1 / a1   │       ▼
   ┌──────────┐ ──────► ┌───────────┐
   │    Q1    │         │    Q2     │
   │ SUPERADO │         │ LIDERANDO │
   └──────────┘         └───────────┘
     │      │             │       │
  p2/a3   p3/a3         p2/a3   p3/a2
     ▼      ▼             ▼       ▼
   ┌────────────────────────────────────┐
   │          Q3 — ENCERRADO            │
   └────────────────────────────────────┘
```

**Como o estado interno representa informação passada.** A percepção "o tempo acabou" (p3) é **idêntica** em Q1 e em Q2, mas a ação correta é oposta: em Q2 o agente arremata, em Q1 sai sem o item. O que decide é o passado — *o último lance válido foi meu?* O estado Q2 resume toda a sequência de percepções anteriores nesse único fato. Assim o programa não precisa guardar o histórico completo de lances; um símbolo de estado basta. É a diferença entre **função de agente** (recebe o histórico inteiro) e **programa de agente** (recebe a percepção atual + estado interno). Um agente reativo puro, sem estado, não teria como responder corretamente a p3 — é um exemplo concreto do item 2.3-b.

**Limitação da simplificação.** Com só três estados o agente não representa **quanto** falta para o limite, **quanto tempo** resta nem o **perfil dos rivais**. Ele cobre sempre que pode, então não consegue usar estratégias melhores, como esperar os últimos segundos (*sniping*) ou economizar evitando guerras de lances no começo. Além disso, o valor do lance e o limite ficam fora do autômato (são variáveis numéricas do programa). Para decidir com isso seria preciso um agente baseado em utilidade, e o modelo deixaria de ser um autômato finito simples.

**Execução.** O arquivo [`agente_leilao_automato.py`](agente_leilao_automato.py) implementa essa tabela de transições e simula dois leilões. Saída real:

```text
$ python agente_leilao_automato.py
=== Cenário 1 — rivais param antes do limite ===
Limite do agente: R$ 300,00 | incremento: R$ 20,00
passo | percepção                | estado -> próximo          | ação
------+--------------------------+----------------------------+---------------------------
    1 | rival deu R$ 150,00      | SUPERADO   -> LIDERANDO    | dar lance de R$ 170,00
    2 | rival deu R$ 190,00      | LIDERANDO  -> LIDERANDO    | dar lance de R$ 210,00
    3 | rival deu R$ 230,00      | LIDERANDO  -> LIDERANDO    | dar lance de R$ 250,00
    4 | fim do tempo             | LIDERANDO  -> ENCERRADO    | arrematar
Resultado: ARREMATOU por R$ 250,00

=== Cenário 2 — rival passa do limite ===
Limite do agente: R$ 300,00 | incremento: R$ 20,00
passo | percepção                | estado -> próximo          | ação
------+--------------------------+----------------------------+---------------------------
    1 | rival deu R$ 200,00      | SUPERADO   -> LIDERANDO    | dar lance de R$ 220,00
    2 | rival deu R$ 240,00      | LIDERANDO  -> LIDERANDO    | dar lance de R$ 260,00
    3 | rival deu R$ 290,00      | LIDERANDO  -> ENCERRADO    | desistir (passaria do limite)
Resultado: não arrematou — último lance do agente: R$ 260,00
```

---

## Referências

- RUSSELL, Stuart; NORVIG, Peter. *Inteligência Artificial: uma abordagem moderna*. Capítulo 2 — Agentes inteligentes. Material disponibilizado na disciplina.
- VALÉRIA, Kadidja. *Instruções gerais — Atividade sobre agentes inteligentes*. UDF, aula de 19/10/2026.
- Conteúdo de Linguagens Formais da própria disciplina (autômatos finitos, linguagem aⁿbⁿ, Máquinas de Turing e problema da parada) — ver pastas [`Unidade1_LinguagensFormais`](../Unidade1_LinguagensFormais) e [`LinguagensRegulares_MaquinaTuring`](../LinguagensRegulares_MaquinaTuring) deste repositório.
