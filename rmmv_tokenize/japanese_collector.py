import json
import re
from typing import List, Any

class JapaneseStringCollector:
    JAPANESE_PATTERN = re.compile(r'[\u3040-\u30ff\u3400-\u4dbf\u4e00-\u9fff\uff66-\uff9f]')

    def __init__(self, json_path: str):
        self.json_path = json_path
        self.japanese_strings = []

    def collect(self) -> List[str]:
        with open(self.json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        self.japanese_strings = []
        self._traverse(data)
        return self.japanese_strings

    def _traverse(self, obj: Any):
        if isinstance(obj, str):
            if self.is_japanese(obj):
                self.japanese_strings.append(obj)
        elif isinstance(obj, dict):
            for v in obj.values():
                self._traverse(v)
        elif isinstance(obj, list):
            for item in obj:
                self._traverse(item)

    @classmethod
    def is_japanese(cls, text: str) -> bool:
        return bool(cls.JAPANESE_PATTERN.search(text))
