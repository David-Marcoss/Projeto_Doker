from .entidades.models import endereco as EnderecoModel
from .config.db_connection import DB_connection

#operações com o bd
class enderecos_op:

    #insere um endereco no bd
    def insert(self,cep,rua,cidade,estado):
        #whith abre uma conexao com o bd e encerra a conexao depois que todos os comandos forem execultados
        with DB_connection() as db:
            
            try:
                new_endereco = EnderecoModel(cep=cep,rua=rua,cidade=cidade,estado=estado)
                db.session.add(new_endereco)
                db.session.commit()
                

                return True
            
            except:
        
                return False
