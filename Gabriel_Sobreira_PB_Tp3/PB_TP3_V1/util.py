
def entrar_inteiro(msg):
   
 while (True):
       
    try:
        entrada = int(input(msg))

        break
    except ValueError as e:

        print("Erro: Valor invalido")

 return entrada

def entrar_positivo(msg):
   
     while True:
      
       try: 
          entrada = int(input(msg))

          break
       except ValueError as e: 
         
         print("Erro: Valor inválido")

     if entrada <= 0:
        print("Erro: Valor negativo")
     else:
        return entrada
   