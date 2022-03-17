#!/usr/bin/env python
#~*~ coding: utf-8 ~*~

## Imports ---------------------------------------------------------------------
import requests

from .errors import *
## -----------------------------------------------------------------------------

## Constantes Internes ---------------------------------------------------------
API_URL = 'https://smsapi.free-mobile.fr/sendmsg'

# Codes de Response
SENT           = 200 # Le SMS a été envoyé sur votre mobile.
MISSING_PARAM  = 400 # Un des paramètres obligatoires est manquant.
LIMIT_EXCEEDED = 402 # Trop de SMS ont été envoyés en trop peu de temps.
AUTH_ERROR     = 403 # Le service n'est pas activé sur l'espace abonné, ou login / clé incorrect.
INTERNAL_ERROR = 500 # Erreur côté serveur. Veuillez réessayer ultérieurement.
## -----------------------------------------------------------------------------

## API Main Class --------------------------------------------------------------
class Notifier:
    """Cette classe va stocker les credentials de l'API de Notification par SMS
    de Free Mobile, et faciliter l'envoi de notification SMS depuis votre code.
    L'unique méthode `send` requiert l'adoption du modèle de gestion des erreurs
    `try...except`. Pour obtenir la liste des erreurs, entrez `import freesmsapi.errors`
    suivi de `help(freesmsapi.errors)`, ou consultez le fichier errors.py.

    Attributes:
        user -- L'identifiant utilisateur
        passwd -- La clé d'authentification

    Disclaimer:
        Vous devez être abonné Free Mobile et avoir activé l'option de notification
        par SMS dans l'espace abonné.
        https://mobile.free.fr/moncompte/index.php?page=options (en bas de la page)
        C'est sur cette même page que vous trouverez la clé d'authentification.
        L'identifiant utilisateur est, lui, le même que pour votre espace abonné.
    """

    def __init__(self, user, passwd):
        """Initialise l'API avec les identifiants donnés.

        Arguments:
            user   (int/string) -- L'identifiant utilisateur
            passwd (string)     -- La clé d'authentification
        """
        self.user = user
        self.passwd = passwd

    def send(self, msg):
        """Envoie un SMS avec le message donné. Doit être utilisée dans un bloc
        `try...except`

        Arguments:
            msg (string) -- Le message à envoyer. (supporte l'utf-8)

        Return:
            True si le message a été envoyé

        Raises:
            Une erreur spécifique en fonction de la réponse du serveur si le
            message n'a pas pu être envoyé.
        """
        params = {'user': self.user, 'pass': self.passwd, 'msg': msg.encode('utf-8')}

        # Je ne sais pas pourquoi mais les requêtes POST renvoient MISSING_PARAM...
        # Heureusement, requests url_encode automatiquement nos paramètres.
        return self._check_response(params, requests.get(API_URL, params=params).status_code)

    def _check_response(self, params, response):
        # Parse la réponse (basé sur le Status Code HTTP)
        if response == SENT:
            return True
        elif response == MISSING_PARAM:
            raise MissingParameter(params)
        elif response == LIMIT_EXCEEDED:
            raise LimitExceeded(params)
        elif response == AUTH_ERROR:
            raise AuthenticationError(params)
        elif response == INTERNAL_ERROR:
            raise InternalError(params)
        else:
            raise UnknownError(params, response)
## -----------------------------------------------------------------------------

## Tester le module -------------------------------------------------------------
if __name__ == '__main__':

    from time import sleep

    user   = raw_input('Veuillez entrer votre identifiant utilisateur > ')
    passwd = raw_input('Et la clé d\'authentification > ')
    print('')
    msg    = raw_input('Maintenant écrivez un court message à envoyer > ')

    notifier = Notifier(user, passwd)

    try:
        notifier.send(msg)
        sleep(2)
        print("N'est-ce pas vraiment génial ?")

    except AUTH_ERROR as err:
        print(err.description)

    except MissingParameter as err:
        print(err.description)

    except LimitExceeded as err:
        print(err.description)

    except InternalError as err:
        print(err.description)

    except UnknownError as err:
        print(err.description)


## -----------------------------------------------------------------------------
