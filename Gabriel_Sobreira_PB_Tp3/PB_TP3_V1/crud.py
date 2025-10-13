from util import *

def buscar_produto(id, produtos):

    for produto in produtos:

        if produto[0] == id:
            return produto
        
    print("Produto não encontrado")
    return None


def get_produto_nome(id, produtos):
    
    produto = buscar_produto(id, produtos)

    if produto is not None:
      return produto[1]
    
def get_produto_preco(id, produtos):
    
    produto = buscar_produto(id, produtos)

    if produto is not None:
      return produto[3]
 
def alterar_quantidade(produto, quantidade):
   
   if produto is not None:
        produto[2] -= quantidade
  

def alterar_produtos(produtos_vendidos,produtos):

    for produto in produtos_vendidos:
     
     produto_para_alterar =  buscar_produto(produto[0], produtos) 
     if produto_para_alterar is not None:
      alterar_quantidade(produto_para_alterar, produto[2])


def atualizar_estoque(produtos_vendidos, todos_os_produtos):
    for item in produtos_vendidos:
        nome = item[0]
        preco = item[1]
        quantidade_vendida = item[2]

        for produto in todos_os_produtos:
            if produto[1] == nome and produto[3] == preco:
                produto[2] -= quantidade_vendida
                break