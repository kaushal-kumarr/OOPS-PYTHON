from abc import ABC,abstractmethod
class Notification(ABC):
    @abstractmethod
    def send(self):
        pass

class Email(Notification):
    def send(self):
        print("Sending Email Notification: Check your inbox.")

class Sms(Notification):
    def send(self):
        print("Sending SMS Notification: Check your messages.")

class PushNotification(Notification):
    def send(self):
        print("Sending Push Notification: Check your app notifications.")

notifications = (Email(), Sms(), PushNotification())

for notify in notifications:
    notify.send()