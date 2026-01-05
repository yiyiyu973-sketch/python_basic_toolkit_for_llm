import csv
import re
def count_word_frequency(txt_path: str, encoding: str = "utf-8") -> dict:
    try:
        with open(txt_path, "r", encoding=encoding) as f:
            text = re.sub(r"[^\w\s]", "", f.read().lower())
            words = text.split()
            word_count = {word: words.count(word) for word in words}
            return dict(sorted(word_count.items(), key=lambda x: x[1], reverse=True))
    except FileNotFoundError: raise FileNotFoundError(f"文件 {txt_path}不存在")

def read_csv_simple(csv_path: str, encoding: str = "utf-8") -> list:
    try:
        with open(csv_path, "r", encoding=encoding) as f:
            return [row for row in csv.reader(f)]
    except Exception as e: raise Exception(f"读取CSV失败: {str(e)}")