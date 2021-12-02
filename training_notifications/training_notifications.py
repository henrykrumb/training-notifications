import os
import json
import traceback

import click


def notifier_from_dict(d):
    """
    Create notifier from dict.
    Use this method to configure your notifiers before training.

    :param d: dict containing notifier configuration
    """
    module_name = 'notifier'
    if 'notifier' in d:
        module_name += '_' + d['notifier'].lower()
    try:
        module = __import__(module_name)
    except ImportError:
        click.secho(f'Error: Notifier {module_name} not found', fg='red')
        exit()
    class_name = 'Notifier' + d.get('notifier')
    klass = getattr(module, class_name)
    instance = klass(**d)
    return instance


def notify_all(notifiers, epoch, metrics):
    """
    Send notifications utilizing a list of notifiers.

    :param notifiers: List of Notifier subclassed objects
    :param epoch: Current epoch
    :param metrics: Dict of metrics (floats) to report
    """
    for notifier in notifiers:
        try:
            notifier.notify(epoch, metrics)
        except Exception:
            click.secho('Warning: Failed to notify about training progress.', fg='red')
            traceback.print_exc()
