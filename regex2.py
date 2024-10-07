import re 

pp = 'You know, it turns out that I missed all these Pythonic jpurney, never leave me please, stay witgh me Python'

pattern = 'me'

if re.search(pattern, pp):
    print("Found")
else:
    ("No clue")

match = re.search(pattern, pp)
print(match)        