# FreeSMSNotification (Swift version)

## Installation :
Ce module est un Swift Package. Il suffit donc de l'ajouter à votre projet directement dans Xcode : `File > Add Package` et d'entrer l'url du repo. /!\ **Veillez à bien choisir la branche *Swift*.** /!\

## Utilisation

Rien de plus simple :


#### Initialisation

Il faut d'abord instancier un "notifier" qui est simplement la structure qui va contenir vos identifiants 
et s'occuper d'envoyer la notification. 
Ce dernier testera alors si la connexion est établie. Si c'est le cas vous recevrez un SMS le confirmant.
Sinon, l'initialisation renverra nil.

```swift
import FreeSMSNotification

let notifier = FreeSMSNotification(id: "12345678", key: "aBcd1E2FghIjKL", application: "App Name")

// Si ça marche vous aurez votre notifier. Et vous pourrez l'utiliser.
// Sinon vous aurez nil. À vous de trouver quoi en faire.

```

#### Envoi de la notification

Une fois l'instance créé, vous aurez la possibilité d'envoyer votre notification de manière synchrone ou asynchrone.

##### Synchrone

La fonction *send()* synchrone est une fonction *throw*. Elle ne renvoie rien mais génère des erreurs s'il y en a. Ces erreurs doivent être gérées dans un do-catch.

Elle prend 2 paramètres, dont 1 optionnel :
    - message : qui est le contenu de la notification
    - timeout : qui est la durée en secondes avant de renoncer à la requête. (Defaut: 0 -> 10 secondes)
    
    
Voici son prototype :

```swift
public func send(_ message: String, timeout: Int = 0)
```

Exemple :

```swift

do {
    try notifier.send("Mon super message")
    
    // OU
    
    try notifier.send("Mon super message", timeout: 3) // On modifie le timeout à 3 secondes
    
} catch {
    print("Erreur. La notification n'a pu être envoyée")
}

```

##### Asynchrone

La version asynchrone de *send()* est à la fois similaire et différente. Elle prend toujours 2 arguments, cette fois obligatoires. Mais elle ne *throw* pas. À la place elle renvoie un resultat de type Result à la closure passée en paramètre.

Voici son prototype :

```swift
public func send(_ message: String, withCompletionHandler completion: @escaping (Result<Any?, Errors>) -> Void)
```
Exemple:

```swift

notifier.send("Mon super message") {
    result in
    
    switch result {
    case .success(_):
        // Faites quelque chose. Ou pas.
        return
    case .failure(let error):
        // Gérez les erreurs ici.
    }
}

```

##### Exemple

Utilisation du module au sein d'une structure :

```swift

import FreeSMSNotification

struct bidule {
    let notifier: FreeSMSNotification?
    
    init() {
        notifier = FreeSMSNotification(id: "12345678", key: "aBcd1E2FghIjKL", application: "Hello, world!")
    }
            
    func notify(_ message: String) {
        if let notifier = notifier {
            notifier.send(message) {
                result in
                        
                switch result {
                case .success(_):
                    return
                case .failure(let error):
                    print(error.localizedDescription)
                }
            }
        }
    }
            
            
    func method() {
        // Do something that may want to notify you
        notify("Your notification")
    }
}
```

##### Erreurs

Les erreurs sont rassemblées dans l'enum Errors du module : 

```swift
public enum Errors: Error {
    case missingParameter          // Il manque un paramètre dans la requête (exemple: message vide)
    case sendingTooFast            // Les notifications sont envoyées trop vite. Il y a un anti-flood.
    case authenticationError       // Besoin d'expliquer ?
    case serverError               // Erreur interne au serveur. (Requête mal formée ? Plantage serveur ?...)
    case badMsgFormat              // Le message ne peut pas être encodé correctement
    case requestTimeout            // Timeout atteint. Requête expirée.
    case unknown(statusCode: Int)  // Erreur non répertoriée/documentée. Renvoie le status_code HTTP.
}
```

Libre à vous de les gérer ou de les ignorer.

Exemple do-catch:

```swift
do {
    try notifier.send("Message qui n'arrivera pas")
}
catch FreeSMSNotifier.Errors.missingParameter {
    print("Votre message ne serait-il pas vide ?")
}
catch FreeSMSNotifier.Errors.sendingTooFast {
    print("Eh... Molo. On fait pas un DoS là...")
}
catch FreeSMSNotifier.Errors.unknown let code {
    print("Code d'erreur HTTP: \(code)")
}
catch {
    print("L'une des erreurs restantes...")
}
```
Exemple asynchrone :

```swift

notifier.send("Un autre message inutile") {
    result in
    
    switch result {
    case .success(_):
        return
    case .failure(let error):
    
        switch error {
            case .missingParameter:
                print("Votre message ne serait-il pas vide ?")
            case .unknown(let code):
                print("Code d'erreur : \(code)")
            default:
                print("On va pas tous les faire")
        }
        
    }
}
```
