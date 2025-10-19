
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

     if entrada == 0:
        print("Erro:quantidade deve ser maior que zero")
     elif entrada < 0:
        print("Erro: qauntidade deve ser positiva")
     else:
        return entrada
   