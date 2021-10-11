# FreeSMSNotification

L'opérateur Free Telecom met à disposition de ses abonnés mobiles une petite API permettant de s'envoyer des notifications par SMS.
Il est ainsi possible d'envoyer des notifications SMS depuis n'importe quel script ou application que vous développez. N'importe où dans le monde. Gratuitement.

T'as Free, t'as tout compris !

L'objectif de ce projet, c'est de transposer cette fonctionnalité directement dans le langage que vous utilisez pour votre projet. Sans avoir besoin d'en recréer la mécanique à chaque fois.


Installez le module correspondant et utilisez-le directement dans votre code.

## Prérequis

- __L'utilisateur final doit être abonné à un forfait Free Mobile.__

- __L'option doit être activée dans l'espace abonné__ :
  https://mobile.free.fr/account/mes-options

Activez l'option en cliquant sur la marque correspondante :
![Activation](https://github.com/chalios/FreeSMSNotification/raw/main/images/Activ_option.png)

En cliquant sur l'onglet on obtient plus de détails sur l'option :
![Details](https://github.com/chalios/FreeSMSNotification/raw/main/images/Options_details.png)

Une fois l'option activée, la clé d'API devient accessible :
![Activated](https://github.com/chalios/FreeSMSNotification/raw/main/images/Options_landing.png)

## Dépôt

Ce dépôt est structuré de la manière suivante :

- La branche principale (*main*) est la "page d'accueil" du projet.
- Chaque autre branche est dédiée à un module spécifique et donc généralement un langage.

## Installation

Rendez-vous dans la branche désirée pour obtenir la procédure d'installation spécifique.

Si vous clonez le dépôt, la commande `git checkout branche` vous permettra d'activer la branche indiquée.

## Contribution

Ce projet n'a pas une grande ampleur, ni un grand intérêt technologique. Son objectif est simplement de donner un coup de pouce à toute personne désireuse d'intégrer **facilement** ce type de notifications dans son propre code. Et ce, quelque soit le langage ou la plateforme.

Oui, c'est très restreint puisqu'il faut être abonné Free pour pouvoir en bénéficier.

Mais ce n'est pas pour autant qu'il est inutile d'y contribuer.
Que ce soit en signalant des bugs ou erreurs, en suggérant des améliorations, en développant ou corrigeant un module...

Vous pouvez apporter la possibilité à d'autres (ou à vous-même) de réaliser de grandes choses à partir de petites pièces. Vous pouvez apprendre à développer vos compétences sur un projet simple. Ou encore faire sourire un inconnu en soutenant son projet.

La contribution est donc libre et encouragée ! À vos Pull Requests !

#### Les règles de développement d'un module

- [x] Il doit s'installer facilement. (Idéalement par un package manager : [swift package manager, npm, pip, ...])
- [x] Il doit s'intégrer facilement. (Dans l'idéal, doit pouvoir s'intégrer dans tout projet existant sans modifications importantes.)
- [x] Il doit être documenté. (Procédures d'installation, d'utilisation, exemple, code source commenté...)

## Remerciements

Merci à Free Telecom.

Ça n'est pas grand chose, la possibilité de s'envoyer soi-même des SMS. Mais c'est pourtant bien pratique. Et peu d'opérateurs, à l'heure où j'écris ces lignes, ne soutiennent autant les amateurs de technologie que Free. Tant par le matériel que les services. (Ils ont été jusqu'à intégrer la possibilité de faire tourner une VM directement sur la Freebox. Qui fait ça ?!)

Alors, merci Free.
