#!/usr/bin/env python
#~*~ coding: utf-8 ~*~

from FreeSMSNotification import *
from time import sleep

print 'Veuillez entrer votre identifiant utilisateur'
user   = raw_input('>> ')

print 'Et la clé d\'authentification'
passwd = raw_input('>> ')

print 'Maintenant écrivez un court message à envoyer'
msg    = raw_input('>> ')

notifier = FreeSMSNotifier(user, passwd)

try:
    notifier.send(msg)
    sleep(2)
    print "N'est-ce pas vraiment génial ?"

except AuthenticationError as err:
    print err.description

except MissingParameter as err:
    print err.description

except LimitExceeded as err:
    print err.description

except InternalError as err:
    print err.description

except UnknownError as err:
    print err.description
