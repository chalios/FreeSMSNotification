# FreeSMSNotification (Python)
Utilisez l'API de notification par SMS de Free Mobile directement avec Python.

# Installation
+ `git clone`
+ `cd freesmsapi`
+ `pip install .` ou `python setup.py install`

Si vous utilisez `virtualenv`, assurez-vous que python 2 est utilisé par défaut ou spécifiez `--python=python2` lors de la création de l'environnement virtuel.

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
