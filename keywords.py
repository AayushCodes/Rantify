from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.sentiment import SentimentIntensityAnalyzer
s = SentimentIntensityAnalyzer()
sample = "I think I should not be doing engineering and open a small pastry shop in france. I will probably have a chance at love then and maybe not die a lonely virgin. I wish to live happily, bake by day and get baked by night. I would find love, be happy and be succesfull. Instead i choose to be miserable and commit suicide one day."
sample = sample.lower()
stop_words = set(stopwords.words('english'))
stop_words.update(("i","would",",","."))
word_tokens = word_tokenize(sample)
filtered_sentence = []
for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)
filtered_sentence = set(filtered_sentence)
scores = s.polarity_scores(' '.join(filtered_sentence))
print('depression =', scores['neg'] + scores['neu']//2)
print('heppy =', scores['pos'])