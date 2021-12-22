from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
friday_god = "I think I should not be doing engineering and open a small pastry shop in france. I will probably have a chance at love then and maybe not die a lonely virgin. I wish to live happily, bake by day and get baked by night. I would find love, be happy and be succesfull. Instead i choose to be miserable and commit suicide one day."
friday_god = friday_god.lower()
stop_words = set(stopwords.words('english'))
stop_words.update(("i","would",",","."))
word_tokens = word_tokenize(friday_god)
filtered_sentence = []
for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)
filtered_sentence = set(filtered_sentence)
print((filtered_sentence))