from crud import *
from datetime import datetime
from tabulate import tabulate
from util import *

def entrar_produtos(produtos):

    id_produto = entrar_inteiro("Entre com o id do produto:")
    produto = buscar_produto(id_produto, produtos)
    
    if buscar_produto(id_produto, produtos) is not None:

   
        if produto is not None:
          
          nome = produto["nome"]
          preco = produto["preco"]
          qtd_produto = entrar_positivo("Entre com a quantidade de produtos:")
          total = qtd_produto * preco
        
          return {
            "nome": nome,
            "preco": preco,
            "quantidade": qtd_produto,
            "total": total
                 }


    print("Produto não encontrado.")
    return None

def imprimir_recibo(cliente, produtos):
    data = datetime.now().strftime("%d/%m/%Y %H:%M")
    print(f"Cliente {cliente}")
    print(f"Data: {data}\n")
    print(f"{'Item':<6}{'Produto':<20}{'Quant.':<10}{'Preço':<10}{'Total':<10}")
    print(f"{'-'*6}{'-'*20}{'-'*10}{'-'*10}{'-'*10}")

    total_geral = 0
    for i, produto in enumerate(produtos, start=1):
        nome = produto["nome"]
        preco = produto["preco"]
        qtd = produto["quantidade"]
        total = produto["total"]
        total_geral += total
        print(f"{i:<6}{nome:<20}{qtd:<10}{preco:<10.2f}{total:<10.2f}")

    print(f"\nTotal: {total_geral:.2f}")

def verificar_estoque(produtos):

    produtos_sem_estoque = []

    for p in produtos:

        if p["quantidade"] <=0: 
            produtos_sem_estoque.append(p["nome"])

    return produtos_sem_estoque

def fechamento_caixa(todos_os_recibos, produtos):

  
    produtos_sem_estoque = verificar_estoque(produtos)

    print("\n\n=== FECHAMENTO DE CAIXA ===")
    total_clientes = len(todos_os_recibos)
    total_itens = 0
    total_caixa = 0

    for i, recibo in enumerate(todos_os_recibos, start=1):
        print(f"\nCliente {i}:")
        subtotal = 0

        for item in recibo:
            qtd = item["quantidade"]
            total = item["total"]

            subtotal += total
            total_itens += qtd

        total_caixa += subtotal
        print(f"Total: {subtotal:.2f}")
    
    print("\n============================")
    print(f"Total de clientes: {total_clientes}")
    print(f"Total de itens vendidos: {total_itens}")
    print(f"Total arrecadado: {total_caixa:.2f}")
    print("============================\n")

    if produtos_sem_estoque:
        print("\n========= Produtos sem estoque ==========")
        for p in produtos_sem_estoque:
            print(f"O produto {p} ficou sem estoque")
        print("===========================================\n")
    else:
        print("Nenhum produto ficou sem estoque.\n")
 
   
