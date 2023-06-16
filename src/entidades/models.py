from sqlalchemy import Column,Integer,String
from src.config import Base
from sqlalchemy.sql.expression import true


#declaração da tabela 
class endereco(Base):
    __tablename__ = "enderecos"

    idenderecos = Column(Integer,primary_key=True)
    cep = Column(String,unique=true)
    rua = Column(String)
    cidade = Column(String)
    estado = Column(String)

    def __repr__(self):
        return self.cep