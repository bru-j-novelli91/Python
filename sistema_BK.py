import textwrap

# ================= MENU =================
def menu():
    menu = """
============= MENU ================
[d]\tDepositar
[s]\tSacar
[e]\tExtrato
[nu]\tNovo Usuário
[nc]\tNova Conta
[lc]\tListar Contas
[q]\tSair
=> """
    return input(textwrap.dedent(menu))


# ================= DEPÓSITO =================
def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Valor inválido! @@@")
    return saldo, extrato


# ================= SAQUE =================
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > saldo:
        print("\n@@@ Saldo insuficiente! @@@")
    elif valor > limite:
        print("\n@@@ Valor excede o limite! @@@")
    elif numero_saques >= limite_saques:
        print("\n@@@ Limite de saques atingido! @@@")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")
    else:
        print("\n@@@ Valor inválido! @@@")

    return saldo, extrato, numero_saques


# ================= EXTRATO =================
def exibir_extrato(saldo, /, *, extrato):
    print("\n======== EXTRATO ========")
    print(extrato if extrato else "Não houve movimentações.")
    print(f"Saldo:\t\tR$ {saldo:.2f}")
    print("=========================")


# ================= USUÁRIO =================
def filtrar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None


def criar_usuario(usuarios):
    cpf = input("CPF (somente números): ")
    if filtrar_usuario(cpf, usuarios):
        print("\n@@@ Usuário já existe! @@@")
        return

    nome = input("Nome completo: ")
    nascimento = input("Data de nascimento (dd-mm-aaaa): ")
    endereco = input("Endereço: ")

    usuarios.append({
        "nome": nome,
        "cpf": cpf,
        "nascimento": nascimento,
        "endereco": endereco
    })

    print("\n=== Usuário criado com sucesso! ===")


# ================= CONTA =================
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if not usuario:
        print("\n@@@ Usuário não encontrado! @@@")
        return None

    print("\n=== Conta criada com sucesso! ===")
    return {"agencia": agencia, "numero": numero_conta, "usuario": usuario}


def listar_contas(contas):
    for conta in contas:
        print("=" * 40)
        print(f"Agência: {conta['agencia']}")
        print(f"Conta: {conta['numero']}")
        print(f"Titular: {conta['usuario']['nome']}")


# ================= MAIN =================
def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Valor do saque: "))
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("\n@@@ Opção inválida! @@@")


main()




 
  
 



    





    
     
      



        

