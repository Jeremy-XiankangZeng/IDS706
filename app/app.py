from flask import Flask,render_template
import random

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    input_text = 'I like it'
    input_text = "Our application provides sentiment analysis for your customized text based on pre-trained " \
                 "machine learning and deep learning models. The results are in 3 categories: positive, neutral and negative."
    res = random.choice(['Positive', 'Negative','Neutral'])
    return render_template('./index.html',input_text=input_text, res = res)

if __name__ == '__main__':
    app.run(debug=True)