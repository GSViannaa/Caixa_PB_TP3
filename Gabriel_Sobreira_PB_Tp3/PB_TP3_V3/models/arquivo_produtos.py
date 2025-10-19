import csv
from models.produtos import Produto
import os

class ArquivoProdutos:
    def __init__(self, nome_arquivo="Produtos.csv"):

        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        data_dir = os.path.join(base_dir, "data")
        self.caminho = os.path.join(data_dir, nome_arquivo)

    def ler(self):
        produtos = []
        try:
            with open(self.caminho, "r", encoding="utf-8") as arquivo:
                leitor = csv.reader(arquivo)

                for linha in leitor:
                    if not linha:  
                        continue
                    id_, nome, qtd, preco = linha
                    produtos.append(Produto(int(id_), nome, int(qtd), float(preco)))

            print(f"[OK] {len(produtos)} produtos carregados de {self.caminho}")

        except FileNotFoundError:
            print(f"[ERRO] Arquivo não encontrado em: {self.caminho}")

        except Exception as e:
            print(f"[ERRO] Falha ao ler produtos: {e}")

        return produtos

    def gravar(self, produtos):

        try:
            os.makedirs(os.path.dirname(self.caminho), exist_ok=True)

            with open(self.caminho, "w", encoding="utf-8", newline="") as arquivo:
                escritor = csv.writer(arquivo)

                for p in produtos:
                    escritor.writerow([p.id, p.nome, p.quantidade, p.preco])

            print(f"[OK] Produtos gravados com sucesso em {self.caminho}")
            
        except Exception as e:
            print(f"[ERRO] Falha ao gravar arquivo: {e}")
