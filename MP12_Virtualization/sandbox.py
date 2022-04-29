from kubernetes import client, config
from flask import Flask,request
from os import path
import yaml, random, string, json
import sys
import json

# Configs can be set in Configuration class directly or using helper utility
config.load_kube_config()
v1 = client.CoreV1Api()

def premium_job():
    with open(path.join(path.dirname(__file__), "premium-job.yaml")) as f:
        # Look into the usage of yaml.safe_load()
        dep = yaml.safe_load(f)
        # print `dep` to see the structure

        # To-do: generate a random deployId
        # To-do: replace some attributes of `dep` with the arguments in `body`

        k8s_apps_v1 = client.BatchV1Api()
        resp = k8s_apps_v1.create_namespaced_job(body=dep, namespace="default")
        # print `resp` to see the response

def free_job():
    with open(path.join(path.dirname(__file__), "free-job.yaml")) as f:
        # Look into the usage of yaml.safe_load()
        dep = yaml.safe_load(f)
        # print `dep` to see the structure

        # To-do: generate a random deployId
        # To-do: replace some attributes of `dep` with the arguments in `body`

        k8s_apps_v1 = client.BatchV1Api()
        resp = k8s_apps_v1.create_namespaced_job(body=dep, namespace="free-service")
        # print `resp` to see the response

def get_config():
    pods = []

    # your code here
    pods = v1.list_pod_for_all_namespaces(watch=False)
    
    # print(type(pods))
    for i in pods.items:
        # print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))
        # print(f'{i.metadata.namespace} {i.metadata.name} {i.status}')
        print(f'{i.metadata}')
        break

get_config()