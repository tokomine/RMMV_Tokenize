import os
import unittest
from rmmv_tokenize.batch_tokenize import BatchJapaneseTokenizer
import csv

class TestBatchJapaneseTokenizer(unittest.TestCase):
    def setUp(self):
        self.folder_path = os.path.join(os.path.dirname(__file__))
        self.cache_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), '_cache')
        os.makedirs(self.cache_dir, exist_ok=True)
        self.output_csv = os.path.join(self.cache_dir, 'test_token_freq.csv')
        # 清理旧文件
        if os.path.exists(self.output_csv):
            os.remove(self.output_csv)

    def test_process(self):
        tokenizer = BatchJapaneseTokenizer(self.folder_path, self.output_csv)
        tokenizer.process()
        # 检查csv文件是否生成
        self.assertTrue(os.path.exists(self.output_csv))
        # 检查csv内容是否合理
        with open(self.output_csv, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
            self.assertGreater(len(rows), 0)
            # 检查字段名
            self.assertIn('token', reader.fieldnames)
            self.assertIn('count', reader.fieldnames)
            # 检查词频为数字
            for row in rows:
                self.assertTrue(row['token'])
                self.assertTrue(row['count'].isdigit())

if __name__ == '__main__':
    unittest.main()
