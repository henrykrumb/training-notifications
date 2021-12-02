#!/usr/bin/env python3

try:
    from training_notifications import notifier_from_dict, notify_all
except ImportError:
    def notifier_from_dict(d): pass
    def notify_all(n, e, m): pass



def fmain():
    definitions = [
        {
            'notifier': 'KDEConnect'
        },
        {
            'notifier': 'Desktop'
        }
    ]
    notifiers = [notifier_from_dict(d) for d in definitions]
    metrics = {
        'validation_accuracy': 0.1337
    }
    notify_all(notifiers, 42, metrics)


if __name__ == '__main__':
    fmain()
