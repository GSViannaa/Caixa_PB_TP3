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

        if qtd_produto is not None:

          lista_produtos.append(nome_produto)
          lista_produtos.append(preco_produto)
          lista_produtos.append(qtd_produto)
          return lista_produtos


def imprimir_recibo(cliente, itens):

    data = datetime.now().strftime("%d/%m/%Y %H:%M")
    print(f"Cliente {cliente}")
    print(f"Data: {data}")
    print()
    print(f"{'Item':<5} {'Produto':<10} {'Quant.':<7} {'Preço':<7} {'Total':<7}")
    print("-" * 40)

    total_geral = 0

    for i, (produto, quantidade, preco) in enumerate(itens, start=1):
        total_item = quantidade * preco
        total_geral += total_item
        print(f"{i:<5} {produto:<10} {quantidade:<7} {preco:<7} {total_item:<7}")

    print()
    print(f"Items: {len(itens)}")
    print(f"Total: {total_geral}")
    print("-" * 40)


 
   
