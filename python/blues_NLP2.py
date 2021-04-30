from collections import Counter
import pygal
import spacy
# Need line 8 the first time: Then comment it out after the first time you run it:
# nlp = spacy.cli.download("en_core_web_sm")
nlp = spacy.load('en_core_web_sm')
lemmatizer = nlp.get_pipe("lemmatizer")
#print(lemmatizer.mode)  # 'rule'

JLHooker = open('JLHooker_Words_ebb.txt', 'r')
# If, when you print the file, it comes out with weird characters in place of apostrophes, quotes, etc.,
# try adapting this alternative version of the line above:
# yourtext = open('yourtext.txt', 'r', encoding="utf8", errors='ignore')

words = JLHooker.read()
hookerWords = nlp(words)

#hookerWordList = nlp(hookerWords)

#words = disneysongs.read()
#disneywords = nlp(words)
# print(words)

def nouncollector(words):
    Nouns = []
    count = 0
    for token in words:
        if token.pos_ == "NOUN":
            count += 1
            Nouns.append(token.lemma_)
    return Nouns

print("TOP TEN NOUNS:")
listNouns = nouncollector(hookerWords)
noun_freq = Counter(listNouns)
nounTopTen = noun_freq.most_common(10)
print(nounTopTen)

nounBar_chartOver10 = pygal.Bar()
nounBar_chartTopTen = pygal.Bar()

nounBar_chartOver10.title = 'Nouns Used Over 10 Times in John Lee Hooker Song Lyrics'
nounBar_chartTopTen.title='Top 10 Nouns in John Lee Hooker Songs'
print(nounBar_chartOver10.title)
for n in noun_freq:
    # verb_freq is a dictionary structure, so we return its key and its value:
    print(n, noun_freq[n])
    if noun_freq[n] > 10:
        nounBar_chartOver10.add(n, noun_freq[n])

print(nounBar_chartTopTen.title)
for o in nounTopTen:
    # this is a list of tuples, so we return its values like this:
    print(o[0], o[1])
    nounBar_chartTopTen.add(o[0], o[1])

# print(bar_chart)
print(nounBar_chartOver10.render(is_unicode=True))
nounBar_chartOver10.render_to_file('NOUNbar_chartOver10.svg')
nounBar_chartTopTen.render_to_file('NOUNbar_chartTopTen.svg')






def verbcollector(words):
    Verbs = []
    count = 0
    for token in words:
        if token.pos_ == "VERB":
            count += 1
            # print(count, ": ", token.text, " lemma: ", token.lemma_, " pos: ", token.pos_)
            # don't forget the underscore after token.lemma_ , token.pos_, etc.!
            Verbs.append(token.lemma_)
            #print(count, ": ", token, token.pos_, spacy.explain(token.pos_))
    # print(count, ": ", Verbs)
    return Verbs

print("TOP TEN VERBS:")
listVerbs = verbcollector(hookerWords)
verb_freq = Counter(listVerbs)
topTen = verb_freq.most_common(10)
print(topTen)
lastTen = verb_freq.most_common()[:5:1]
#print("5 LEAST COMMON VERBS:")
#print(lastTen)

# ebb: Okay, let's try out the pygal graphing library!
# Here I am experimenting and creating TWO bar graphs. For homework you only need to create one.
# I made one bar graph called bar_chartOver10, and another that I like much better called bar_chartTopTen
bar_chartOver10 = pygal.Bar()
bar_chartTopTen = pygal.Bar()

bar_chartOver10.title = 'Verbs Used Over 10 Times in John Lee Hooker Song Lyrics'
bar_chartTopTen.title='Top 10 Verbs in John Lee Hooker Song'
print(bar_chartOver10.title)
for v in verb_freq:
    # verb_freq is a dictionary structure, so we return its key and its value:
    print(v, verb_freq[v])
    if verb_freq[v] > 10:
        bar_chartOver10.add(v, verb_freq[v])

print(bar_chartTopTen.title)
for t in topTen:
    # this is a list of tuples, so we return its values like this:
    print(t[0], t[1])
    bar_chartTopTen.add(t[0], t[1])

# print(bar_chart)
print(bar_chartOver10.render(is_unicode=True))
bar_chartOver10.render_to_file('VERBbar_chartOver10.svg')
bar_chartTopTen.render_to_file('VERBbar_chartTopTen.svg')


# On windows ctrl / comments out blocks.
# On mac command / comments out blocks

# lowercaseList = []
# for l in listVerbs:
#     l = str(l).lower()
#     lowercaseList.append(l)
# setVerbs = set(lowercaseList)
# count = 0
# for s in setVerbs:
#     count += 1
# print(sorted(setVerbs))
# print(count)


