import os #Serve para importar a biblioteca OS (Usada para limpar o terminal)!

def menu():
    menu = """
    ================= MENU =================

    [d] Depositar 
    [s] Sacar 
    [e] Extrato 
    [nc] Nova conta 
    [lc] Listar contas
    [nu] Novo usuário 
    [q] Sair 

    ==> """
    return input((menu)).upper()

def main():
    
    LIMITE_SAQUES = 3 
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    numero_saques = 0
    id_operacao = 0
    usuarios = {}
    contas = {}
    
    usuario = input("Digite o seu e-mail cadastrado: ")
    select_usuario = usuarios.get(usuario)

    if select_usuario == None:
        criar_usuarios(usuarios)
    while True:

        opcao = menu() #Serve para chamar o input, que é retornado pela função "menu()".

        if opcao in ['D', 'S', 'E', 'NC', 'LC', 'NU', 'Q']: #Serve para verificar se o usuário escolheu alguma das opções!
            match opcao:
                case "D":
                    os.system('cls') #Serve para limpar o terminal
                    print("Área de depósito!")
                    tipo_operacao = "Depósito"
                    valor = float(input("Informe o valor do depósito: "))

                    saldo, id_operacao = depositar(usuario, tipo_operacao, usuarios, saldo, valor, id_operacao)

                case "S":
                    os.system('cls') #Serve para limpar o terminal
                    print("Área de saque!")
                    tipo_operacao = "Saque"
                    if numero_saques < LIMITE_SAQUES:
                        valor = float(input("Informe o valor do saque: "))

                        saldo, numero_saques, id_operacao = sacar(usuario, tipo_operacao, usuarios, saldo, valor, numero_saques, id_operacao)
                        
                    else:
                        print(f"Você atingiu o limite de {LIMITE_SAQUES} saques diários!")

                case "E":
                    os.system('cls') #Serve para limpar o terminal
                    extrato(usuarios, usuario, saldo)
                case "NC":
                    os.system('cls') #Serve para limpar o terminal
                    criar_conta(contas, AGENCIA)
                case "LC":
                    os.system('cls') #Serve para limpar o terminal
                    listas_contas(contas)
                case "NU":
                    os.system('cls') #Serve para limpar o terminal
                    criar_usuarios(usuarios)
                case "Q":
                    print("Saindo do Programa")
                    break #Serve para encerrar o programa!
        else: #Caso o usuário não escolha nenhuma das opções acima, vamos exibir a mensagem abaixo para ele!
            print("Por favor, escolha uma opção válida.")
    
def criar_usuarios(usuarios):
    print("Bem vindo ao cadastro de Usuários!")
    nome_usuario = input("Para começar, digite o seu nome: ")
    idade_usuario = int(input("Digite a sua idade: "))
    email_usuario = input("Digite o seu melhor e-mail: ")

    usuario_info = {"nome": nome_usuario, "idade": idade_usuario, "email": email_usuario, "operacoes": {"Depósito" : {}, "Saque": {}}}
    usuarios[f"{email_usuario}"] = usuario_info

    print("Usuário cadastrado com sucesso!")

    return usuarios

def depositar(usuario, tipo_operacao, usuarios, saldo, valor, id_operacao):
    if valor > 0:
        saldo = saldo + valor
        id_operacao += 1
        save_extrato(usuario, tipo_operacao, valor, usuarios, id_operacao)
        print("Depósito realizado com sucesso!")
    else:
        print("O valor deve ser maior do que 0!")

    return saldo, id_operacao

def sacar(usuario, tipo_operacao, usuarios, saldo, valor, numero_saques, id_operacao):
    if valor > 0:
        if valor <= saldo:
            if valor <= 500:
                saldo = saldo - valor
                numero_saques += 1
                id_operacao += 1
                save_extrato(usuario, tipo_operacao, valor, usuarios, id_operacao)
                print("Saque realizado com sucesso!")
            else:
                print("O valor limite por saque é de 500 reais!")
        else:
            print("Saldo não suficiente para a operação!")
    else:
        print("O valor deve ser maior do que 0!")

    return saldo, numero_saques, id_operacao

def save_extrato(usuario, tipo_operacao, valor, usuarios, id_operacao):
    desc_extrato = {"Valor": valor}
    usuarios[f"{usuario}"]["operacoes"][f"{tipo_operacao}"][f"{id_operacao}"] = desc_extrato

    return tipo_operacao, valor, usuarios

def extrato(usuarios, usuario, saldo):
    ext_depositos = usuarios[f"{usuario}"]["operacoes"]["Depósito"]
    ext_saques = usuarios[f"{usuario}"]["operacoes"]["Saque"]
    print("================== Extrato ==================")
    print("Depósitos")
    if ext_depositos:
        for operacao in ext_depositos:
            deposito = ext_depositos[operacao].get("Valor")
            print(deposito)
    else:
        print("Não houveram Depósitos!\n")
    print("=============================================")
    print("Saques")
    if ext_saques:
        for operacao in ext_saques:
            saque = ext_saques[operacao].get("Valor")
            print(saque)
    else:
        print("Não houveram Saques!\n")
    print(f"\nO seu saldo atual é de R${saldo}")

def criar_conta(contas, AGENCIA):
    print("Bem vindo ao cadastro de Contas!")
    nome_completo = input("Digite o seu nome completo: ")
    cod_agencia = AGENCIA
    num_conta = '000001'
    conta_info = {"nome": nome_completo, "agencia": cod_agencia, "conta": num_conta}
    contas[f"{nome_completo}"] = conta_info

    print("Conta criada com sucesso!")

    return contas

def listas_contas(contas):
    list_contas = contas
    print("Bem vindo à lista de Contas!\n")
    if list_contas:
        print(contas)
    else:
        print("Nenhuma conta foi criada!")

    return contas

if __name__ == '__main__': #Serve para informar ao terminal, que a página que estamos executando é a principal!
    main() #Serve para executar a função "main()", que irá organizar as etapas do programa!