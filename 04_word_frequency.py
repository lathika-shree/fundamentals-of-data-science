from collections import Counter
import re

text = """Emma was happy and clever. Emma loved her home and family.
The home was comfortable, and the family was happy."""
words = re.findall(r"\b[\w'-]+\b", text.lower())
frequencies = Counter(words)
print("Word-frequency pairs:")
for word, count in frequencies.items():
    print(word, "->", count)
