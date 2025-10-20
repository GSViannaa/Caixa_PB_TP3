from sqlalchemy.orm import Session
from models.produtos import Produto
from models.base import SessionLocal

class BancoProduto:

  
    def __init__(self):
        self.session: Session = SessionLocal()

    def listar_todos(self):
      
        produtos = self.session.query(Produto).all()
        print(f"[OK] {len(produtos)} produtos carregados do banco.")

        return produtos

    def salvar_todos(self, produtos):
        
        for p in produtos:
            existente = self.session.get(Produto, p.id)

            if existente:
                existente.nome = p.nome
                existente.quantidade = p.quantidade
                existente.preco = p.preco

            else:
                self.session.add(p)
        
        self.session.commit()
        print(f"[OK] {len(produtos)} produtos gravados no banco.")

    def adicionar_produto(self, nome, quantidade, preco):
   
        novo_produto = Produto(nome=nome, quantidade=quantidade, preco=preco)
        self.session.add(novo_produto)
        self.session.commit()
        print(f"[OK] Produto '{nome}' adicionado com sucesso.")
        return novo_produto

    def buscar_por_id(self, id_produto):
    
        return self.session.get(Produto, id_produto)

    def fechar(self):
      
        self.session.close()
