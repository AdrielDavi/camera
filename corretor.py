#pip install pyspellchecker
from spellchecker import SpellChecker

spell = SpellChecker(language='pt') #Dicionário português - Portugal

words: list = "caza germi vid onho casros".split()
list_of_correct_words: list = [spell.correction(word) for word in words]
"""
for i in p:
    x = 
    correct_words.append(spell.correction(word))
"""
final_word = ""
for word in list_of_correct_words:
    final_word += word + " "

print(final_word)
