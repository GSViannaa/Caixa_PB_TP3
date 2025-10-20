import csv
import os
import sqlite3

def migrar_csv_para_sqlite(csv_nome="Produtos.csv", db_nome="produtos.db"):

    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(base_dir, "data")
    csv_path = os.path.join(data_dir, csv_nome)
    db_path = os.path.join(data_dir, db_nome)

    if not os.path.exists(csv_path):

        print(f"[ERRO] Arquivo CSV não encontrado em {csv_path}")
        return

    os.makedirs(data_dir, exist_ok=True)
    conn = sqlite3.connect(db_path)
    
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            quantidade INTEGER NOT NULL,
            preco REAL NOT NULL
        )
    """)

    produtos_inseridos = 0

    with open(csv_path, "r", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)
       
        for linha in leitor:

            if not linha:
                continue

            try:
                id_, nome, qtd, preco = linha
                cursor.execute("""
                    INSERT OR REPLACE INTO produtos (id, nome, quantidade, preco)
                    VALUES (?, ?, ?, ?)
                """, (int(id_), nome, int(qtd), float(preco)))
                produtos_inseridos += 1
            except Exception as e:
                print(f"[ERRO] Falha ao inserir linha {linha}: {e}")

    conn.commit()
    conn.close()

    print(f"[OK] Migração concluída. {produtos_inseridos} produtos inseridos no banco {db_path}.")


if __name__ == "__main__":
    migrar_csv_para_sqlite()