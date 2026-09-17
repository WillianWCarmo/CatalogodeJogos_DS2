from sqlalchemy import Column, Integer, String, Float
from database import Base

class Receita(Base):
    __tablename__ = "receita"
    id = Column(Integer, autoincrement=True, primary_key=True)
    nome = Column(String(100), nullable=False)
    descricao = Column(String(250))
    valor = Column(Float, nullable=False, default=0.0)
    
    def __init__(self, nome:str, descricao:str, valor:float):
        self.nome = nome,
        self.descricao = descricao,
        self.valor = float(valor)