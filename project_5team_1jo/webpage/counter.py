import matplotlib
# https://stackoverflow.com/a/53434541
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from PIL import Image
import numpy as np
from wordcloud import WordCloud
from collections import Counter
from ast import literal_eval

def makeCounter(books):
    nouns = []

    for book in books:
        keywords = []
        for each_keyword in book.keyword[:3]:
            keyword = list(each_keyword.values())[0]
            keywords.append(keyword)
        
        nouns.extend(keywords)

    return Counter(nouns)

def makeCommon(keywords):
    commons = []

    for i in keywords.most_common(10):
        commons.append(i[0])

    return commons