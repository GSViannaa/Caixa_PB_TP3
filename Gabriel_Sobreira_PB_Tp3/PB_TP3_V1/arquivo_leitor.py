import os.path


ARQ = "produtos.csv"
DIR = os.path.dirname(os.path.abspath(__file__))
ARQ = os.path.join(DIR, ARQ)

def ler_produtos():
  
   produtos = []

   try:
        with open(ARQ, "r", encoding="utf-8") as arquivo:
           
           linha = arquivo.readline
           
           for linha in arquivo:
             
              campos = linha.split(",")
              id, nome, quantidade, preco = int(campos[0]), campos[1], int(campos[2]), float(campos[3])
              produtos.append([id, nome, quantidade, preco])
             
             
        arquivo.close()
   except: 
        print("Erro leitura arquivo")

   return produtos

