import Foundation

public struct FreeSMSNotification {
    
    // MARK: - Errors enumeration
    public enum Errors: Error {
        case missingParameter
        case sendingTooFast
        case authenticationError
        case serverError
        case badMsgFormat
        case requestTimeout
        case unknown(statusCode: Int)
    }
    
    // MARK: - Properties
    private let id      : String
    private let key     : String
    public  let appName : String?

    // MARK: - Initialization
    public init?(id: String, key: String, application name: String? = nil) {
        self.id      = id
        self.key     = key
        self.appName = name
        
        // Check connexion :
        let msg = "Service de notification par SMS activé"
        do {
            try send(msg)
        }
        catch {
            return nil
        }
    }
    
    // MARK: - Sending SMS notification
    
    /*
     On se base ici sur la description de l'option "Notification par SMS" de Free
     (Qui se trouve ici : https://mobile.free.fr/account/mes-options/notifications-sms)
     (C'est également là qu'il faut activer l'option.)
     
     Le système est particulièrement simple : il suffit de faire une requête (GET ou POST) vers le serveur de notification :
     "https://smsapi.free-mobile.fr/sendmsg" en y ajoutant 3 paramètres :
        • user - le numéro d'identification (login) [/!\ ≠ n° telephone /!\]
        • pass - la clé d'identification
        • msg  - le message à envoyer
     
     Ici nous nous contenterons d'une requête GET. Et pour nous simplifier la tâche, nous ne parserons même pas le
     JSON de la réponse. Les Status Codes suffisent comme l'indique la documentation :
     
     >>> Le code de retour HTTP indique le succès ou non de l'opération :
     >>>    • 200 : Le SMS a été envoyé sur votre mobile.
     >>>    • 400 : Un des paramètres obligatoires est manquant.
     >>>    • 402 : Trop de SMS ont été envoyés en trop peu de temps.
     >>>    • 403 : Le service n'est pas activé sur l'espace abonné, ou login / clé incorrect.
     >>>    • 500 : Erreur côté serveur. Veuillez réessayer ultérieurement.
     
    */
    
    // MARK: Synchronous
    public func send(_ message: String, timeout: Int = 0) throws {
        
        /*
         Cette fonction ne renvoie rien quand tout se passe comme prévu.
         Si une erreur survient, elle va jeter l'erreur pour qu'elle puisse être attrapée
         par un do_catch et traitée par ce dernier.
        */
        
        // On s'assure d'avoir un message qui soit URL encodé
        guard let message = prepared(message).urlEncoded else {
            throw Errors.badMsgFormat
        }
        
        // On génère l'URL de la requête avec ses paramètres
        let url = URL(string: "https://smsapi.free-mobile.fr/sendmsg?user=\(id)&pass=\(key)&msg=\(message)")!
        
        // On effectue la requête
        let task = URLSession.shared.dataTask(with: url)
        
        let start_time = Int64(Date.timeIntervalSinceReferenceDate * 1000)
        task.resume()
        
        // On attend que l'échange avec le serveur se termine
        while task.state != .completed {
            
            // On vérifie qu'on a pas dépassé le timeout
            let now = Int64(Date.timeIntervalSinceReferenceDate * 1000)
            if now - start_time >= converted(timeout) {
                // Si c'est le cas, on abandonne et on jette une erreur.
                task.cancel()
                throw Errors.requestTimeout
            }
            
            usleep(1000) // sleep 1ms
        }
        
        // On vérifie s'il y a eu une erreur et on la jette si c'est le cas
        if let response = task.response as? HTTPURLResponse {
            if let error = convertedError(response.statusCode) {
                throw error
            }
        }
    }
    
    // MARK: Asynchronous
    public func send(_ message: String, withCompletionHandler completion: @escaping (Result<Any?, Errors>) -> Void) {
        
        
        // On s'assure d'avoir un message qui soit URL encodé
        guard let message = prepared(message).urlEncoded else {
            DispatchQueue.main.async {
                completion(.failure(.badMsgFormat))
            }
            return
        }
        
        // On génère l'URL de la requête avec ses paramètres
        let url = URL(string: "https://smsapi.free-mobile.fr/sendmsg?user=\(id)&pass=\(key)&msg=\(message)")!
        
        // On effectue la requête
        let task = URLSession.shared.dataTask(with: url) {
            (_, response, _) in
            
            if let response = response as? HTTPURLResponse {
                if let error = self.convertedError(response.statusCode) {
                    DispatchQueue.main.async {
                        completion(.failure(error))
                    }
                } else {
                    DispatchQueue.main.async {
                        completion(.success(nil))
                    }
                }
            }
        }
        task.resume()
    }
    
    // MARK: - Helper internal methods
    
    private func convertedError(_ code: Int) -> Errors? {
        switch code {
        case 200:
            return nil
        case 400:
            return Errors.missingParameter
        case 402:
            return Errors.sendingTooFast
        case 403:
            return Errors.authenticationError
        case 500:
            return Errors.serverError
        default:
            return Errors.unknown(statusCode:code)
        }
    }
    
    private func converted(_ timeout: Int) -> Int {
        if timeout == 0 {
            return 10 * 1000
        } else {
            return timeout * 1000
        }
    }
    
    private func prepared(_ message: String) -> String {
        
        // On ajoute le nom de l'application devant le message s'il existe
        if let appName = appName {
            return "Notification \(appName):\n\n\(message)"
        } else {
            return message
        }
    }

}

public extension String {
    var urlEncoded: String? {
        return addingPercentEncoding(withAllowedCharacters: .alphanumerics)
    }
}


