from flask import Flask,render_template, request
import random

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    input_text = request.values.get('user_text')
    if input_text:
        res1 = random.choice(['Positive', 'Negative','Neutral'])
        res2 = random.choice(['Positive', 'Negative', 'Neutral'])
    else:
        input_text = ''
        res1 = 'Empty Input'
        res2 = 'Empty Input'
    return render_template('./index.html',input_text=input_text, res1=res1, res2=res2)

if __name__ == '__main__':
    app.run(debug=True)