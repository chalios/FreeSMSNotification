# FreeSMSNotification (Python)
Utilisez l'API de notification par SMS de Free Mobile directement avec Python.

# Prérequis
- Python >= 3.6

# Installation
+ `git clone`
+ `cd FreeSMSNotification`
+ `git checkout python`
+ `pip install .`

# Exemple
```python
from FreeSMSNotification import Notifier

notifier = Notifier('123456', '<auth_key>')

message = '''Importante Notification !

Ce message est une notification automatique envoyée depuis un script python
'''

try:
  notifier.send(message)
except:
  print 'Unable to send the SMS'
```

Un exemple plus complet est disponible dans [examples](/examples).
