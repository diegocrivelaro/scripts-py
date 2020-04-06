from random import choice

sexo = input("Nomes masculinos ou feminino? [M/F] ").strip()[0]
x = int(input("Quantos nomes randômicos serão gerados? "))

sobrenomes = ["Ferreira", "Barbosa", "Barros",
                "Silva", "Borges", "Batista",
                "Campos", "Cardoso", "Costa",
                "Pereira", "Souza", "Santos",
                "Alves", "Gomes", "Lima"]

for cont in range(0, x+1):
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