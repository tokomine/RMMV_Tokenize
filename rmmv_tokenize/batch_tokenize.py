import os
import glob
import csv
from .japanese_collector import JapaneseStringCollector
from .tokenizer import Tokenizer
import unicodedata

class BatchJapaneseTokenizer:
    def __init__(self, folder_path: str, output_csv: str):
        self.folder_path = folder_path
        self.output_csv = output_csv
        self.tokenizer = Tokenizer()

    def is_punctuation(self, token: str) -> bool:
        # 仅当字符串全部为标点符号时才过滤
        if not token:
            return True
        for char in token:
            if not unicodedata.category(char).startswith('P'):
                return False
        return True

    def is_single_character(self, token: str) -> bool:
        # 判断是否为单字符（日文字符宽度不一，len通常可用）
        return len(token) == 1

    def process(self):
        all_japanese_strings = []
        json_files = glob.glob(os.path.join(self.folder_path, '**', '*.json'), recursive=True)
        for json_file in json_files:
            print(json_file)
            collector = JapaneseStringCollector(json_file)
            all_japanese_strings.extend(collector.collect())
        for text in all_japanese_strings:
            self.tokenizer.tokenize(text)
        freq = self.tokenizer.get_word_freq()
        print(freq)
        # 过滤掉单字和标点
        filtered = [(word, count) for word, count in freq.items()
                    if not self.is_single_character(word) and not self.is_punctuation(word)]
        # 按词频排序
        filtered.sort(key=lambda x: x[1], reverse=True)
        # 保存为CSV
        with open(self.output_csv, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['token', 'count'])
            for word, count in filtered:
                writer.writerow([word, count])
