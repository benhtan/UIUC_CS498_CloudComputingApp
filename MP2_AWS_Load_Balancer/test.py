import requests
import json

url = 'https://seorwrpmwh.execute-api.us-east-1.amazonaws.com/prod/mp2-autograder-2022-spring'

payload = {
		'ip_address1':  # <insert ip address:port of first EC2 instance>, 
		'ip_address2':  # <insert ip address:port of second EC2 instance>,
		'load_balancer' :  # <insert address of load balancer>,
		'submitterEmail':  # <insert your coursera account email>,
		'secret':  # <insert your secret token from coursera>
		}

r = requests.post(url, data=json.dumps(payload))

print(r.status_code, r.reason)
print(r.text)