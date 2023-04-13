from random_word import RandomWords
r = RandomWords()

# Return a single random word
r.get_random_word()
# Return list of Random words
r.get_random_words()
# Return Word of the day
r.word_of_the_day()

print(r.get_random_word(hasDictionaryDef="True", includePartOfSpeech="noun,verb", minCorpusCount=1, maxCorpusCount=10, minDictionaryCount=1, maxDictionaryCount=10, minLength=5, maxLength=10))


print(r.get_random_word(hasDictionaryDef='True', includePartOfSpeech="verb"))
