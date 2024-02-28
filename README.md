# Word-Suggester

Essentially, what this does is it takes a .docx file and looks for words that repeat.

It then suggests alternatives using a thesaurus API (that's kinda meh b/c getting a Merriam Webster API key is annoying and I don't want to apply for it)

It is a bit messy, but it works.

Make sure you do `pip install python-docx`, then run synonyms.py

It will go through each word and its synonyms, but it might be a bit taxing if the essay runs long
