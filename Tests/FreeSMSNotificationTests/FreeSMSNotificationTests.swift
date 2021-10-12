import XCTest
@testable import FreeSMSNotification

final class FreeSMSNotificationTests: XCTestCase {
    func testExample() throws {
        
        let id  = "12345678"        // Entrez ici VOTRE id
        let key = "abcdefgHIjk79s"  // Et ici VOTRE clé d'API
        
        if let notifier = FreeSMSNotification(id: id, key: key, application: "XCTest") {
            notifier.send("Coucou") {
                result in
                
                switch result {
                case .success(_):
                    XCTAssertTrue(true)
                case .failure(let error):
                    XCTFail("Failed with error: \(error.localizedDescription)")
                }
            }
        } else {
            XCTFail("Authentication error")
        }
        
    }
}
