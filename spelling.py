from textblob import TextBlob
def spellcheck(a):
    x = []
    for i in a.split():
        b = TextBlob(i)
        x.append(str(b.correct()))
    a = ' '.join(x)
    return a