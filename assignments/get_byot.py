from pathlib import Path

try:
    your_text = list(Path('../BYOT').glob('*.txt'))[0].read_text()
except IndexError:
    raise Exception('.txt not found in BYOT folder! Make sure your text is saved with .txt extension!')