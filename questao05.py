def main():
    # Lê o número inteiro de 1 a 12
    try:
        numero_mes = int(input("Digite um número de 1 a 12: "))
    except ValueError:
        print("Valor inválido. Insira um número inteiro de 1 a 12.")
        return

    # Verifica o mês correspondente usando match case
    match numero_mes:
        case 1:
            mes = "Janeiro"
        case 2:
            mes = "Fevereiro"
        case 3:
            mes = "Março"
        case 4:
            mes = "Abril"
        case 5:
            mes = "Maio"
        case 6:
            mes = "Junho"
        case 7:
            mes = "Julho"
        case 8:
            mes = "Agosto"
        case 9:
            mes = "Setembro"
        case 10:
            mes = "Outubro"
        case 11:
            mes = "Novembro"
        case 12:
            mes = "Dezembro"
        case _:
            mes = "Mês Inválido"

    # Exibe o resultado
    print(f"O número {numero_mes} corresponde ao mês de {mes}.")

if __name__ == "__main__":
    main()
