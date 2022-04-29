from kubernetes import client, config
from flask import Flask,request
from os import path
import yaml, random, string, json
import sys
import json

# Configs can be set in Configuration class directly or using helper utility
config.load_kube_config()
v1 = client.CoreV1Api()
batch_v1 = client.BatchV1Api()
app = Flask(__name__)
# app.run(debug = True)

@app.route('/config', methods=['GET'])
def get_config():
    pods_list = []

    # your code here
    pods = v1.list_pod_for_all_namespaces(watch=False)
    
    # print(type(pods))
    for i in pods.items:
        # print(f'{i.spec.node_name} {i.status.pod_ip} {i.metadata.namespace} {i.metadata.name} {i.status.phase}')
        pods_list.append({'node': i.spec.node_name, 'ip': i.status.pod_ip, 'namespace': i.metadata.namespace, 'name': i.metadata.name, 'status': i.status.phase})

    pods_list = {'pods': pods_list}
    # print(pods_list)
    
    output = json.dumps(pods_list)
    # print(output)

    return output, 200

@app.route('/img-classification/free',methods=['POST'])
def post_free():
    # your code here

    return "success"


@app.route('/img-classification/premium', methods=['POST'])
def post_premium():
    # your code here

    return "success"

    
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)
