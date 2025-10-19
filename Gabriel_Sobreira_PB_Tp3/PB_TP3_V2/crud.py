from util import *

def buscar_produto(id, produtos):

    for produto in produtos:

        if produto["id"] == id:
            return produto
        
    print("Produto não encontrado")
    return None


def get_produto_nome(id, produtos):
    
    produto = buscar_produto(id, produtos)

    if produto is not None:
      return produto["nome"]
    
def get_produto_preco(id, produtos):
    
    produto = buscar_produto(id, produtos)

    if produto is not None:
      return produto["preco"]
 
def alterar_quantidade(produto, quantidade):
   
   if produto is not None:
        produto["quantidade"] -= quantidade
  

def alterar_produtos(produtos_vendidos,produtos):

   for produto_vendido in produtos_vendidos:
        nome_vendido = produto_vendido["nome"]
        quantidade_vendida = produto_vendido["quantidade"]

        produto_para_alterar = next((p for p in produtos if p["nome"] == nome_vendido), None)

        if produto_para_alterar is not None:
            alterar_quantidade(produto_para_alterar, quantidade_vendida)

def atualizar_estoque(produtos_vendidos, todos_os_produtos):

    for item in produtos_vendidos:
        nome = item["nome"]
        preco = item["preco"]
        quantidade_vendida = item["quantidade"]

        for produto in todos_os_produtos:
            if produto["nome"] == nome and produto["preco"] == preco:
                produto["quantidade"] -= quantidade_vendida
                break