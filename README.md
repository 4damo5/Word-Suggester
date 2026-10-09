# Word-Suggester

Reads a `.docx` essay, finds words you repeat too often, and suggests synonyms using the [API Ninjas thesaurus](https://api-ninjas.com/api/thesaurus).

- Skips headings (paragraphs much shorter than average), capitalized words, and a list of common words (`common_words.txt`)
- Ranks repeated words by frequency, then steps through each with suggested replacements

## Usage
```
pip install python-docx requests
```
1. Put your API Ninjas key in `key.txt` (not committed).
2. Set the document name in `doc_test.py`.
3. `python3 synonym.py`

Long essays make one API call per repeated word, so they take a while.
