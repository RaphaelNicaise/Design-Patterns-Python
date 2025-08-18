from abc import ABC,abstractmethod

class Notificacion(ABC): 
    @abstractmethod
    def enviar(self):
        pass

class NotificacionMail(Notificacion):
    def enviar(self, mensaje, receptor, headers):
        print(f"Enviando '{mensaje}' via Mail a {receptor} con headers {headers}")

class NotificacionSMS(Notificacion):
    def enviar(self, mensaje, receptor, headers=None):
        print(f"Enviando '{mensaje}' via SMS a {receptor}  ")

class NotificacionWP(Notificacion):
    def enviar(self, mensaje, receptor, headers=None):
        print(f"Enviando '{mensaje}' via Whatsapp a {receptor} ")


class CreadorNotificacion(ABC):
    @abstractmethod
    def crearNotificacion(self):
        pass

class CreadorNotificacionMail(CreadorNotificacion):
    def crearNotificacion(self):
        return NotificacionMail()
    
class CreadorNotificacionSMS(CreadorNotificacion):
    def crearNotificacion(self):
        return NotificacionSMS()
    
class CreadorNotificacionWP(CreadorNotificacion):
    def crearNotificacion(self):
        return NotificacionWP()

if __name__ == "__main__":
    creador_mail = CreadorNotificacionMail()
    creador_sms = CreadorNotificacionSMS()
    creador_wp = CreadorNotificacionWP()

    
    notificacion_mail = creador_mail.crearNotificacion()
    notificacion_sms = creador_sms.crearNotificacion()
    notificacion_wp = creador_wp.crearNotificacion()

    mensaje = "Mensaje"
    receptor = "usuario@example.com"
    headers = {"Asunto": "Notificación"}

    notificacion_mail.enviar(mensaje, receptor, headers)
    notificacion_sms.enviar(mensaje, receptor)
    notificacion_wp.enviar(mensaje, receptor)
