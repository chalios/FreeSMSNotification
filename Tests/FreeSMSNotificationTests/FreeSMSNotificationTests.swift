import XCTest
@testable import FreeSMSNotification

final class FreeSMSNotificationTests: XCTestCase {
    func testExample() throws {
        // This is an example of a functional test case.
        // Use XCTAssert and related functions to verify your tests produce the correct
        // results.
        
        if let notifier = FreeSMSNotification(id: "32284532", key: "vLmc1Q4McRTIMs", application: "Tortuga") {
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
