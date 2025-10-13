from crud import *
from datetime import datetime
from util import *

def entrar_produtos(produtos):

    lista_produtos = []
    
    id_produto = entrar_inteiro("Entre com o id do produto:")
    
    if buscar_produto(id_produto, produtos) is not None:

        nome_produto = get_produto_nome(id_produto, produtos)
        preco_produto = get_produto_preco(id_produto, produtos)
        

        qtd_produto = entrar_positivo("Entre com a quantidade de pedidos:")

        total_compra = qtd_produto * preco_produto

        if qtd_produto is not None:

          lista_produtos.append(nome_produto)
          lista_produtos.append(preco_produto)
          lista_produtos.append(qtd_produto)
          lista_produtos.append(total_compra)
          return lista_produtos

    
    print("Produto não encontrado.")
    return None

def imprimir_recibo(cliente, produtos):
    data = datetime.now().strftime("%d/%m/%Y %H:%M")
    print(f"\nCliente {cliente}")
    print(f"Data: {data}")
    print()
    print(f"{'Item':<5} {'Produto':<10} {'Quant.':<12} {'Preço':<7} {'Total':<7}")
    print("-" * 40)

    total_geral = 0

    for i, produto in enumerate(produtos, start=1):
        nome_produto = produto[0]
        preco = produto[1]
        quantidade = produto[2]
        total_produto = produto[3]
        
        total_geral += total_produto
        print(f"{i:<5} {nome_produto:<10} {quantidade:<12} {preco:<7} {total_produto:<7}")

    print()
    print(f"produto: {len(produto)}")
    print(f"Total: {total_geral:.2f}")
    print("-" * 40)


def fechamento_caixa(todos_os_recibos):
    print("\n\n=== FECHAMENTO DE CAIXA ===")
    total_clientes = len(todos_os_recibos)
    total_itens = 0
    total_caixa = 0

    for i, recibo in enumerate(todos_os_recibos, start=1):
        print(f"\nCliente {i}:")
        subtotal = 0
        for item in recibo:
            qtd = item[2]
            total = item[3]
            subtotal += total
            total_itens += qtd
        total_caixa += subtotal
        print(f"Total: {subtotal:.2f}")
    
    print("\n============================")
    print(f"Total de clientes: {total_clientes}")
    print(f"Total de itens vendidos: {total_itens}")
    print(f"Total arrecadado: {total_caixa:.2f}")
    print("============================\n")

 
   
