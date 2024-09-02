# Função para realizar depósito
def deposito(saldo: float, valor: float, extrato: str) -> tuple:
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

# Função para realizar saque
def saque(*, saldo: float, valor: float, extrato: str, limite: float, numero_saques: int, LIMITE_SAQUES: int) -> tuple:
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato, numero_saques

# Função para visualizar o extrato
def extrato(saldo: float, *, extrato: str) -> None:
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

# Função para criar um novo usuário
def criar_usuario(nome: str, data_nascimento: str, cpf: str, endereco: str, usuarios: list) -> None:
    if any(usuario['cpf'] == cpf for usuario in usuarios):
        print("CPF já cadastrado.")
        return
    usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco})
    print("Usuário cadastrado com sucesso.")

# Função para criar uma nova conta corrente
def criar_conta_corrente(usuario_cpf: str, contas: list, usuarios: list) -> None:
    if not any(usuario['cpf'] == usuario_cpf for usuario in usuarios):
        print("Usuário não encontrado.")
        return
    num_conta = len(contas) + 1
    contas.append({'agencia': '0001', 'numero_conta': num_conta, 'cpf_usuario': usuario_cpf})
    print(f"Conta {num_conta} criada com sucesso para o usuário com CPF {usuario_cpf}.")

# Função para listar contas
def listar_contas(contas: list) -> None:
    for conta in contas:
        print(f"Agência: {conta['agencia']}, Número da Conta: {conta['numero_conta']}, CPF do Usuário: {conta['cpf_usuario']}")

# Função para listar usuários
def listar_usuarios(usuarios: list) -> None:
    for usuario in usuarios:
        print(f"Nome: {usuario['nome']}, Data de Nascimento: {usuario['data_nascimento']}, CPF: {usuario['cpf']}, Endereço: {usuario['endereco']}")

# Código principal
menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[c] Cadastrar Usuário
[n] Criar Conta Corrente
[l] Listar Contas
[u] Listar Usuários
[q] Sair
=> """

saldo = 0
limite = 500
extrato_str = ""
numero_saques = 0
LIMITE_SAQUES = 3

usuarios = []
contas = []

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato_str = deposito(saldo, valor, extrato_str)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato_str, numero_saques = saque(saldo=saldo, valor=valor, extrato=extrato_str, limite=limite, numero_saques=numero_saques, LIMITE_SAQUES=LIMITE_SAQUES)

    elif opcao == "e":
        extrato(saldo, extrato=extrato_str)

    elif opcao == "c":
        nome = input("Nome: ")
        data_nascimento = input("Data de Nascimento (dd/mm/aaaa): ")
        cpf = input("CPF (somente números): ")
        endereco = input("Endereço (logradouro, número, bairro - cidade/sigla estado): ")
        criar_usuario(nome, data_nascimento, cpf, endereco, usuarios)

    elif opcao == "n":
        usuario_cpf = input("CPF do usuário: ")
        criar_conta_corrente(usuario_cpf, contas, usuarios)

    elif opcao == "l":
        listar_contas(contas)

    elif opcao == "u":
        listar_usuarios(usuarios)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
