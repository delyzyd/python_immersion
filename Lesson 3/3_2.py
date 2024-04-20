# 3. В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. 
# Не учитывать знаки препинания и регистр символов. 
# За основу возьмите любую статью из википедии или из документации к языку.


import re
from collections import Counter

def find_top_10_common_words(text):
    words = re.findall(r'\b\w+\b', text.lower())
    word_count = Counter(words)
    most_common_words = word_count.most_common(10)
    return most_common_words

# Пример текста(статья из Википедии о Python)
text = """
Python is an interpreted, high-level and general-purpose programming language. Python's design 
philosophy emphasizes code readability with its notable use of significant whitespace. Its language 
constructs and object-oriented approach aim to help programmers write clear, logical code for small and 
large-scale projects.
"""

# Использование функции:
result = find_top_10_common_words(text)
print(result)