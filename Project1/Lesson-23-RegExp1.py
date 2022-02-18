import re

mytext = "Vasya aaaaaaa 1972, Kolya -1972: Olesya 1981, aaaaaaaa@intel.com," \
         "bbbbbbb@intel.com, Petya ggggggg, 1992, cccccc@yahoo.com, " \
         "Vladimir 1977, Irina, 2001, annnn@intel.com, eeeeee@yandex.com," \
         "dd@intel.com, vasya@yandex.net, hello hello, Misha #43 1984, " \
         "oooooooo@hotmail.gov, gggggg@gov.by, tutututu@giv.hot"

"""
\d = Any Digit 0~9
\D = Any non Digit
\w = any Alphabet symbol [A-Z a-z]
\W = Any non Alphabet
\s = whitespace
\S = non whitespace

[0-9]{3} три подряд стоящие цифры


"""

textLookFor1 = r"yandex" # Найдет слово yandex
textLookFor2 = r"\d\d\d" # Любые три подряд стоящие цифры
textLookFor3 = r"[0-9]{3}" # Тоже три цифры подряд
textLookFor4 = r"\w{6}\s" # идет 6 символово подряд плюс пробел за ними
textLookFor5 = r"[A-Z][a-z]+" # ищет слова с большой буквы, после большой сколько угодно (+) маленьких
textLookFor6 = r"@\w+\.\w+" # ищет типо доменные имена в виде @ + символ + неважно сколько символов ".", и далее неважно сколько символов
allResults = re.findall(textLookFor6 , mytext)

print(allResults)