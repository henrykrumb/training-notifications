from .notifier import Notifier

class NotifierKDEConnect(Notifier):
    def __init__(self):
        pass

    def notify(self, epoch, metrics):
        title = Notifier.make_title()
        message = Notifier.make_message(epoch, metrics)
