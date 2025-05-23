import unittest
from rmmv_tokenize.tokenizer import Tokenizer

class TestTokenizer(unittest.TestCase):
    def setUp(self):
        self.tokenizer = Tokenizer()

    def test_tokenize_and_word_freq(self):
        text1 = "麩菓子は、麩を主材料とした日本の菓子。"
        text2 = "麩を用いた菓子は江戸時代からすでに存在していた。"
        tokens1 = self.tokenizer.tokenize(text1)
        tokens2 = self.tokenizer.tokenize(text2)
        # 检查返回类型
        self.assertIsInstance(tokens1, list)
        self.assertIsInstance(tokens2, list)
        # 检查词频统计是否包含部分已知词
        freq = self.tokenizer.get_word_freq()
        print(freq)
        self.assertGreater(freq['麩'], 0)
        self.assertGreater(freq['菓子'], 0)
        self.assertGreaterEqual(freq['存在'], 0)

if __name__ == '__main__':
    unittest.main()
