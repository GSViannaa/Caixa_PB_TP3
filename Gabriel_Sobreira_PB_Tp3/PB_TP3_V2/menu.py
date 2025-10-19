from util import entrar_inteiro

def menu_entarda_opcoes():

    print("======== Caixa ========")
    print("[1] - iniciar novo atendimento")
    print("[2] - fechar caixa")

    opcao = entrar_inteiro("Esolha uma opção:")

    return opcao

def menu_atendimento():

    print("======== Caixa ========")
    print("[1] - Escanear produto")
    print("[2] - Encerrar atendimento")

    opcao = entrar_inteiro("Escolha uma opção:")

    return opcao