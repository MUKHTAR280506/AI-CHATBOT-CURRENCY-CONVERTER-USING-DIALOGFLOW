# AI-CHATBOT-CURRENCY-CONVERTER-USING-DIALOGFLOW
AI CHATBOT FOR CURRENCY CONVERTOR USING GOOGLE'S  DIALOGFLOW

This is AI chatbot for currency conversion. Chatbot is integrated with Telegram.  It gives the latest rates of the currency.
It can give latest rates for 33 currency including USD, GBP, INR, CAD etc. List of supported currency can be checked in URL https://app.freecurrencyapi.com/request-playground.

language used -  Python
web framework- Flask


Library used - check the requirements.txt file


Steps to make the chatbot.

Step 1- Create the Chatbot (Agents) using Google's Dialogflow which is a Natural Language
        Understanding platform. Define intents (user inputs) and corresponding response	(chatbot reply) for the Agents
        refer link https://www.geeksforgeeks.org/getting-started-with-dialogflow/     for more information

Step 2- Create a simple web application ( i am using Flask web framework) to get the json
        response from the chatbot. Analyse the json response in any json viewer (https://jsonviewer.stack.hu/) and get
        the required key value pair . In our project it is currency-name and amount.

Step 3 - Now make your local webservers to internet via proxy tool . We used ngrok for this project
         run ngrok http 5000  in ngrok terminal , you will get the URL . paste this URL to Dialog flow chatbot 
         Fulfillment->Webhook->URL
         also enable fulfillment under intent --> fulfillment-> enable webhook call for this intent 

step 4-  Implement the logic in our app.py to the get value from json response

step 5 - Now get the latest currency rates from Internet using currency conversion sites
         e.g  https://app.freecurrencyapi.com/request-playground

Step 6 - Implement conversion logic in app.py for target currency and return the response
         to chatbot 

Step 7 - Now test your chatbot with intent and check for the real time response

Step 8 - Go to integrations and run the chatbot with the options available like Webdemo, Telegram etc

Step 9 - create a bot in telegram with botfather and get the token and paste the token in dialogflow integration with telegram
          
![TELEGRAM CHAT](https://github.com/user-attachments/assets/bb08efe3-1902-4fd4-a828-2ed7dcea08a3)
![CHATBOT IMAGE](https://github.com/user-attachments/assets/ee507036-44cc-4038-9c98-29880fd80d3d)


 

