import sys

myMap = dict([
    ("q", "t"), ("h", "e"), ("y", "/"), ("n", "n"), ("m", "g"), ("i", "t"), ("p", "e"), ("w", "a"), ("s", "/"),
    ("e", "h"), ("d", "/"), ("c", "i"), ("f", "."), ("v", "n"), ("r", "/"), ("z", "t"), ("g", "t"), ("k", "h"),
    ("u", "n"), ("a", "p"), ("j", "s"), ("o", ":")

])

myMap2 = dict([
    ("b", "e"), ("y", "q"), ("o", "p"), ("n", "w"), ("m", "j"), ("c", "c"), ("r", "n"), ("g", "v"), ("z", "k"),
    ("q", "f"), ("u", "u"), ("x", "a"), ("v", "z"), ("s", "i"), ("d", "m"), ("j", "r"), ("l", "y"), ("k", "h"),
    ("a", "o"), ("e", "s"), ("i", "d"), ("w", "g")

])

myMap3 = dict([
    ("o", "u"), ("n", "y"), ("e", "l"), ("f", "b"), ("a", "i"), ("m", "e"), ("l", "n"), ("i", "a"), ("z", "v"),
    ("x", "s"), ("w", "x"), ("r", "j"), ("h", "o"), ("q", "r"), ("y", "d"), ("s", "k"), ("t", "z"), ("k", "g"),
    ("v", "w"), ("p", "m"), ("u", "q"), ("b", "c")

])

myMap4 = dict(
    [("g", "t"), ("a", "f"), ("k", "a"), ("c", "v"), ("p", "s"), ("q", "u"), ("j", "m"), ("s", "b"), ("v", "r"),
     ("b", "p"), ("n", "q"), ("u", "e"), ("e", "o"), ("f", "w"), ("w", "h"), ("l", "x"), ("i", "n"), ("h", "l"),
     ("m", "z"), ("y", "y"), ("t", "k"), ("o", "i")

     ])

myMap5 = dict(
    [("q", "h"), ("h", "s"), ("w", "q"), ("i", "u"), ("e", "g"), ("r", "y"), ("u", "l"), ("z", "b"), ("k", "v"),
     ("s", "n"), ("c", "w"), ("b", "c"), ("g", "t"), ("o", "j"), ("n", "o"), ("j", "f"), ("a", "e"), ("p", "m"),
     ("d", "p"), ("t", "i"), ("m", "a"), ("v", "k")
     ])

result = ""
word1 = ""
word2 = ""
word3 = ""
word4 = ""

for n in "mpbjznvksecauqhwgdtiro":
    word1 = word1 + myMap5[n]
for n in word1:
    word2 = word2 + myMap4[n]
for n in word2:
    word3 = word3 + myMap3[n]
for n in word3:
    word4 = word4 + myMap2[n]
for n in word4:
    result = result + myMap[n]

sys.exit(result)
