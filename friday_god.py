import yake
from nltk.sentiment import SentimentIntensityAnalyzer
import spelling
kw_extractor = yake.KeywordExtractor()
text = "I think I should not be doing engineering and open a small pastry shop in france. I will probably have a chance at love then and maybe not die a lonely virgin. I wish to live happily, bake by day and get baked by night. I would find love, be happy and be succesfull. Instead i choose to be miserable and commit suicide one day."
sample = "I am so happy my heart is exploding. I want to fall in love. I have some hellish desires I wanna fulfill. The future appears to be so bright."
lol = "i am sad"
hep = 'i am happy'
kk = 'I wish I was die'
ll = 'I am the luckiest man in the world'
longboi = 'I sometimes feel so empty insidej that I tamlk to myiself for hours at end. If I do not find anysone to love me soon, then I might just leap off a cliff and just die. I mean it gets so lonely sometimes. It\'s not even about being desperate or something but i feel so empty in my heart. There is no one to listen to me and no reason to live. I mean what am i doing wrong. I was once happy and now I just feel i have been dead inside for years.' 
complex = 'I am kind of neutral today. I feel so hopeless sometimes but also so excited for some other things. Life has become an emotional rollecoster. I want to party but also remain in my bed all sad. I do not know what to anymore and it is the confusion that is eating me alive'
dep = "He was my bestfriend and I trusted him more than I trusted myself. And to think he would do such a horrible thing to me would seem impposible."
alle = "All my friends are toxic or ambitionless so rude and always negative, I need new friends but it's not that quick and easy oh i'm drowning let me breathe."
posi = "I am so happy today!It was my birthday today and I was feeling lonely but my old friends hit me up and took me bowling. It was so fun and then we went to a party and crashed at my place again. Feels good to have company sometimes you know"
gudu = ""
friday = [text, lol, sample, hep, kk, ll, longboi, complex,dep,alle,posi,]
language = "en"
max_ngram_size = 3
deduplication_threshold = 0.9
numOfKeywords = 10
custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_threshold, top=numOfKeywords, features=None)

def rant_check(i):
    i = spelling.spellcheck(i)
    keywords = custom_kw_extractor.extract_keywords(i)
    pp = []
    for kw in keywords:
        pp.append(kw[0])
    s = SentimentIntensityAnalyzer()
    scores = s.polarity_scores(' '.join(pp))
    print(i)
    #print('depression =', scores['neg'] + 0.000001)
    #print('heppy =', scores['pos'] + 0.000001)
    heppy = scores['pos'] + 0.00000001
    sed = scores['neg'] + 0.00000001
    if heppy > sed:
        print('heppy')
    else:
        print('sed')