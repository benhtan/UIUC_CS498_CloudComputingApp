# MP12 Concerns and FAQs

## MP context diagram: (Designed by students)
https://docs.google.com/drawings/d/16n-ll084RyDPXsXzRvz0RI1N02CT1VxtslrslhIqssk/edit

## How to access a worker node in EKS?

Type `kubectl get svc` and get the IP addresses of the worker nodes and then use ssh 
`kubectl get nodes`

## Do we have to create a new VPC?

Not required.

## Some useful commands:

```
kubectl get deployments -A --all-namespaces
kubectl get jobs -A --all-namespaces
kubectl describe <...>
kubectl get pods -A --all-namespaces
kubectl describe pod <pod_name> --all-namespaces
kubectl logs <...>
kubectl get nodes -A --all-namespaces
docker ps -a
docker container prune
docker images
```

## When specifying an image within a yaml file for kubectl, how do I specify a local docker file?  

When you create a docker image, it gets deployed to your local docker image
repo. You just have to specify that image name within the yaml file under
image. 

## Exposing Image Classification
- Created GET "/config" endpoint to return pod details
- Created two POST endpoints: one for free and another one for premium (HINT: DATASET value mnist vs kmnist ;-))
- Log debug messages from your RESTful endpoints so that you can find out what's going when you run test.py
- Created a simple shell script on node 0 to delete jobs. Required before running test.py
- Finally delete all the services

## Resource Provisioning
- Followed the instruction at https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/quota-memory-cpu-namespace/ to create & apply resource quota
- Locally tested the resource quota on node 0
- Ensured that atmost there can be only two free-service jobs and there can be any number of premium jobs
- In the job yaml file(s) you can use generateName instead of name to get a unique name and be able to create new job using the same yaml file

## Deploying to cluster
- Created two job specs (one for free service and another one for premium)
- Tested job specs locally on node 0
- Defined ENV in job spec

## Students suggested MP guide: 
https://docs.google.com/document/d/1cPkPejiiuqjq0czuG2WsEsASueYTWpl5aPpBr1a1KUM/edit?usp=sharing


## Also a few tips to save you some money in AWS. you can work in this order:
1. Containerize the classify.py first (you may need a t2.medium to build the image and test container, with ~20GB volume. You can change it back to t2.micro)
2. Develop the web application to expose image classification. (you can't test at this point just yet)
3. Configure kubernetes and launch AWS EKS (you can delete cluster or detach node group and recreate if you have to)
4. Test job deployment manually, and then Test the web application (for every test you should delete jobs from both default and free-service namespaces)


## How can I minimize the cost?

EKS along with 2 t3 medium nodes charge about ~ $0.2 / hour which you can start
and stop as you work on the MP. If you want to minimize this cost further, you
can do everything from section 3.2 to 3.5 locally and then deploy it to EKS. In
order to setup kubernetes on your local machine, the following tutorial will
help: https://kubernetes.io/docs/setup/learning-environment/minikube/ While
this will start a single node server, most of the configurations will still
stay the same.

## I have set up Docker, Flask server etc. on my EC2 instance of educate starter account. Do I have to set it up again on my personal EC2 to access EKS?

No. You can access EKS through any system as far as you have configured aws credentials properly. 
https://docs.aws.amazon.com/eks/latest/userguide/getting-started-eksctl.html
https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html

## am spending too much time on this MP. What should I do?
It is extremely important to have a conceptual understanding first and then try to approach this MP. 

## When I run my jobs, the status goes to ContainerCantRun. 
Use your path variables value and add it to the dockerfile. When you build the docker it will now include an updated path.

## The Docker image created to run the provided script lives on Docker Hub. Where exactly do Kubernetes live in our system? It can't be either of the 2 EC2 instances, right?
K8s acts as a container management tool. 

## From what I understand, Kubernetes just executes our Docker containers in a specific state, such as setting the Environment variables, correct?
K8s acts as a container management tool. 

## When we invoke Kubernetes in AWS, how will it know how to reach our EC2 instances?
You need to specify which image to deploy on k8s.

## What is the purpose of running 2 EC2 instances?
You need containers to run your applications.

## How to respond to MP’s grader GET and POST?
There is no code for the GET request. You are just hitting the endpoint to get the fields from each of your jobs as listed in the project description. 

## The autogravder test.py is returning with a 502 bad gateway every time
In test.py I was adding http:// before my IP, the solution was to only use IP:PORT as specified.

## ModuleNotFoundError: No module named 'torch'
-> RUN pip --no-cache-dir install torch torchvision in Dockerfile

## How to generate Free Service vs Default namespace?
You have to use generate-name or change the name dynamically.You cannot deploy the pod with the same name

## To delete all pods
`kubectl delete --all all --namespace=free-service`


## TIPS:
AWS EKS/Kubernetes setup:
- Create EC2 (t2.micro) (aka node 0) -> ssh into the EC2 instance and then setup the EKS so that the credentials are managed through that.
- Add rule to allow http traffic (Used port 8080)
- Followed the instructions https://docs.aws.amazon.com/eks/latest/userguide/getting-started-eksctl.html
- Use "Cluster with Linux-only workloads" option and passed ssh public key from EC2 (node 0) which is required if you want to ssh to worker nodes (node 1 & node 2 both are t3.medium)
- Modify classify.py to flush stdout to see the output
- Added ENV to Dockerfile
- Used tag when building docker image (did not use ":latest")




