# Correct Spellings using Python

from spellchecker import SpellChecker

corrector = SpellChecker()

word = input('Enter a word: ')

if word in corrector:
    print('Correct Spelling')
else:
    word = corrector.correction(word)
    print('Right Spelling is :', word)
