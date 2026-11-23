# Sistema Especialista: Quanto Abastecer Antes da Viagem

**Aluno:** Renato Miranda de Souza Araujo Alves  
**RGM:** 38989611
**Aluno:** Vitor Hugo Duarte Lima   
**RGM:** 38853558

**Disciplina:** Inteligência Artificial e LFA | Sistemas Especialistas  
**Professora:** Kadidja Valéria

## Projeto

Sistema híbrido (aprendizado de máquina + sistema especialista) que ajuda o motorista a decidir quanto abastecer antes de uma viagem.

O usuário informa:

- a distância da viagem (km);
- o consumo médio do carro (km por litro);
- quantos litros cabem no tanque;
- quantos litros já estão no tanque.

O sistema responde se o gasto da viagem será **alto** ou **baixo**, quantos litros são necessários com margem de segurança, qual regra foi aplicada e o que fazer.

**Exemplo:** 60 km, carro que faz 12 km/l, tanque de 16 L com 2 L. O gasto previsto é baixo, a viagem precisa de 5,5 L (5 L + 10% de margem), aplica a R2 e a recomendação é **abastecer pelo menos 3,5 litros**.

## Arquivos

| Arquivo | Conteúdo |
|---|---|
| `SISTEMAESPECIALISTA_ES_N1.ipynb` | Notebook com o desenvolvimento completo, as respostas do estudo inicial e a análise dos resultados |
| `dataset_viagens_simulado.csv` | Dataset rotulado e simulado usado no treino e no teste (16 viagens) |
| `requirements.txt` | Bibliotecas para rodar na máquina local |
| `README.md` | Este arquivo |

## Como funciona

1. **A árvore de decisão prevê o gasto.** Ela recebe `distancia_km` e `consumo_km_l` e classifica a viagem como `alto` ou `baixo`. Essa previsão vira o **fato 1**.
2. **O sistema calcula os litros necessários.** A margem de segurança depende do gasto previsto: 10% para gasto baixo e 20% para gasto alto.
3. **O sistema compara com o tanque.** Isso gera o **fato 2**, a situação do tanque:
   - `suficiente`: o que já tem no tanque cobre a viagem;
   - `falta_cabe`: falta combustível, mas o que falta cabe no tanque;
   - `nao_cabe`: a viagem precisa de mais do que o tanque comporta.
4. **O motor de inferência aplica a regra.** A função `aplicar_regras()` procura a regra que combina com os dois fatos e devolve a recomendação com a explicação.

## Base de conhecimento (regras)

As regras foram escritas por mim. Elas não foram aprendidas dos dados, e essa é a diferença entre a parte especialista e a parte de aprendizado de máquina.

| Regra | SE | ENTÃO |
|---|---|---|
| R1 | situação = suficiente | não precisa abastecer |
| R2 | gasto = baixo E situação = falta_cabe | abastecer os litros que faltam |
| R3 | gasto = alto E situação = falta_cabe | abastecer os litros que faltam e, se possível, completar o tanque |
| R4 | situação = nao_cabe | encher o tanque e planejar uma parada no caminho |

## Os dados

O dataset é **fictício**, com 16 viagens: 8 de gasto baixo e 8 de gasto alto. O critério de rotulagem foi: gasto **alto** quando a viagem gasta mais de 10 litros (distância ÷ consumo > 10) e **baixo** nos demais casos.

O arquivo `dataset_viagens_simulado.csv` tem as colunas `distancia_km`, `consumo_km_l` e `gasto`.

## Resultados

Foram separadas 12 viagens para treino e 4 para teste. A árvore, com profundidade máxima 2, acertou **100% dos casos de teste**.

| Caso | Entrada | Regra | Recomendação |
|---|---|---|---|
| 1 | 40 km, 10 km/l, tanque de 50 L com 12 L | R1 | Não precisa abastecer |
| 2 | 60 km, 12 km/l, tanque de 16 L com 2 L | R2 | Abastecer pelo menos 3,5 L |
| 3 | 200 km, 12 km/l, tanque de 50 L com 5 L | R3 | Abastecer pelo menos 15 L e, se possível, completar o tanque |
| 4 | 250 km, 10 km/l, tanque de 16 L com 2 L | R4 | Encher o tanque (14 L) e parar para abastecer antes de 133 km |

O resultado de 100% não mostra que o sistema funciona na vida real: são só 4 casos de teste, os dados são fictícios e as classes foram feitas para serem fáceis de separar.

## Limitações

- A árvore aprendeu a separar só pela distância (viagens acima de 125 km são gasto alto). Um carro que gasta muito em uma viagem média recebe a margem menor.
- O consumo informado é uma média e muda com trânsito, ar-condicionado, estrada ou cidade.
- As margens de segurança (10% e 20%) foram escolhidas por mim, não foram validadas com dados reais.
- É um exemplo didático. A decisão final é sempre do motorista.

## Como rodar

O jeito mais fácil é abrir o notebook no [Google Colab](https://colab.research.google.com/drive/1ilf0m0UijDwyJdF0HOQb6PVkVXpISJY5) e ir em **Ambiente de execução → Executar tudo**. Os dados já estão dentro do notebook, então não precisa carregar o CSV. Na seção 7 dá para trocar os quatro valores da consulta e executar de novo.

Na máquina local:

```bash
pip install -r requirements.txt
jupyter notebook SISTEMAESPECIALISTA_ES_N1.ipynb
```

## Tecnologias

Python, pandas, scikit-learn, matplotlib e Google Colab.

## Referências

- IBM. Guia de Aprendizado de Máquina: https://www.ibm.com/br-pt/think/machine-learning
- IBM. Aprendizado supervisionado: https://www.ibm.com/br-pt/think/topics/supervised-learning
- scikit-learn. DecisionTreeClassifier: https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html
- scikit-learn. train_test_split: https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html
