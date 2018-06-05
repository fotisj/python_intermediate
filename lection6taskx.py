import pandas as pd
from collections import Counter 
import re    
import matplotlib.pyplot as plt

def visualize(data):
    [plt.bar(x[0],x[1]) for x in list(data.items())]
    plt.show()

def calc_types(filename):
    with open (filename, "r", encoding="utf-8") as fi:
        words = Counter() 
        for l in fi:
            wl = re.findall("\w+", l)
            for w in wl:
                words[w] += 1
    s = pd.Series(list(words.keys()))
    wl = s.str.len()
    print("Wordlength < 6 in word types: ", len(wl[wl<6])/len(wl))
    visualize(Counter(wl))

def calc_tokens(filename):
    with open (filename, "r", encoding="utf-8") as fi:
        text = fi.read()
        words = re.findall("\w+", text)
    wl = pd.Series(words).str.len()
    print("Wordlength < 6 in word tokens", len(wl[wl<6])/len(wl))
    visualize(Counter(wl))


calc_types("effi.txt")
calc_tokens("effi.txt")