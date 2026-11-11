# Sistema de Controle de Hotel
# Artefato inicial do projeto.

hospedes = []

def cadastrar_hospede(nome, quarto):
    hospede = {"nome": nome, "quarto": quarto}
    hospedes.append(hospede)
    print(f"Hóspede {nome} cadastrado no quarto {quarto}.")

def listar_hospedes():
    if not hospedes:
        print("Nenhum hóspede cadastrado.")
        return

    print("\nHóspedes cadastrados:")
    for hospede in hospedes:
        print(f"Nome: {hospede['nome']} | Quarto: {hospede['quarto']}")

if __name__ == "__main__":
    cadastrar_hospede("João da Silva", 12)
    listar_hospedes()
