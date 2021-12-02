from plyer import notification

from .notifier import Notifier


class NotifierDesktop(Notifier):
    def __init__(self):
        super(NotifierDesktop, self).__init__()

    def notify(self, epoch, metrics):
        title = Notifier.make_title()
        message = Notifier.make_message(epoch, metrics)
        notification.notify(title, message)

