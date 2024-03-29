import yake
from nltk.sentiment import SentimentIntensityAnalyzer
import language_tool_python
tool = language_tool_python.LanguageTool('en-US')
kw_extractor = yake.KeywordExtractor()
language = "en"
max_ngram_size = 3
deduplication_threshold = 0.9
numOfKeywords = 10
custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_threshold, top=numOfKeywords, features=None)

def rant_check(i):
    i = tool.correct(i)
    keywords = custom_kw_extractor.extract_keywords(i)
    sample = []
    for kw in keywords:
        sample.append(kw[0])
    s = SentimentIntensityAnalyzer()
    scores = s.polarity_scores(' '.join(sample))
    pos = scores['pos'] + 0.00000001
    neg = scores['neg'] + 0.00000001
    if pos > neg:
        return 1
    else:
        return 0