import random
sen = ""
global encSen
encSen = ""
n = random.randint(1,25)
symb=[" ", ",", ".", "!", "?", ":", ";", "'"]
def encode(sen):
    s = [*sen.lower()]
    def lOutput(x):
        if x in symb:
            return x
        else:
            return chr(ord('`')+x)
    def lInput(x):
        if x in symb:
            return x
        else:
            for i in range(1,27):
                if chr(ord('`')+i) == x:
                    return i
    def overAlphabet(x,y):
        if x in symb:
            return x
        elif x + y > 26:
            return x+y-26
        else:
            return x+y
    for I in range(len(s)):
        s[I] = lOutput(overAlphabet(lInput(s[I]),n))
    for l in range(len(s)):
        if sen[l] == (sen[l]).upper():
            s[l] = s[l].upper()
    return (''.join(s))
print(encode(sen))