import spacy
nlp = spacy.load("en_core_sci_lg")
text = "I think I should not be doing engineering and open a small pastry shop in france. I will probably have a chance at love then and maybe not die a lonely virgin. I wish to live happily, bake by day and get baked by night. I would find love, be happy and be succesfull. Instead i choose to be miserable and commit suicide one day."
doc = nlp(text)
print(doc.ents)
