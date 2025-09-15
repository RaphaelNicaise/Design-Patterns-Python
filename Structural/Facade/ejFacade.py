class SubsitemaInventario:
    def __init__(self):
        self._inventario = []
        self.__init_sys() # inicializa el inventario con productos

    def __init_sys(self):
        productos = [
            {"nombre": "Producto A", "precio": 100, "stock": 10},
            {"nombre": "Producto B", "precio": 150, "stock": 5},
            {"nombre": "Producto C", "precio": 200, "stock": 8}
        ]
        self._inventario.extend(productos)

    def verificar_stock(self, producto, cantidad):
        """ verifica si hay suficiente stock del producto solicitado """
        for item in self._inventario:
            if item["nombre"] == producto and item["stock"] >= cantidad:
                return True
        return False
    
    def actualizar_stock(self, producto, cantidad):
        """ actualiza el stock del inventario restando la cantidad vendida """
        for item in self._inventario:
            if item["nombre"] == producto:
                item["stock"] -= cantidad
                print(f"Stock actualizado: {item['nombre']} ahora tiene {item['stock']} unidades.")
                return True
            
        return False
    
    def get_precio(self, producto):
        """ obtiene el precio del producto """
        for item in self._inventario:
            if item["nombre"] == producto:
                return item["precio"]
        return None
    
class SubsistemaPagos:
    def procesar_pago(self, metodo, monto):
        """ simula el procesamiento de un pago """
        print(f"Procesando pago de {monto} usando {metodo}")
        return True
    
    def reembolsar_pago(self, metodo, monto):
        """ simula el reembolso de un pago """
        print(f"Reembolsando {monto} usando {metodo}")
        return True

class SubsistemaEnvios:
    def calcular_costo_envio(self, direccion):
        """ simula el calculo del costo de envio basado en la direccion """
        print(f"Calculando costo de envio a {direccion}")
        return 50  # costo fijo para simplificar

    def realizar_envio(self, direccion):
        """ simula la realizacion del envio """
        print(f"Realizando envio a {direccion}")
        return True
    
class SubsistemaNotificaciones:
    def enviar_confirmacion(self, email):
        """ simula el envio de una confirmacion por email """
        print(f"Enviando confirmacion a {email}")
        return True
    
    def enviar_actualizacion_envio(self, email):
        """ simula el envio de una actualizacion del estado del envio """
        print(f"Enviando actualizacion de envio a {email}")
        return True

class Facade: # interfaz para interactuar con los subsistemas de forma sencilla
    def __init__(self):
        self._sysInventario = SubsitemaInventario()
        self._sysPagos = SubsistemaPagos()
        self._sysEnvios = SubsistemaEnvios()
        self._sysNotificaciones = SubsistemaNotificaciones()

    def cancelar_pedido(self):
        print("Cancelando pedido...")

    def procesar_pedido(self, producto, cantidad, metodo_pago, direccion_envio, email_cliente):
        print("Iniciando procesamiento de pedido...")
        
        if not self._sysInventario.verificar_stock(producto, cantidad):
            self.cancelar_pedido()
            return False
        
        costo_envio = self._sysEnvios.calcular_costo_envio(direccion_envio)
        costo_total = self._sysInventario.get_precio(producto) * cantidad + costo_envio

        self._sysPagos.procesar_pago(metodo_pago, costo_total)
        self._sysInventario.actualizar_stock(producto, cantidad)

        self._sysNotificaciones.enviar_confirmacion(email_cliente)
        self._sysEnvios.realizar_envio(direccion_envio)
        self._sysNotificaciones.enviar_actualizacion_envio(email_cliente)
        
Facade().procesar_pedido("Producto A", 2, "debito", "Mi casita 123", "raphanicaise1@gmail.com")