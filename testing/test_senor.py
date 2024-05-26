import unittest
from back import *

class TestSenORLegalAdvisor(unittest.TestCase):
    
    def test_model(self):
        user_query = "What are my legal rights as a woman in the workplace?"
        max_length = 1024
        temp = 0.5
        response = model(user_query, max_length, temp)
        self.assertNotEqual(response, "")              # Assert that the response is not empty
        #method is used to verify that two values are not equal
 
    def test_text_speech(self):
       
        text = "This is a test message."
        audio_base64 = text_speech(text)
        self.assertNotEqual(audio_base64, "")         # Assert that the audio_base64 is not empty

if __name__ == "__main__":
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestSenORLegalAdvisor)
    test_result = unittest.TextTestRunner().run(test_suite)

    print("\nTest Results:")
    print("-------------")
    for test, failure_message in test_result.failures:
        print(f"{test.id()}: FAILED - {failure_message}")
    print("\nOverall Result:", "PASSED" if test_result.wasSuccessful() else "FAILED")
