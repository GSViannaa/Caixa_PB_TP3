from sqlalchemy import Column, Integer, String, Float
from models.base import Base

class Produto(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    quantidade = Column(Integer, nullable=False)
    preco = Column(Float, nullable=False)

    def reduzir_estoque(self, quantidade):

        if quantidade <= self.quantidade:
            self.quantidade -= quantidade
            print(f"[OK] Estoque atualizado: {self.nome} agora tem {self.quantidade} unidade(s).")

        else:
              print(f"[AVISO] Estoque insuficiente para o produto '{self.nome}'. "
              f"Disponível: {self.quantidade}, solicitado: {quantidade}.")
         
    def __repr__(self):
        return f"{self.id} - {self.nome} (Qtd: {self.quantidade}, Preço: {self.preco:.2f})"