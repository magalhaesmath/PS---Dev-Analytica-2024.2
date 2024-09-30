# Questão 3 da Tarefa de Programação 2, PS - Dev UFRJ Analytica 2024.2
# Autor: Matheus Magalhães

def main():
  notas100 = 0;
  notas50 = 0;
  notas20 = 0;
  notas10 = 0;
  notas5 = 0;
  notas2 = 0;
  moedas1 = 0;
  moedas50cent = 0;
  moedas25cent = 0;
  moedas10cent = 0;
  moedas5cent = 0;
  moedas1cent = 0;

  valor = input("> ")
  try:
    valor = float(valor)
  except ValueError:
    print("Valor inválido.")
    return
  if valor < 0:
    print("Valor inválido.")
    return
  if valor == 0:
    print("0 nota(s)")

  valores = [100, 50, 20, 10, 5, 2, 1, .5, .25, .1, .05, .01]
  notas = [notas100, notas50, notas20, notas10, notas5, notas2, moedas1, moedas50cent, moedas25cent, moedas10cent, moedas5cent, moedas1cent]

  resto = valor
  for i in range(len(valores)):
    notas[i] = int(resto // valores[i])
    resto = resto % valores[i]

  print(f"NOTAS:\n{notas[0]} nota(s) de R$ 100.00\n{notas[1]} nota(s) de R$ 50.00\n{notas[2]} nota(s) de R$ 20.00\n{notas[3]} nota(s) de R$ 10.00\n{notas[4]} nota(s) de R$ 5.00\n{notas[5]} nota(s) de R$ 2.00\n")
  print(f"MOEDAS:\n{notas[6]} moeda(s) de R$ 1.00\n{notas[7]} moeda(s) de R$ 0.50\n{notas[8]} moeda(s) de R$ 0.25\n{notas[9]} moeda(s) de R$ 0.10\n{notas[10]} moeda(s) de R$ 0.05\n{notas[11]} moeda(s) de R$ 0.01\n")

if __name__ == "__main__":
  main()
