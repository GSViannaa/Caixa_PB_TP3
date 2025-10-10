from arquivo_leitor import *
from menu import *
from caixa_util import *

produtos = ler_produtos()
produtos_vendidos = []
produtos_por_cliente = []

opcao = menu_entarda_opcoes()

numero_cleinte = 1

while True:

 if opcao == 1: 
  
   entrada = menu_atendimento()

   if entrada == 1: 
     produtos_por_cliente.append(entrar_produtos(produtos))
     print(produtos_por_cliente)
   elif entrada == 2:
     imprimir_recibo(numero_cleinte, produtos_por_cliente)
   
 elif opcao == 2:
   print("Fechando caixa...")
   break
 
 else: 
   print("Opção invalida")
   opcao = menu_entarda_opcoes()
 


 
