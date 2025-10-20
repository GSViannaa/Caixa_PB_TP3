from models.base import Base, engine
from models.produtos import Produto

def criar_banco():
    print("[INFO] Criando tabelas do banco de dados...")
    Base.metadata.create_all(bind=engine)
    print("[OK] Banco de dados criado com sucesso.")
