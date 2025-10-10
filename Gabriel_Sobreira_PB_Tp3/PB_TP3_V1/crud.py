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


