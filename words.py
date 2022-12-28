import re
with open('war.txt', encoding='utf-8', mode='r') as file:
    f = []
    a = file.read()
    a = a.upper()
    for i in a.split():
        if re.search(r"\b[А-Я]", i):
            i = re.sub(f'[,.()?»«!;:]','', i)
            f.append(i)
    frequency = {}
    for i in f:
        if i not in frequency:
            frequency.update({i:1})
        else:
            frequency.update({i : frequency[i] +1})
    for key, value in frequency.items():
        print(f"Слово {key} встречается {value} раз")