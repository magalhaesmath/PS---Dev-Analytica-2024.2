# Questão 1 da Tarefa de Análise de Dados 1, PS - Dev UFRJ Analytica 2024.2
# Autor: Matheus Magalhães

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def main():
    # Questão 1:
    dataFrame = pd.read_csv(r"C:\Users\emine\OneDrive\Documentos\Faculdade\Ciência da Computação\4o Período\UFRJ Analytica\Dataset_Processo_Seletivo_UFRJ_Analytica_2024-2.csv")
    
    # Questão 2:
    print(dataFrame) # Imprime a tabela.  
    print("\n")

    # Questão 3:
    # (a)
    filtro1991 = dataFrame["ano"] == 1991
    dataFrame1991 = dataFrame[filtro1991]
    print(dataFrame1991) # Dados somente do ano de 1991
    print("\n")

    # (b) e (c)
    idhMedioNacional = sum(dataFrame1991["idhm"])/27 # São 27 UF's.
    print(f"\n\nIDH médio do Brasil em 1991 era {idhMedioNacional:.3f}\n\n")

    # Questão 4:
    # (a)
    filtro_IDHMedio = dataFrame1991["idhm"] > idhMedioNacional
    dataFrameIDHMedia = dataFrame1991[filtro_IDHMedio]

    # (b)
    print("\nEstados que, em 1991, possuíam IDH médio acima da média nacional: \n")
    for estado in dataFrameIDHMedia["sigla_uf"]:
        print(estado + '\n')

    # Questão 5:
    dataFrame1991.sort_values(by='idhm')
    print(dataFrame1991.head(5))


    # Questão 6:
    print(dataFrame1991.min())
    print("\n")
    print(dataFrame1991.idxmin())
    print("\n")
    print(dataFrame1991.max())
    print("\n")
    print(dataFrame1991.idxmax())

    # Pelos dados expostos acima, sabemos que o menor IDH é 0.357 e o Estado é o 9.
    # Além disso, o maior IDH é de 0.616 e o Estado relativo tem índice 6.
    # Basta retornar estes Estados.

    print("\n")
    print("O Estado de menor IDH em 1991 era: " + dataFrame1991["sigla_uf"][9])
    print("O Estado de maior IDH em 1991 era: " + dataFrame1991["sigla_uf"][6])
    print("\n")

    # Questões da sessão 1.3 - Matplotlib

    # Questão 1: 
    estados = dataFrame1991["sigla_uf"]  
    populacoes = dataFrame1991["populacao_urbana"]  

    plt.bar(estados,populacoes)
    plt.xlabel('Estados')
    plt.ylabel('População total em dezenas de milhões')
    plt.title('Populações dos Estados em 1991:')
    plt.show()

    # Questão 2:
    idh1991 = dataFrame1991["idhm"]

    filtro2000 = dataFrame["ano"] == 2000
    dataFrame2000 = dataFrame[filtro2000]

    idh2000 = dataFrame2000["idhm"]

    filtro2010 = dataFrame["ano"] == 2010
    dataFrame2010 = dataFrame[filtro2010]

    idh2010 = dataFrame2010["idhm"]

    plt.figure(figsize=(10, 6))

    # Histograma para 1991
    plt.hist(idh1991, bins=10, alpha=0.5, label='IDH 1991')

    # Histograma para 2000
    plt.hist(idh2000, bins=10, alpha=0.5, label='IDH 2000')

    # Histograma para 2010
    plt.hist(idh2010, bins=10, alpha=0.5, label='IDH 2010')

    # Configurações do gráfico
    plt.title('Histograma do IDH em 1991, 2000 e 2010')
    plt.xlabel('IDH')
    plt.ylabel('Frequência')
    plt.legend()

    plt.show()

    # Questão 3: 
    idh = np.array(dataFrame["idhm"])
    expectativaVida = np.array(dataFrame["expectativa_vida"])

    plt.scatter(idh,expectativaVida)
    plt.xlabel('IDH')  
    plt.ylabel('Expectativa de Vida')
    plt.title('Expectativa de vida em função do IDH')  
    plt.show()
    
    # Analisando o plot da expectativa de vida em função do IDH, percebe-se um claro padrão, que pode ser uma reta
    # ou até mesmo uma exponencial. Isso poderia ser comprovado através de uma regressão polinomial.
    # Conclusão final obtida: Quanto maior o IDH, maior será a expectativa de vida.
    
    # Desafio Final:
    expectativaVida1991 = dataFrame1991["expectativa_vida"]
    expectativaVida2010 = dataFrame2010["expectativa_vida"]
    diferencasExpectativa = []

    i = 0
    for expectativa in expectativaVida2010:
        diferencasExpectativa.append(expectativa - expectativaVida1991[i])
        i+=1

    plt.bar(dataFrame1991["sigla_uf"], diferencasExpectativa)
    plt.xlabel('Estados')
    plt.ylabel('Diferença absoluta na expectativa de vida entre 1991 e 2010')
    plt.axhline(y=10,color='r', linestyle='--')
    plt.show() # Gráfico com as diferenças na expectativa de vida das UF's.

    estadosDif10 = []

    for i in range(0,27):
        if(diferencasExpectativa[i] >= 10):
            estadosDif10.append(dataFrame1991["sigla_uf"][i])
    
    print("Os Estados brasileiros que apresentaram um aumento de, no mínimo, 10 anos em suas expectativas de vida entre 1991 e 2010 foram: ")
    print(estadosDif10)

    # As UF's que apresentaram esse aumento de, no mínimo, 10 anos foram: AL, BA, CE, MA, MT, PB, PE, PI, RN, RR, SE, TO.
    return 

if __name__ == "__main__":
    main()
