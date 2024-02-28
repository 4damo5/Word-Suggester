
import requests
from docx import Document
import doc_test as dt

#thesaurus API HAS GAPS Ex. Bottle
#https://api-ninjas.com/api/thesaurus

#potential doc editing
#https://www.rikvoorhaar.com/blog/python_docx
#need to learn to create a copy
#doc.save('path')
#https://python-docx.readthedocs.io/en/latest/api/document.html#id1
#https://python-docx.readthedocs.io/en/latest/api/document.html#docx.opc.coreprops.CoreProperties
#


#print(dt.sorted_count_dict)

#pseudocode 
#while there are words in the essay, 
#check count of each word to see if any are used more than once
#ignore is, the, a, to, etc
#ignore capitalized words / .isupper() words

#if any words are on the "list of most common words" replace these
#otherwise just replace the additional uses of the word with a synonym

#show some variations and give a summary of what you changed
#read a .doc file and dont edit the styling, only the word choice


for word in dt.sorted_count_dict.keys():
    api_url = 'https://api.api-ninjas.com/v1/thesaurus?word={}'.format(word)

    response = requests.get(api_url, headers={'X-Api-Key': open('key.txt').read()}) #*** REMOVE API KEY WHEN ADDING TO GITHUB
    if response.status_code == requests.codes.ok:
        if response.json()["synonyms"] != []:
            print(f'\n{response.json()["word"].capitalize()}')
            print('='*10)
            try:
                for syns in range(dt.sorted_count_dict[word]):
                    print(syns, response.json()["synonyms"][syns])
                input('next? ')
            except:
                input('\nnext? ')
    else:
        print("Error:", response.status_code, response.text)