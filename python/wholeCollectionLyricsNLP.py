from collections import Counter
import pygal
import spacy

nlp = spacy.load('en_core_web_sm')
lemmatizer = nlp.get_pipe("lemmatizer")

lyrics = open("rawText/wholeCollectionLyrics.txt", "r")

words = lyrics.read()
lyricsWords = nlp(words)



def GPEcollector(words):
    GPE = []
    count = 0
    for token in lyricsWords.ents:
        if token.label_ == "GPE" and token.text != "BB" and token.text != "Angelina" and token.text != "Tellin" and token.text != "Corrina":
            count += 1
            print(count, ": ", token.text, token.label_, spacy.explain(token.label_))

            GPE.append(token.lemma_)
    return GPE

listGPE = GPEcollector(lyricsWords)
GPE_freq = Counter(listGPE)
GPETopTwenty = GPE_freq.most_common(20)
GPETopTen = GPE_freq.most_common(10)
print(GPETopTwenty)
print(GPETopTen)
GPELastTen = GPE_freq.most_common()[:5:1]

bar_chartTopTwentyGPE = pygal.Bar()
bar_chartTopTenGPE = pygal.Bar()
bar_chartTopTwentyGPE.title='Top 20 Geopolitical Entities Mentioned in Whole Blues Collection'
bar_chartTopTenGPE.title = 'Top 10 Geopolitical Entities Mentioned in Whole Blues Collection'

print(bar_chartTopTwentyGPE.title)
print(bar_chartTopTenGPE.title)
for t in GPETopTen:
    print(t[0], t[1])
    bar_chartTopTenGPE.add(t[0], t[1])
for e in GPETopTwenty:
    # this is a list of tuples, so we return its values like this:
    print(e[0], e[1])
    bar_chartTopTwentyGPE.add(e[0], e[1])

print(bar_chartTopTwentyGPE.render(is_unicode=True))
print(bar_chartTopTenGPE.render(is_unicode=True))
bar_chartTopTwentyGPE.render_to_file('COLLECTION_GPENTITYbar_chartTopTwenty.svg')
bar_chartTopTenGPE.render_to_file('COLLECTION_GPENTITYbar_TopTen.svg')




def PPLcollector(words):
    PPL = []
    count = 0
    for token in lyricsWords.ents:
        if token.label_ == "PERSON" and token.text != "St Louis" and token.text != "Mm" and token.text != "Soul" and token.text != "Yeh" and token.text != "standin" and token.text != "Whoah":
            count += 1
            print(count, ": ", token.text, token.label_, spacy.explain(token.label_))

            PPL.append(token.lemma_)
    return PPL

listPPL = PPLcollector(lyricsWords)
PPL_freq = Counter(listPPL)
PPLTopTwenty = PPL_freq.most_common(20)
PPLTopTen = PPL_freq.most_common(10)
print(PPLTopTwenty)
print(PPLTopTen)
PPLLastTen = PPL_freq.most_common()[:5:1]

bar_chartTopTwentyPPL = pygal.Bar()
bar_chartTopTenPPL = pygal.Bar()
bar_chartTopTwentyPPL.title='Top 20 Names Mentioned in Whole Blues Collection'
bar_chartTopTenPPL.title = 'Top 10 Names Mentioned in Whole Blues Collection'

print(bar_chartTopTwentyPPL.title)
print(bar_chartTopTenPPL)
for p in PPLTopTen:
    print(p[0], p[1])
    bar_chartTopTenPPL.add(p[0], p[1])

for e in PPLTopTwenty:
    # this is a list of tuples, so we return its values like this:
    print(e[0], e[1])
    bar_chartTopTwentyPPL.add(e[0], e[1])

print(bar_chartTopTwentyPPL.render(is_unicode=True))
print(bar_chartTopTenPPL.render(is_unicode=True))
bar_chartTopTwentyPPL.render_to_file('COLLECTION_PEOPLEbar_chartTopTwenty.svg')
bar_chartTopTenPPL.render_to_file('COLLECTION_PPLbar_TopTen.svg')



def nouncollector(words):
    Nouns = []
    count = 0
    for token in words:
        if token.pos_ == "NOUN":
            count += 1
            Nouns.append(token.lemma_)
    return Nouns

print("TOP TEN NOUNS:")
listNouns = nouncollector(lyricsWords)
noun_freq = Counter(listNouns)
nounTopTen = noun_freq.most_common(10)
print(nounTopTen)

nounBar_chartOver10 = pygal.Bar()
nounBar_chartTopTen = pygal.Bar()

nounBar_chartOver10.title = 'Nouns Used Over 10 Times in Song Lyrics from Entire Collection'
nounBar_chartTopTen.title = 'Top 10 Nouns in Songs from Entire Collection'
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

print(nounBar_chartOver10.render(is_unicode=True))
nounBar_chartOver10.render_to_file('collectionNOUNbar_Over10.svg')
nounBar_chartTopTen.render_to_file('collectionNOUNbar_TopTen.svg')
