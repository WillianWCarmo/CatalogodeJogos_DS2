from database import Session

class ReceitaRepository:
    def __init__(self):
        self.__session = Session()
        
    def cadastrar(self, receita):
        self.__session.add(receita)
        self.__session.commit()
        self.__session.close()