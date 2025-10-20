import sqlite3
import os
from models.produtos import Produto

class BancoProduto:

    def __init__(self, nome_banco="produtos.db"):

        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        data_dir = os.path.join(base_dir, "data")
        os.makedirs(data_dir, exist_ok=True)

        self.caminho = os.path.join(data_dir, nome_banco)
        self._criar_tabela()

    def _criar_tabela(self):
     
        with sqlite3.connect(self.caminho) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS produtos (
                    id INTEGER PRIMARY KEY,
                    nome TEXT NOT NULL,
                    quantidade INTEGER NOT NULL,
                    preco REAL NOT NULL
                )
            """)
            conn.commit()

    def ler(self):

        produtos = []
        with sqlite3.connect(self.caminho) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, nome, quantidade, preco FROM produtos")
            for id_, nome, qtd, preco in cursor.fetchall():
                produtos.append(Produto(id_, nome, qtd, preco))

        print(f"[OK] {len(produtos)} produtos carregados de {self.caminho}")
        return produtos

    def gravar(self, produtos):
        with sqlite3.connect(self.caminho) as conn:
            cursor = conn.cursor()

            for p in produtos:
                cursor.execute("""
                    INSERT INTO produtos (id, nome, quantidade, preco)
                    VALUES (?, ?, ?, ?)
                    ON CONFLICT(id) DO UPDATE SET
                        nome = excluded.nome,
                        quantidade = excluded.quantidade,
                        preco = excluded.preco
                """, (p.id, p.nome, p.quantidade, p.preco))

            conn.commit()

        print(f"[OK] {len(produtos)} produtos gravados em {self.caminho}")
