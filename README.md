# training-notifications

Simple framework to send notifications about training progress
to one or multiple notifiers.


## Notifiers

### Notifier

The default notifier. Simply reports training progress to the console.

### NotifierDesktop

Uses plyer Python module to send desktop notifications.
Perfect if you run your training on your desktop machine, e.g. in a background
process or Jupyter notebook in a different tab.

### NotifierKDEConnect

Sends ping to KDEConnect. If device ID is not explicitly configured, it will
use the first available device as default.


### NotifierSSH

Connects to another machine via SSH and issues a notification command.


### NotifierXMPP

Sends a message via XMPP.

