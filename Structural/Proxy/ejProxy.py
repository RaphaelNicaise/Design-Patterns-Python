# Sistema de Base de Datos con Control de Acceso

# Objeto real: Conexión directa a BD que puede hacer SELECT, INSERT, UPDATE, DELETE
# Proxy: Verifica rol del usuario antes de cada operación
# Roles: "admin" (todo), "user" (solo SELECT), "guest" (nada)

from abc import ABC, abstractmethod

class Permissions:
    # objeto que define los permisos de un perfil
    def __init__(self,select=0,insert=0,update=0,delete=0):
        for arg in (select,insert,update,delete):
            Permissions.validate_value(arg)
        self.permissions = dict(select=select,insert=insert,update=update,delete=delete)
    
    @staticmethod
    def validate_value(value:int):
        if value not in (0,1):
            raise ValueError("Los permisos deben ser 0 o 1")

    def change_permission(self,operation:str,value:int):
        if operation not in self.permissions.keys():
            raise ValueError(f"Operación {operation} no válida")
        Permissions.validate_value(value)
        self.permissions[operation] = value

# Definición de perfiles con diferentes permisos
class Profile:
    def __init__(self):
        self.permissions = None

    def show_permissions(self):
        return self.permissions.permissions
    
class Admin(Profile):
    """
    Admin tiene todos los permisos
    """
    def __init__(self):
        self.permissions = Permissions(
            select=1,
            insert=1,
            update=1,
            delete=1
        )

class User(Profile):
    def __init__(self):
        self.permissions = Permissions(
            select=1
        )
        
class Guest(Profile):
    def __init__(self):
        self.permissions = Permissions(
            select=0
        )

class DatabaseInterface(ABC):
    # Interfaz común para Database y DatabaseProxy
    @abstractmethod
    def query(self, sql:str):
        pass

class Database(DatabaseInterface):
    # Objeto real que ejecuta las consultas
    def query(self, sql:str):
        print(f"Ejecutando consulta: {sql}")

class DatabaseProxy(DatabaseInterface):
    # Proxy que controla el acceso a la base de datos
    # Le agrega un perfil de usuario para verificar permisos
    def __init__(self, profile:Profile):
        self.profile = profile
        self.database = Database()

    def query(self, sql:str):
        # Buscar si alguna palabra clave de permisos esta en el SQL
        operation = None
        for op in self.profile.permissions.permissions.keys():
            if op.lower() in sql.lower():
                operation = op
                break

        if not operation:
            return
        
        if self.profile.permissions.permissions[operation] == 1: # valida si puede
            self.database.query(sql)
        else:
            print(f"Acceso denegado a {self.profile.__class__.__name__} para la operación {operation}")

if __name__ == "__main__":
    admin = Admin()
    print("Admin:", admin.show_permissions())

    proxyAdmin = DatabaseProxy(admin)
    proxyAdmin.query("SELECT * FROM users") # ya que es admin, puede

    proxyAdmin.query("UPDATE FROM users WHERE id=1") # ya que es admin, puede
    
    proxyGuest = DatabaseProxy(Guest())
    print("Guest:", proxyGuest.profile.show_permissions())
    proxyGuest.query("SELECT * FROM users") # no puede, no tiene permisos