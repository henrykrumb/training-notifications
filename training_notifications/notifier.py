import click


class Notifier:
    def __init__(self):
        pass

    @staticmethod
    def make_title():
        return 'Training Progress'

    @staticmethod
    def make_message(epoch, metrics):
        """
        :param epoch: Number of epochs that has passed so far
        :param metrics: Dict of metrics (float)
        """
        message = f'epoch: {epoch}'
        for key, metric in metrics.items():
            message += f'{key}: {metric:.5f}'
        return message

    def notify(self, epoch, metrics):
        title = Notifier.make_title()
        message = Notifier.make_message(epoch, metrics)

