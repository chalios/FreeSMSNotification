#!/usr/bin/env python
#~*~ coding: utf-8 ~*~

class API_Error(Exception):
    """Classe abstraite qui sert de base pour les erreurs spécifiques

    Attributes:
        user        -- L'identifiant utilisateur
        passwd      -- La clé d'authentification
        msg         -- Le message qui aurait du être envoyé
        description -- La description humainement lisible et intelligible
    """

    def __init__(self, params):
        """Assigne les valeurs adéquates aux attributs de la classe en parsant
        l'objet params et en remplaçant toute valeur nulle ou vide par la chaine
        '*missing*'.

        Arguments:
            params (dict) -- Le dictionnaire contenant les paramètres de la requête
        """

        self.user        = params['user'] or '*missing*'
        self.passwd      = params['pass'] or '*missing*'
        self.msg         = params['msg']  or '*missing*'
        self.description = ''


# Allez, un peu d'anglais...

class AuthenticationError(API_Error):
    """Raised when the server couldn't authenticate the request

    Attributes:
        Inherited from API_Error
    """

    def __init__(self, params):
        """Create a new AuthenticationError object

        Arguments:
            params (dict) -- The request's parameters dictionnary
        """

        API_Error.__init__(self, params)
        self.decription = '''Authentication failed with : [user: {}, pass: {}]
Check your credentials and the activation of the option on:
https://mobile.free.fr/moncompte/index.php?page=options (on page bottom)
        '''.format(self.user, self.passwd)

class MissingParameter(API_Error):
    """Raised when there is at least 1 missing parameter in the request.

    Attributes:
        Inherited from API_Error
    """

    def __init__(self, params):
        """Create a new MissingParameter object.

        Arguments:
            params (dict) -- The request's parameters dictionnary
        """
        API_Error.__init__(self, params)
        self.description = 'Missing parameter(s): [user: {}, pass: {}, msg: \'{}...\']'
        self.description = self.description.format(self.user, self.passwd, self.msg[:10])

class LimitExceeded(API_Error):
    """Raised when sending notifications too fast.

    Attributes:
        Inherited from API_Error
    """

    def __init__(self, params):
        """Create a new LimitExceeded object.

        Arguments:
            params (dict) -- The request's parameters dictionnary
        """

        API_Error.__init__(self, params)
        self.description = 'You are sending sms too fast. Please wait a moment...'

class InternalError(API_Error):
    """Raised when the server encounters an internal error.

    Attributes:
        Inherited from API_Error
    """
    def __init__(self, params):
        """Create a new InternalError object.

        Arguments:
            params (dict) -- The request's parameters dictionnary
        """
        API_Error.__init__(self, params)
        self.description = 'The server encountered an error. Please try again later.'

class UnknownError(API_Error):
    """Raised when the server respond with an undescribed status_code.

    Attributes:
        Inherited from API_Error
        self.status_code -- The response from the server
    """

    def __init__(self, params, response):
        """Create a new AuthenticationError object.

        Arguments:
            params      (dict) -- The request's parameters dictionnary
            status_code (int)  -- The server response's status_code
        """
        API_Error.__init__(self, params)
        self.response = response
        self.description = 'The server returned the following status_code: {}, which is undescribed'
        self.description = self.description.format(response)
