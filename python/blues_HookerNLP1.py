import spacy

# nlp = spacy.cli.download("en_core_web_sm")

nlp = spacy.load('en_core_web_sm')

hookerWordList = open('JLHooker_Words.txt', 'r')
words = hookerWordList.readlines()
wordstrings = str(words)

count=0
for w in words:
    count += 1
   # print(count, ": ", w)


hookerWordList = nlp(wordstrings)
for token in hookerWordList:
    print(token.text, "---->", token.pos_, "::", token.lemma_)

    #mia: not sure why there's a \n after all of the words..? 
