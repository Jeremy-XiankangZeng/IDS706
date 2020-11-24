from flask import Flask,render_template, request
import random,json
import boto3

client = boto3.client('lambda',
                        region_name= 'es-east-2',
                        aws_access_key_id='AKIAVXCIIWAWTMZIIJ2U',
                        aws_secret_access_key='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')


app = Flask(__name__)
#app.logger.setLevel(logging.ERROR)

@app.route('/', methods = ['GET', 'POST'])
def index():
    input_text = request.values.get('user_text')

    if input_text:
        payload = {"text":input_text}
        RESULT = client.invoke(FunctionName='cloud9-zihaoAWSComprehendTe-zihaoAWSComprehendTest-1821L8MSNKCZY',
                            InvocationType='RequestResponse',
                            Payload=json.dumps(payload))

        range = RESULT['Payload'].read()
        api_response = json.loads(range)
        res1 = api_response
        
    else:
        input_text = ''
        res1 = 'Empty Input'
        res2 = 'Empty Input'
    
    return render_template('./index.html',input_text=input_text, res1=res1, res2=res1)

if __name__ == '__main__':
    #app.run(debug=True)
    #app.run(host='0.0.0.0', debug= True)
    # host is others who will access your website
    # 127.0.0.1 -> localhost
    
    app.run(host = "0.0.0.0", port=5000, debug=True, use_reloader=True)
    # port=5000, 
