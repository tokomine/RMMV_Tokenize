import unittest
import os
from rmmv_tokenize.japanese_collector import JapaneseStringCollector

class TestJapaneseStringCollector(unittest.TestCase):
    def setUp(self):
        self.json_path = os.path.join(os.path.dirname(__file__), 'test_japanese.json')
        self.collector = JapaneseStringCollector(self.json_path)

    def test_collect(self):
        result = self.collector.collect()
        print(result)
        # 预期的日文字符串
        expected = [
            "これは日本語です。",
            "テスト用の文字列",
            "日本語のテキスト",
            "カタカナ"
        ]
        for jp in expected:
            self.assertIn(jp, result)
        # 检查非日文字符串未被收集
        self.assertNotIn("not japanese", result)
        self.assertNotIn("english text", result)
        self.assertNotIn("abc", result)
        self.assertNotIn("123", result)

if __name__ == '__main__':
    unittest.main()
