# Nova funcionalidade: consulta de disponibilidade de quarto.

def verificar_disponibilidade(quartos_ocupados, numero_quarto):
    """Retorna True quando o quarto não está na lista de ocupados."""
    return numero_quarto not in quartos_ocupados


if __name__ == "__main__":
    quartos_ocupados = [10, 11, 12]
    quarto_consultado = 15

    if verificar_disponibilidade(quartos_ocupados, quarto_consultado):
        print(f"O quarto {quarto_consultado} está disponível.")
    else:
        print(f"O quarto {quarto_consultado} está ocupado.")
