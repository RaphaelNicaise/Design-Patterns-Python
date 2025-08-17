# Gestión de conexión a base de datos
# Para evitar múltiples conexiones innecesarias, una sola instancia gestiona el acceso a la base de datos.

class ConnDDBB:
    __instance = None

    def __init__(self, host, port, database, pwd, user="root"):
        self.__host = host
        self.__port = port
        self.__database = database
        self.__pwd = pwd
        self.__user = user

        if ConnDDBB.__instance != None:
            raise Exception("La clase ya a sido creada")
        else:
            ConnDDBB.__instance = self

    @staticmethod
    def getInstance():
        if ConnDDBB.__instance == None:
            ConnDDBB()
        return ConnDDBB.__instance
    
    def __repr__(self):
        return f'ConnDB("{self.host}","{self.port}","{self.database}","{self.pwd}","{self.user}")'

    # getters
    @property
    def host(self): return self.__host
    
    @property
    def port(self): return self.__port
    
    @property
    def database(self): return self.__database

    @property
    def pwd(self): return self.__pwd
    
    @property
    def user(self): return self.__user


if __name__ == "__main__":
    ConnDDBB(
        "127.0.0.1","5000","db1","1234","root" # creamos instancia
    )
    conn1 = ConnDDBB.getInstance()
    conn2 = ConnDDBB.getInstance()

    print(conn1)
    print(conn2)
    print(conn1 == conn2)