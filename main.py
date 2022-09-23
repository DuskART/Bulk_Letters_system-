f = open("input\\names.txt", "r")
letter = open("input\\letter.txt", "r")
letter_text = (letter.read())



names_l = (f.readlines())
names_list = []


for name in names_l:
    name = name.strip()
    names_list.append(name)

print(names_list)

for name in names_list:
    letter = open(f"output\\letter_{name}.txt", "w")
    # už vím.. my jsme si přepsali name a když se for načetl znova tak už vycházel z hello deontay a proto nebylo možné najít a přepsat"name".... letter text tedy musel zustat zachovany at z neho mohou brat i ostatni...
    predelany = letter_text.replace('"NAME"', name)
    letter.write(f"{predelany}")
# 
# print(letter_text)
# 
# print(letter_text.replace('"NAME"', name))