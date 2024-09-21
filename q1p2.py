# Questão 1 da Tarefa de Programação 2, PS - Dev UFRJ Analytica 2024.2
# Autor: Matheus Magalhães

def main ():
  entrada = input("> ")
  hora = str(entrada)

  if entrada == 'f':
    print("Fim...")
    return

  if len(hora) != 5 or hora[2] != ":" or not hora[0:2].isdigit() or not hora[3:5].isdigit() or int(hora[0:2]) > 23 or int(hora[3:5]) > 59:
    print("Entrada inválida")
    return

  # Para cada hora avançada a partir das 00h ou 12h, o ponteiro de horas avança 30 graus -> 360/12 = 30
  anguloHora = int(hora[0:2]) * 30

  # Para cada minuto avançado a partir dos 00min, o ponteiro de minutos avança 6 graus -> 360/60 = 6
  anguloMinuto = int(hora[3:5]) * 6

  anguloHoraMinuto = abs(anguloHora - anguloMinuto)

  if anguloHoraMinuto > 180:
    anguloHoraMinuto = abs(360 - anguloHoraMinuto)
  
  print(f"O menor ângulo é de {anguloHoraMinuto}°")

if __name__ == "__main__":
  main()
