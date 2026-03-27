import unittest
from Emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):

    def test_happy(self):
        result = emotion_detector("I am very happy today!")
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_sad(self):
        result = emotion_detector("I am feeling very sad.")
        self.assertEqual(result['dominant_emotion'], 'sadness')

    def test_angry(self):
        result = emotion_detector("I am so angry right now!")
        self.assertEqual(result['dominant_emotion'], 'anger')

    def test_fear(self):
        result = emotion_detector("I am scared of this situation.")
        self.assertEqual(result['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()
