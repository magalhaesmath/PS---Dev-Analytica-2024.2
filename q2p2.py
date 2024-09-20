# Questão 1 da Tarefa de Programação 2, PS - Dev UFRJ Analytica 2024.2
# Autor: Matheus Magalhães

def main():
    while True:
        entrada = input("> ").lower() 
        if entrada == 'f':
            print("Fim...")
            break
        
        if len(entrada) != 2 or entrada[0] not in 'abcdefgh' or not entrada[1].isdigit() or int(entrada[1]) not in range(1, 9):
            print("Posição inválida!")
            continue

        h = entrada[0]  # Horizontal (letra)
        v = int(entrada[1])  # Vertical (número)

        # Movimentos possíveis do cavalo:
        movimentos = [
            (-2, -1), (-2, 1), (2, -1), (2, 1),
            (-1, -2), (1, -2), (-1, 2), (1, 2)
        ]

        posicoesPossiveis = []

        colunas = 'abcdefgh'
        coluna_atual = colunas.index(h)

        for movimento in movimentos:
            nova_coluna = coluna_atual + movimento[0]
            nova_linha = v + movimento[1]

            if 0 <= nova_coluna < 8 and 1 <= nova_linha <= 8:
                posicao = colunas[nova_coluna] + str(nova_linha)
                posicoesPossiveis.append(posicao)

        print(", ".join(sorted(posicoesPossiveis)))

if __name__ == "__main__":
    main()
