import requests
import json

url = 'https://seorwrpmwh.execute-api.us-east-1.amazonaws.com/prod/mp2-autograder-2022-spring'

payload = {
		'ip_address1': '54.183.95.202:5000', # <insert ip address:port of first EC2 instance>, 
		'ip_address2': '3.101.13.19:5000', # <insert ip address:port of second EC2 instance>,
		'load_balancer' : 'CS498-MP2-1274606434.us-west-1.elb.amazonaws.com', # <insert address of load balancer>,
		'submitterEmail': 'btan90@gmail.com', # <insert your coursera account email>,
		'secret': 'FfIzPkJMyOpbwGIq' # <insert your secret token from coursera>
		}

r = requests.post(url, data=json.dumps(payload))

print(r.status_code, r.reason)
print(r.text)