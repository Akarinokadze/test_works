import spacy
import re
from collections import Counter

with open('input.txt') as f:
    texts = f.readlines()
texts = [_.strip() for _ in texts]

nlp = spacy.load("en_core_web_sm")
with open('output.html', 'w') as f:
    # creating HTML page
    f.write('<html>\n<head>\n<style>\np{text-align: right;}\n</style>\n</head>\n<body>\n')
    for text in texts:
        doc = nlp(text)
        # counting PROPN and retrieving all NUMs
        raw_nums = []
        propn = 0
        for ent in doc:
            if ent.pos_ == 'PROPN':
                propn += 1
            if ent.pos_ == 'NUM':
                raw_nums.append(ent.text)
        # extracting complex NUMs
        nums = []
        for num in raw_nums:
            num = re.sub(r'\D', ' ', num)
            if type(num) == int:
                nums.extend([num])
            else:
                nums.extend([_.strip() for _ in num.split()])
        # counting unique NUMs
        num_cnt = list(Counter(nums).values())
        # writing to file
        f.write('<p>' + text + '</p>\n')
        for num in num_cnt:
            f.write('<p>' + str(num) + '</p>\n')
        f.write('<p>' + str(propn) + '</p>\n')
    # closing HTML page
    f.write('</body>\n</html>')
