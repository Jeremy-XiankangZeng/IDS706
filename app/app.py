from flask import Flask,render_template, request
import random,json

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    input_text = request.values.get('user_text')
    if input_text:
        res = random.choice(['Positive', 'Negative','Neutral'])
    else:
        input_text = ''
        res = 'Empty Input'
    return render_template('./index.html',input_text=input_text, res=res)

if __name__ == '__main__':
    app.run(debug=True)