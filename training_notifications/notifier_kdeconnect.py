import subprocess

from .notifier import Notifier


class NotifierKDEConnect(Notifier):
    def __init__(self, device_id=''):
        super(NotifierKDEConnect, self).__init__()
        if not device_id:
            cmd = 'kdeconnect-cli -a --id-only'.split(' ')
            out = subprocess.run(cmd, capture_output=True)
            self.device_id = out.stdout.decode('utf-8').strip()
        else:
            self.device_id = device_id

    def notify(self, epoch, metrics):
        title = Notifier.make_title()
        message = Notifier.make_message(epoch, metrics)
        cmd = f'kdeconnect-cli -d {self.device_id} --ping-msg'.split(' ')
        cmd.append(f'"{title}:\n{message}"')
        subprocess.run(cmd)
