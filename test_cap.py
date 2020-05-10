import unittest
import cap # Tuo testiohjelmaan testattavan python-tiedoston


class TestCap(unittest.TestCase): 
    def test_one_word(self):
        text = 'python'
        result = cap.cap_text(text) # Tässä tuodaan cap-tiedoston funktio.
        self.assertEqual(result,'Python')
    def multiple_words(self):
        text = 'monthy python'
        result = cap.cap_text(text)
        self.assertEqual(result,'Monty Python')
if __name__=='__main__':
    unittest.main()
