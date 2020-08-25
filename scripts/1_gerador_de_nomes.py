from random import choice

sexo = input("Nomes masculinos ou feminino? [M/F] ").strip()[0]
x = int(input("Quantos nomes randômicos serão gerados? "))

sobrenomes = ["Ferreira", "Barbosa", "Barros",
                "Silva", "Borges", "Batista",
                "Campos", "Cardoso", "Costa",
                "Pereira", "Souza", "Santos",
                "Alves", "Gomes", "Lima"]
# Código anterior
# for cont in range(0, x+1):
# Código proposto
# Testei seu programa e ele estava retornando 1 nome a mais, então estou sugerindo esta correção
  for cont in range(0, x):
    if sexo in "Mm":
        nomesm = ["Marcos", "Pedro", "Alessandro",
                    "Diego", "Gabriel", "Rafael", 
                    "Bob", "Nathan", "James"]   
        print(f"\033[1m{choice(nomesm)} {choice(sobrenomes)}\033[m")

    elif sexo in "Ff":
        nomesf = ["Julia", "Luisa", "Alice", 
                    "Pietra", "Laura", "Livia", 
                    "Larissa", "Sabrina", "Sofia"]
        print(f"\033[1m{choice(nomesf)} {choice(sobrenomes)}\033[m")
