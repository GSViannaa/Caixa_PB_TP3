from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_dir = os.path.join(base_dir, "data")
os.makedirs(data_dir, exist_ok=True)

DB_PATH = os.path.join(data_dir, "produtos.db")
DATABASE_URL = f"sqlite:///{DB_PATH}"

Base = declarative_base()

engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine)
