from plyer import notification

from .notifier import Notifier


class NotifierDesktop(Notifier):
    def __init__(self):
        super(self, NotifierDesktop).__init__()

    def notify(self, epoch, metrics):
        title = Notifier.make_title()
        message = Notifier.make_message(epoch)
        notification.notify(title, message)

