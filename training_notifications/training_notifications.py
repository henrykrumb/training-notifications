import os
import json


def notifier_from_dict(d):
    module_name = 'notifier'
    if 'notifier' in d:
        module_name += '_' + d.get('notifier').lower()
    module = __import__(module_name)
    class_name = 'Notifier' + d.get('notifier')
    klass = getattr(module, class_name)
    instance = klass(**d)
    return instance


def notifier_from_json(filename):
    with open(filename, 'r') as f:
        d = json.load(f)
    return notifier_from_dict(d)


def notify_all(notifiers, epoch, metrics):
    """
    Send notifications using a list of notifiers.
    """
    for notifier in notifiers:
        try:
            notifier.notify(epoch, metrics)
        except Exception as ex:
            print('Warning: Failed to notify about training progress.')
            print(ex)
