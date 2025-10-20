import csv
import os
from models.produtos import Produto
from models.base import SessionLocal
from database.db_setup import criar_banco

def migrar_csv_para_sqlalchemy(csv_nome="Produtos.csv"):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(base_dir, "data")
    csv_path = os.path.join(data_dir, csv_nome)

    if not os.path.exists(csv_path):
        print(f"[ERRO] Arquivo CSV não encontrado em {csv_path}")
        return

    criar_banco()
    session = SessionLocal()

    with open(csv_path, "r", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)
        produtos_inseridos = 0

        for linha in leitor:

            if not linha:
                continue

            try:
                id_, nome, qtd, preco = linha
                produto = Produto(
                    id=int(id_), nome=nome, quantidade=int(qtd), preco=float(preco)
                )
                session.merge(produto)
                produtos_inseridos += 1
                
            except Exception as e:
                print(f"[ERRO] Falha ao inserir linha {linha}: {e}")

    session.commit()
    session.close()
    print(f"[OK] {produtos_inseridos} produtos migrados com SQLAlchemy.")

if __name__ == "__main__":
    migrar_csv_para_sqlalchemy()
