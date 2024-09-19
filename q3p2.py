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
  
  resto = valor
  notas100 = resto // 100
  resto = resto % 100
  notas50 = resto // 50
  resto = resto % 50
  notas20 = resto // 20
  resto = resto % 20
  notas10 = resto // 10
  resto = resto % 10 
  notas5 = resto // 5
  resto = resto % 5
  notas2 = resto // 2
  resto = resto % 2
  moedas1 = resto // 1
  resto = resto % 1
  moedas50cent = resto // 0.5
  resto = resto % 0.5
  moedas25cent = resto // 0.25
  resto = resto % 0.25
  moedas10cent = resto // 0.1
  resto = resto % 0.1
  moedas5cent = resto // 0.05
  resto = resto % 0.05
  moedas1cent = resto // 0.01
  resto = resto % 0.01

  print(f"NOTAS:\n{notas100} nota(s) de R$ 100.00\n{notas50} nota(s) de R$ 50.00\n{notas20} nota(s) de R$ 20.00\n{notas10} nota(s) de R$ 10.00\n{notas5} nota(s) de R$ 5.00\n{notas2} nota(s) de R$ 2.00\n")
  print(f"MOEDAS:\n{moedas1} moeda(s) de R$ 1.00\n{moedas50cent} moeda(s) de R$ 0.50\n{moedas25cent} moeda(s) de R$ 0.25\n{moedas10cent} moeda(s) de R$ 0.10\n{moedas5cent} moeda(s) de R$ 0.05\n{moedas1cent} moeda(s) de R$ 0.01\n")

if __name__ == "__main__":
  main()
