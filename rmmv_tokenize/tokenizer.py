import fugashi
from collections import Counter


class Tokenizer:
    def __init__(self):
        self.tagger = fugashi.Tagger()
        self.word_freq = Counter()

    def tokenize(self, text):
        """
        Tokenizes the input text using fugashi.
        :param text: The input text to tokenize.
        :return: A list of tokens.
        """
        tokens = []
        for word in self.tagger(text):
            tokens.append(word.feature.lemma)
        # 更新词频统计
        self.word_freq.update(tokens)
        return tokens

    def get_word_freq(self):
        """
        获取当前的词频统计 Counter 对象。
        :return: collections.Counter
        """
        return self.word_freq