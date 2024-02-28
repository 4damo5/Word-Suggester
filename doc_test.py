from docx import Document
import statistics

#potential anomaly:
#if the essay is about common words, it will exclude the topic as words to change 
common_words = open('common_words.txt').read().split()

doc = Document("Green.docx")
core_props = doc.core_properties

paragraph = doc.paragraphs
paragraph_lengths = [len(paragraph[i].text.split()) for i in range(len(paragraph))]

word_count_dict = {}

#lower limit for paragraphs
#using this to sort whether its a heading title or not
paragraph_lower_lim = statistics.mean(paragraph_lengths) - statistics.stdev(paragraph_lengths) / len(paragraph_lengths) ** .5
#print(paragraph_lower_lim)



#list of all paragraphs 
paragraph_word_list = [paragraph[i].text.split() for i in range(len(paragraph)) if len(paragraph[i].text.split()) > paragraph_lower_lim]

#list of all the words in paragraphs but in one list
word_list = []
for pa in paragraph_word_list:
    for word in pa:
        word_list.append(word)




#removes punctuation and figures from all elements
for word in range(len(word_list)):
    no_punc = ''
    for char in word_list[word]:
        if char.isalpha():
            no_punc += char
    #print(no_punc, end=' ')
    if word_list[word].islower():
        word_list[word] = no_punc
    else: 
        word_list[word] = ''

#removes blanks from removed punctuation
for blanks in range(word_list.count('')):
    word_list.remove('')

#print(word_list)
    
wl_index = 0

#index over # of paragraphs
while wl_index < len(paragraph):
    if len(paragraph[wl_index].text.split()) > paragraph_lower_lim:
        for word in word_list:
            #was getting weird bugs for word 3D printer where it stripped the 3 and just added ds', 
            #the len(word) at the end fixes this and removes some more common words and anomalies
            if word not in common_words and word_list.count(word) != 1 and len(word) > 1:
                word_count_dict[word] = word_list.count(word)
    wl_index += 1

#essentially sorts the count list into a interpretable way to distinguish which words are most common
sorted_count_dict = dict(sorted(word_count_dict.items(), key=lambda x:x[1], reverse = True))
#print(sorted_count_dict)

