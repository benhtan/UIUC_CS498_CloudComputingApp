import requests
import json
import uuid

url = "https://seorwrpmwh.execute-api.us-east-1.amazonaws.com/prod/mp3-autograder-2022-spring"

payload = {
	"graphApi": 'https://lwv3a3q3n3.execute-api.us-east-1.amazonaws.com/Prod',#<post api for storing the graph>,
	"botName": 'DistanceCalc',# <name of your Amazon Lex Bot>, 
	"botAlias": 'DistanceCalc',# <alias name given when publishing the bot>,
	"identityPoolId": "us-east-1:cc2f1c89-bd9e-4b7c-9b11-a8ac2057e454",#<cognito identity pool id for lex>,
	"accountId": '793557681566', #<your aws account id used for accessing lex>,
	"submitterEmail": 'btan90@gmail.com',# <insert your coursera account email>,
	"secret": '8L87gq7c89DuDLXd', # <insert your secret token from coursera>,
	"region": 'us-east-1', #<Region where your lex is deployed (Ex: us-east-1)>
    }

r = requests.post(url, data=json.dumps(payload))

print(r.status_code, r.reason)
print(r.text)