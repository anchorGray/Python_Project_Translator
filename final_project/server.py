'''
This is the UI end of the translation app using the IBM Watson Language Translation service
'''
from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    '''
    This takes the input for english to french translation from the HTML form 
    and passes it through the imported function via the local method 
    '''
    text1 = request.args.get('textToTranslate')
    french_text = translator.english_to_french(text1)
    return french_text

@app.route("/frenchToEnglish")
def frenchToEnglish():
        '''
    This takes the input for french to english translation from the HTML form 
    and passes it through the imported function via the local method 
    '''
    text1 = request.args.get('textToTranslate')
    english_text = translator.french_to_english(text1)
    return english_text

@app.route("/")
def render_index_page():
    '''
    This renders the HTML form 
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
