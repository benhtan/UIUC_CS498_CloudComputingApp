import requests
import json
import uuid

url = "https://seorwrpmwh.execute-api.us-east-1.amazonaws.com/prod/mp3-autograder-2022-spring"

payload = {
	"graphApi": 'https://lwv3a3q3n3.execute-api.us-east-1.amazonaws.com/Prod',#<post api for storing the graph>,
	"botName": # <name of your Amazon Lex Bot>, 
	"botAlias": # <alias name given when publishing the bot>,
	"identityPoolId": #<cognito identity pool id for lex>,
	"accountId": #<your aws account id used for accessing lex>,
	"submitterEmail": # <insert your coursera account email>,
	"secret": # <insert your secret token from coursera>,
	"region": #<Region where your lex is deployed (Ex: us-east-1)>
    }

r = requests.post(url, data=json.dumps(payload))

print(r.status_code, r.reason)
print(r.text)