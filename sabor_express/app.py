import os

def exibir_nome_do_programa():  

    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
\n""")

def exibir_opcoes():
    print("1. Cadastrar restaurante")
    print("2. Listar restaurante")
    print("3. Ativar restaurante")
    print("4. Sair\n")

def finalizar_app():
    os.system("cls")
    print("Encerrando programinha...\n")

def escolher_opcao():
    opcao_escolhida = int(input("Escolha uma opção: "))

    #if no portugues e como se fosse se (se for variavel faça tal coisa)
    #elif no portugues é como se fosse ou - ou SE NÃO FOR
    #else no portugues é usada ao final de tudo - Se não for enhuma das opções anteriores

    if  opcao_escolhida == 1:
        print("Cadastrar restaurante")
    elif opcao_escolhida == 2:
        print(" Listar restaurante")
    elif opcao_escolhida == 3:
        print(" Ativar restaurante")
    else:
        finalizar_app()

def main():
    exibir_nome_do_programa()
    exibir_opcoes()  
    escolher_opcao()

if __name__ == "__main__":
    main()