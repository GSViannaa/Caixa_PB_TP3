from arquivo_leitor import *
from menu import *
from caixa_util import *

produtos = ler_produtos()
produtos_vendidos = []

numero_cliente = 1

def atender_cliente(produtos, numero_cliente, produtos_vendidos):
    produtos_por_cliente = []

    while True:
        entrada = menu_atendimento()

        if entrada == 1:
            produto = entrar_produtos(produtos)
            if produto:
                produtos_por_cliente.append(produto)
                print("Produto adicionado.")

        elif entrada == 2:
            imprimir_recibo(numero_cliente, produtos_por_cliente)
            produtos_vendidos.append(produtos_por_cliente)
            print(f"Atendimento ao cliente {numero_cliente} finalizado.\n")

            atualizar_estoque(produtos_por_cliente, produtos)
            gravar_produtos(produtos) 
            
            return numero_cliente + 1  
        
        else:
            print("Entrada inválida no menu de atendimento.")

def caixa(produtos):
    numero_cliente = 1
    produtos_vendidos = []

    while True:
        opcao = menu_entarda_opcoes()

        if opcao == 1:
            numero_cliente = atender_cliente(produtos, numero_cliente, produtos_vendidos)

        elif opcao == 2:
            print("Fechando caixa...")
            fechamento_caixa(produtos_vendidos)
            break
        
        else:
            print("Opção inválida. Tente novamente.")


 
caixa(produtos)