import malaya

# Load the stemmers
naive_stemmer = malaya.stem.naive()
sastrawi_stemmer = malaya.stem.sastrawi()
deep_stemmer = malaya.stem.deep_model()

# Stem a sentence using each stemmer
sentence = 'Hasil semakan rekod jenayah mendapati suspek mempunyai tiga rekod lampau dibawah Seksyen 420 Kanun Keseksaan.'
stemmed_sentence_naive = naive_stemmer.stem(sentence)
stemmed_sentence_sastrawi = sastrawi_stemmer.stem(sentence)
stemmed_sentence_deep = deep_stemmer.stem(sentence)

# Print the results
print('Naive stemmer:', stemmed_sentence_naive)
print('Sastrawi stemmer:', stemmed_sentence_sastrawi)
print('Deep stemmer:', stemmed_sentence_deep)
