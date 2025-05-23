import unittest
import fugashi

class DemoTestCase(unittest.TestCase):
    def test_demo(self):
        self.assertEqual(1 + 1, 2)

    def test_fugashi(self):
        tagger = fugashi.Tagger()
        text = "麩を用いた菓子は江戸時代からすでに存在していた。"

        print("input:", text)
        for word in tagger(text):
            # feature is a named tuple holding all the Unidic info
            print(word.surface, word.feature.lemma, sep="\t")

if __name__ == '__main__':
    unittest.main()
