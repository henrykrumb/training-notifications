# training-notifications

Simple framework to send notifications about training progress
to one or multiple notifiers.



## Installation

Run

```bash
python3 ./setup.py install
```

to install.


## Usage

Import training\_notifications using this code snippet:

```Python
try:
    from training_notifications import notifier_from_dict, notify_all
except ImportError:
    def notifier_from_dict(d): pass
    def notify_all(n, e, m): pass
```

You can now use notifier\_from\_dict(d) to load your preferred notifiers.
I'd recommend to add a config.json file to your project, containing user
configuration for training-notifications and this lands in .gitignore.
You can alternatively use yaml or whatever file type you prefer.
Here's an example for a json config file:

```json
{
...
  "notifiers": [
    {
      "notifier": "desktop"
    }
  ]
...
}
```

Load notifier using this snippet:

```python
import json

...

with open('config.json', 'r') as f:
	config = json.load(f)
notifier_config = config.get('notifiers', [])
notifiers = [notifier_from_dict(n) for n in notifier_config]
```

During your training, you can then use:

```python
metrics = {
	# replace with the metrics you want to monitor
	'validation_accuracy': validation_accuracy
}
notify_all(notifiers, epoch, metrics)
```

e.g. during model validation phase when a better model was found.
Of course, you could also notify\_all after the training terminated.


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

