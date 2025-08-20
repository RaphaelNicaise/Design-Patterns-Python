"""
Tu interfaz esperada: send(msg)

Clases incompatibles:

EmailService.send_email(text)

PushService.push_notification(msg)

SMSService.send_sms(body)

Adaptadores:

EmailAdapter
PushAdapter
SMSAdapter

"""
# se busca compatibilizar distintos metodos de un servicio al cliente

from abc import ABC, abstractmethod


class Interface(ABC):
    @abstractmethod
    def send(self, msg):
        pass

# services
class EmailService:
    def send_email(self, text):
        return f"Mail sended -> '{text}'"
    
class PushService:
    def push_notification(self, msg):
        return f"Notification pushed -> '{msg}'"
    
class SMSService:
    def send_sms(self, body):
        return f"SMS sended -> '{body}'"
    
# adaptadores
class EmailAdapter(Interface):
    def __init__(self, service: EmailService):
        if not isinstance(service, EmailService):
            return
        
        self.service = service

    def send(self, msg):
        return self.service.send_email(msg)
    
class PushAdapter(Interface):
    def __init__(self, service:PushService):
        if not isinstance(service, PushService): 
            return 
        
        self.service = service

    def send(self, msg):
        return self.service.push_notification(msg)
    
class SMSAdapter(Interface):
    def __init__(self, service: SMSService):
        if not isinstance(service, SMSService):
            return
        
        self.service = service

    def send(self, msg):
        return self.service.send_sms(msg)
    

if __name__ == "__main__":
    email_service = EmailService()
    print(email_service.send_email("Mail enviado desde Service")) # nuestro servicio hace esto

    # pero en nuestro programa quiero que con el metodo send, desde cualquier servicio se mande el mensaje

    email_adapter = EmailAdapter(email_service)

    print(email_adapter.send("Mail enviado mediante el adapter"))

    sms_service = SMSService()
    print(sms_service.send_sms("SMS enviado desde Service"))

    sms_adapter = SMSAdapter(sms_service)
    print(sms_adapter.send("SMS enviado mediante el adapter"))