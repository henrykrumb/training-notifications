import asio
import aioxmpp

from .notifier import Notifier


class NotifierXMPP(Notifier):
    def __init__(self, jid, password):
        super(self, NotifierXMPP).__init__()
        self.client = aioxmpp.PresenceManagedClient(
            jid,
            aioxmpp.make_security_layer(password)
        )

    def notify(self, epoch, metrics):
        title = Notifier.make_title()
        message = title + '\n' + Notifier.make_message(epoch, metrics)
        async with client.connected() as stream:
            msg = aioxmpp.Message(
                to=recipient_jid,
                type_=aioxmpp.MessageType.CHAT,
            )
            msg.body[None] = message
            await client.send(msg)
