# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import spacy
from spacy import displacy
from spacy.matcher import Matcher
from spacy import displacy




# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    textstring="I happy mother boyfriend not happy"
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(textstring)
    html = displacy.render(doc, style='dep', page=True)
    print(html)












