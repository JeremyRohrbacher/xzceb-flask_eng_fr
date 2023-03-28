import machinetranslation
from machinetranslation.translator import englishToFrench, frenchToEnglish
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def english_to_french():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    result = machinetranslation.translator.english_to_french(textToTranslate)
    
    return result

@app.route("/frenchToEnglish")
def french_to_english():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    result = machinetranslation.translator.french_to_english(textToTranslate)
    
    return result

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
