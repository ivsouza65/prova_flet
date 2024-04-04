# Lê o valor da variável nome_maquina
nome_maquina = input("Digite o nome da máquina: ")

    # Lê o valor da variável tempo_uso (como inteiro)
try:
        tempo_uso = int(input("Digite o tempo de uso (em minutos): "))
except ValueError:
        print("Valor inválido para tempo_uso. Use um número inteiro.")

    # Lê o valor da variável ligado (como booleano)
ligado_str = input("A máquina está ligada? (S/N): ")
ligado = ligado_str.upper() == "S"

    # Exibe os valores lidos e seus tipos
print(f"Valores lidos:")
print(f"  - nome_maquina: {nome_maquina} (tipo: {type(nome_maquina).__name__})")
print(f"  - tempo_uso: {tempo_uso} (tipo: {type(tempo_uso).__name__})")
print(f"  - ligado: {ligado} (tipo: {type(ligado).__name__})")
