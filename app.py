from flask import Flask, request,jsonify
import requests

app = Flask(__name__)

@app.route('/', methods=['POST'])
def welcome():
    data = request.get_json()
    source_name =  data['queryResult']['parameters']['unit-currency']['currency']
    amount= data['queryResult']['parameters']['unit-currency']['amount']
    target_currency = data['queryResult']['parameters']['currency-name']
    cf = conversion_factor(source_name, target_currency)
    target_amount = amount * cf
    target_amount = round(target_amount,2)
    response = {
        'fulfillmentText':'{} {} is {} {}'.format(amount,source_name,target_amount,target_currency)
    }


    print("{} {} to {}".format(amount,source_name,target_currency))
    return jsonify(response)

def conversion_factor(source, target):
    url = "https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_BBAEAW92ZGtriiAvxyIU9ALEdIOaBGQNeP5EB7HO&currencies={}&base_currency={}".format(target, source)
    response = requests.get(url)
    response = response.json()
    return response['data']['{}'.format(target)]

if __name__ == "__main__":
    app.run(debug=True)

