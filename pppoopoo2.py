import yake
kw_extractor = yake.KeywordExtractor()
text = "I think I should not be doing engineering and open a small pastry shop in france. I will probably have a chance at love then and maybe not die a lonely virgin. I wish to live happily, bake by day and get baked by night. I would find love, be happy and be succesfull. Instead i choose to be miserable and commit suicide one day."
sample = "I am so happy my heart is exploding. I want to fall in love. I have some hellish desires I wanna fulfill. The future appears to be so bright."
language = "en"
max_ngram_size = 3
deduplication_threshold = 0.9
numOfKeywords = 10
custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_threshold, top=numOfKeywords, features=None)
keywords = custom_kw_extractor.extract_keywords(sample)
pp = []
for kw in keywords:
    pp.append(kw[0])
from nltk.sentiment import SentimentIntensityAnalyzer
s = SentimentIntensityAnalyzer()
scores = s.polarity_scores(' '.join(pp))
print('depression =', scores['neg'])
print('heppy =', scores['pos'])
print(scores)