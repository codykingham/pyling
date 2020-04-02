from pathlib import Path

try:
    your_text = list(Path('../BYOT').glob('*.txt'))[0].read_text(encoding='UTF-8')
except IndexError:
    raise Exception('.txt not found in BYOT folder! Make sure your text is saved with .txt extension!')
