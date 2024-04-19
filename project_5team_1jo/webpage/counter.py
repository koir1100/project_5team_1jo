import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
from wordcloud import WordCloud
from collections import Counter
from ast import literal_eval

def makeCounter(books):
    nouns = []

    for i in books:
        nouns += literal_eval(i.keyword)

    return Counter(nouns)

def makeCommon(keywords):
    commons = []

    for i in keywords.most_common(10):
        commons.append(i[0])

    return commons