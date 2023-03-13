# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import spacy

from spacy import displacy
from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():

    html = ""


    return render_template('index.html')

@app.route("/anlyse", methods=['GET'])
def hello():
    textstring = request.args['projectFilepath']
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(textstring)
    html = displacy.render(doc, style='dep', page=True)

    return html




# Press the green button in the gutter to run the script.
##
#if __name__ == '__main__':

 #   textstring="I happy mother boyfriend not happy"
  #  nlp = spacy.load("en_core_web_sm")
   # doc = nlp(textstring)
    #html = displacy.render(doc, style='dep', page=True)
    #print(html)













