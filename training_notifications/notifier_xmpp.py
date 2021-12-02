import asyncio
import aioxmpp

from .notifier import Notifier


class NotifierXMPP(Notifier):
    def __init__(self, jid, password, recipient=''):
        """
        :param jid: Jabber ID as a string, e.g. user@jabber.com
        :param password: Password that belongs to Jabber ID
        :param recipient: Recipient JID as string. If empty, message is sent to sender.
        """
        super(NotifierXMPP, self).__init__()
        self.client = aioxmpp.PresenceManagedClient(
            aioxmpp.structs.JID.fromstr(jid),
            aioxmpp.make_security_layer(password)
        )
        # send message to self if no recipient provided
        self.recipient = recipient if recipient else jid

    async def notify_internal(self, epoch, metrics):
        title = Notifier.make_title()
        message = title + '\n' + Notifier.make_message(epoch, metrics)
        async with self.client.connected() as stream:
            msg = aioxmpp.Message(
                to=aioxmpp.structs.JID.fromstr(self.recipient),
                type_=aioxmpp.MessageType.CHAT,
            )
            msg.body[None] = message
            await self.client.send(msg)

    def notify(self, epoch, metrics):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.notify_internal(epoch, metrics))
        loop.close()
