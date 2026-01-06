import textwrap
from abc import ABC, abstractmethod
from datetime import datetime

# ================= CLIENTE =================
class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome, cpf, data_nascimento, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento


# ================= CONTA =================
class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self.numero = numero
        self.agencia = "0001"
        self.cliente = cliente
        self.historico = Historico()

    @property
    def saldo(self):
        return self._saldo

    def sacar(self, valor):
        if valor > self._saldo:
            print("\n@@@ Saldo insuficiente! @@@")
            return False

        if valor > 0:
            self._saldo -= valor
            return True

        print("\n@@@ Valor inválido! @@@")
        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            return True

        print("\n@@@ Valor inválido! @@@")
        return False


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        saques_realizados = len(
            [t for t in self.historico.transacoes if t["tipo"] == "Saque"]
        )

        if valor > self.limite:
            print("\n@@@ Valor excede o limite! @@@")
            return False

        if saques_realizados >= self.limite_saques:
            print("\n@@@ Limite de saques atingido! @@@")
            return False

        return super().sacar(valor)


# ================= HISTÓRICO =================
class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            }
        )


# ================= TRANSAÇÃO =================
class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        if conta.depositar(self.valor):
            conta.historico.adicionar_transacao(self)
            print("\n=== Depósito realizado com sucesso! ===")


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        if conta.sacar(self.valor):
            conta.historico.adicionar_transacao(self)
            print("\n=== Saque realizado com sucesso! ===")


# ================= FUNÇÕES AUXILIARES =================
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


def filtrar_cliente(cpf, clientes):
    for cliente in clientes:
        if cliente.cpf == cpf:
            return cliente
    return None


def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\n@@@ Cliente não possui conta! @@@")
        return None
    return cliente.contas[0]


def exibir_extrato(conta):
    print("\n======== EXTRATO ========")
    if not conta.historico.transacoes:
        print("Não houve movimentações.")
    else:
        for t in conta.historico.transacoes:
            print(f"{t['tipo']}:\tR$ {t['valor']:.2f} ({t['data']})")

    print(f"\nSaldo:\t\tR$ {conta.saldo:.2f}")
    print("=========================")


# ================= MAIN =================
def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "nu":
            cpf = input("CPF: ")
            if filtrar_cliente(cpf, clientes):
                print("\n@@@ Usuário já existe! @@@")
                continue

            nome = input("Nome completo: ")
            nascimento = input("Data de nascimento: ")
            endereco = input("Endereço: ")

            cliente = PessoaFisica(nome, cpf, nascimento, endereco)
            clientes.append(cliente)
            print("\n=== Usuário criado com sucesso! ===")

        elif opcao == "nc":
            cpf = input("CPF do usuário: ")
            cliente = filtrar_cliente(cpf, clientes)

            if not cliente:
                print("\n@@@ Usuário não encontrado! @@@")
                continue

            numero_conta = len(contas) + 1
            conta = ContaCorrente(numero_conta, cliente)
            cliente.adicionar_conta(conta)
            contas.append(conta)

            print("\n=== Conta criada com sucesso! ===")

        elif opcao in ("d", "s", "e"):
            cpf = input("CPF do usuário: ")
            cliente = filtrar_cliente(cpf, clientes)

            if not cliente:
                print("\n@@@ Usuário não encontrado! @@@")
                continue

            conta = recuperar_conta_cliente(cliente)
            if not conta:
                continue

            if opcao == "d":
                valor = float(input("Valor do depósito: "))
                cliente.realizar_transacao(conta, Deposito(valor))

            elif opcao == "s":
                valor = float(input("Valor do saque: "))
                cliente.realizar_transacao(conta, Saque(valor))

            elif opcao == "e":
                exibir_extrato(conta)

        elif opcao == "lc":
            for conta in contas:
                print("=" * 40)
                print(f"Agência: {conta.agencia}")
                print(f"Conta: {conta.numero}")
                print(f"Titular: {conta.cliente.nome}")

        elif opcao == "q":
            break

        else:
            print("\n@@@ Opção inválida! @@@")


main()



   
      
  








