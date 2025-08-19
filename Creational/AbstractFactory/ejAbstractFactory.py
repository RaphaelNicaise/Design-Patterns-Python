from abc import ABC, abstractmethod

# Factory Abstracto
class AbstractDBFactory(ABC):
    
    @abstractmethod
    def create_connection(self):
        pass

    @abstractmethod
    def create_query(self):
        pass

# Factorys concretas
class FactoryMySQL(AbstractDBFactory):
    def create_connection(self):
        return MySQLConnection()    

    def create_query(self):
        return MySQLQuery()

class FactoryPostgres(AbstractDBFactory):
    def create_connection(self):
        return PostgresConnection()

    def create_query(self):
        return PostgresQuery()

# Productos abstractos
class Connection(ABC):
    @abstractmethod
    def connect(self):
        pass

class Query(ABC):
    @abstractmethod
    def execute(self, query: str):
        pass

# Clases de los productos concretos de MySQL
class MySQLConnection(Connection):
    def connect(self):
        print("Connecting to MySQL")
    
class MySQLQuery(Query):
    def execute(self, query):
        print(f"Ejecutando query en MySQL -> {query}")

# Clases de los productos concretos de Postgres

class PostgresConnection(Connection):
    def connect(self):
        print("Connecting to Postgres")
    
class PostgresQuery(Query):
    def execute(self, query):
        print(f"Ejecutando query en Postgres -> {query}")
    
def main():
    factory_mysql = FactoryMySQL() # la fabrica para los productos mysql

    conn = factory_mysql.create_connection() # creamos conexion
    print(conn) # -> <__main__.MySQLConnection object at 0x000001E3B9A46BA0>

    conn.connect() # nos conectamos

    query = factory_mysql.create_query().execute("SELECT * FROM productos")
if __name__ == "__main__":
    main()