from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DB_connection:
    
    def __init__(self):
        self.__connection_string__ = 'mysql+pymysql://root:123456@172.17.0.3/mydb'
        self.session = None
    
    #cria conexão com o banco de dados
    def __enter__(self):
        engine = create_engine(self.__connection_string__)
        session_maker = sessionmaker()
        self.session = session_maker(bind=engine)

        return self

    #encerra conexão com db
    def __exit__(self,exc_type,exc_val,exc_tb,):
        self.session.close()
        