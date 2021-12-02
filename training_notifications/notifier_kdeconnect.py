import subprocess

from .notifier import Notifier


class NotifierKDEConnect(Notifier):
    def __init__(self, device_id=''):
        if not device_id:
            cmd = 'kdeconnect-cli -a --id-only'.split(' ')
            out = subprocess.run(cmd, capture_output=True)
            self.device_id = out.stdout.encode('utf-8')
        else:
            self.device_id = device_id

    def notify(self, epoch, metrics):
        title = Notifier.make_title()
        message = Notifier.make_message(epoch, metrics)
        cmd = f'kdeconnect-cli -d {} --ping-msg'.split(' ')
        cmd.append(f'"{title}: {message}"')
        subprocess.run(cmd)
