
from flask import Flask,render_template, request, jsonify
import random,json
import boto3

client = boto3.client('lambda',
                        region_name= 'us-east-2',
                        aws_access_key_id='AKIAJ7O4YCNDVVXESNIQ',
                        aws_secret_access_key='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')


application = Flask(__name__)
#app.logger.setLevel(logging.ERROR)

@application.route('/', methods = ['GET', 'POST'])
def index():
    input_text = request.values.get('user_text')

    if input_text:
        payload = {"text":input_text}
        RESULT = client.invoke(FunctionName='cloud9-zihaoprojecttest2-zihaoprojecttest2-1FDR6N0BW531Z',
                            InvocationType='RequestResponse',
                            Payload=json.dumps(payload))

        range = RESULT['Payload'].read()
        api_response = json.loads(range)
        res1 = api_response
        
        
    else:
        input_text = ''
        res1 = 'Empty Input'
        res2 = 'Empty Input'
    # res1 = random.choice(['Positive', 'Negative','Neutral'])
    # res2 = random.choice(['Positive', 'Negative', 'Neutral'])
    
    return render_template('./index.html',input_text=input_text, res1=res1, res2=res1)

if __name__ == '__main__':
    #app.run(debug=True)
    #app.run(host='0.0.0.0', debug= True)
    # host is others who will access your website
    # 127.0.0.1 -> localhost
    
    application.run(host = "0.0.0.0", port=5000, debug=True, use_reloader=True)
