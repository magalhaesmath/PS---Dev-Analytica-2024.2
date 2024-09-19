def main():
  numeros = {}
  while True:
    entrada = input("> ")
    if entrada == 'f':
      break
    try:
      numero = int(entrada) 
      if entrada not in numeros:
        numeros[entrada] = 1
      else:
        numeros[entrada] += 1
    except ValueError:
      continue

  for numero, frequencia in numeros.items():
    print(f"O número {numero} apareceu {frequencia} vez(es).")
  print("Fim...")

if __name__ == "__main__":
  main()
  
