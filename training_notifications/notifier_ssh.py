import spur

from .notifier import Notifier


class NotifierSSH(Notifier):
    def __init__(self, host, user, port=None, password=None, command=['notify-send', '{title}', '{message}']):
        super(self, NotifierSSH).__init__()
        self.command = command
        self.shell = spur.SshShell(hostname=host, username=user, port=port, password=password)

    def notify(self, epoch, metrics):
        title = Notifier.make_title()
        message = Notifier.make_message(epoch, metrics)
        with self.shell:
            v = {
                'title': title,
                'message': message
            }
            command = [token.format(v) for token in self.command]
            result = shell.run(command)
