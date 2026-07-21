# 1- 🏦 Sistema Bancário em Python - Bootcamp LuizasLab

Este projeto é uma simulação de um **sistema bancário simples**, desenvolvido em Python para fins de estudo e prática de programação.  
Ele permite realizar operações básicas como **depósitos, saques, criação de usuários e contas**, além de exibir o extrato de movimentações.


---

## 🚀 Funcionalidades

- 📋 **Menu interativo** para navegação entre opções.  
- 💰 **Depósito**: valida o valor e atualiza saldo e extrato.  
- 💸 **Saque**: controla limite de valor, quantidade máxima de saques e saldo disponível.  
- 📑 **Extrato**: exibe todas as movimentações realizadas e o saldo atual.  
- 👤 **Cadastro de usuários**: cria novos usuários com CPF, nome, data de nascimento e endereço.  
- 🏦 **Cadastro de contas**: associa contas a usuários existentes.  
- 📂 **Listagem de contas**: mostra todas as contas criadas.  

---

## 🛠️ Tecnologias utilizadas

- [Python 3](https://www.python.org/)  
- Estruturas de dados: listas e dicionários  
- Funções e modularização  

---

## 📂 Estrutura do projeto  

- `sistema_BK.py` → código principal com todas as funções do sistema.  
- Funções principais:
- `menu()`
- `depositar()`
- `sacar()`
- `exibir_extrato()`
- `criar_usuario()`
- `filtrar_usuario()`
- `criar_conta()`
- `listar_contas()`

# 2-  💰 Sistema Bancário em Python (POO)   Bootcamp LuizasLab

Projeto de um **sistema bancário desenvolvido em Python**, utilizando **Programação Orientada a Objetos (POO)** e seguindo um **modelo UML**, substituindo o uso de dicionários por classes.

Este projeto é ideal para **estudos, desafios técnicos, provas acadêmicas e portfólio profissional**.

---

## 📌 Funcionalidades

- Criar usuários (Pessoa Física)
- Criar contas bancárias (Conta Corrente)
- Realizar depósitos
- Realizar saques com:
 - Limite de valor
- Limite diário de saques
- Consultar extrato
- Listar contas cadastradas
- Registro de todas as transações

  ## 🧩 Estrutura do Projeto

O sistema utiliza os principais **pilares da Programação Orientada a Objetos**:

- **Encapsulamento**
- **Herança**
- **Abstração**
- **Polimorfismo**

### Principais Classes

- `Cliente`
- `PessoaFisica`
- `Conta`
- `ContaCorrente`
- `Historico`
- `Transacao` (classe abstrata)
- `Deposito`
- `Saque`

---

## ⚙️ Tecnologias Utilizadas

- Python 3.x
- Programação Orientada a Objetos
- Git e GitHub
- Terminal / VS Code

# 3- ✊ Jogo Jo-Ken-Pô em Python

Um jogo clássico de **Pedra, Papel e Tesoura** desenvolvido em **Python**, utilizando a interface gráfica do **Tkinter** e manipulação de imagens com a biblioteca **Pillow**. O projeto conta com um design limpo, placar dinâmico em tempo real e lógica de jogadas automatizada para o computador.


## 🚀 Funcionalidades

* **Interface Gráfica (GUI):** Janela estilizada e personalizada com tema moderno via Tkinter.
* **Placar Dinâmico:** Contagem automática e em tempo real dos pontos do Jogador e do Computador.
* **Inteligência do Oponente:** Escolhas automáticas e aleatórias feitas pelo computador a cada rodada usando a biblioteca `random`.
* **Suporte Visual:** Botões interativos com ícones para representar visualmente as jogadas (Pedra, Papel e Tesoura).


## 🛠️ Tecnologias Utilizadas

* **Python 3.x**
* **Tkinter** (Interface gráfica nativa)
* **Pillow / PIL** (Redimensionamento e manipulação de imagens)
* **Random** (Sorteio das jogadas do computador)


