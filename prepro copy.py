import re
with open('truyenkieu_raw.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    lines  = [re.sub(r'[0-9.,]+', '', line).lstrip() for line in lines]

with open('truyenkieu.txt', 'w', encoding='utf-8') as f:
    [f.write(line) for line in lines]
    



