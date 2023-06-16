from sqlalchemy import Column,Integer,String
from src.config import Base


#declaração da tabela 
class endereco(Base):
    __tablename__ = "enderecos"

    id = Column(Integer,primary_key=True)
    cep = Column(String,unique=True)
    rua = Column(String)
    cidade = Column(String)
    estado = Column(String)

    def __repr__(self):
        return self.cep