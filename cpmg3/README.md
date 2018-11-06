# 3rd Campus Party MG - 07/11/2018
# Workshop: Introduction to Kubernetes
 
## LAB 01

### Install Docker
- Mac: https://store.docker.com/editions/community/docker-ce-desktop-mac
- Windows: https://store.docker.com/editions/community/docker-ce-desktop-windows
- Linux (Ubuntu): https://docs.docker.com/install/linux/docker-ce/ubuntu/

### Minikube

Minikube makes it easy to run an easy to use, installation of Kubernetes that's great to run locally for development, testing, and learning how Kubernetes works. Minikube runs a single-node Kubernetes cluster inside a VM on your laptop for users looking to try out Kubernetes or develop with it day-to-day. You have the option of using one of several hypervisors, but we'll let Minikube use Virtualbox.

Before you begin installing Minikube, you must install a Hypervisor such as VirtualBox: https://www.virtualbox.org/wiki/Downloads

Install *kubectl*: https://kubernetes.io/docs/tasks/tools/install-kubectl/

Install Minikube: https://github.com/kubernetes/minikube/releases

Setup Minikube: https://kubernetes.io/docs/setup/minikube/

Minikube will create a “minikube” context, and set it to default in kubectl. To switch back to this context later, run this command: `kubectl config use-context minikube`

## LAB 02

### Running your 1st Container

`docker run -it --name firstContainer alpine /bin/sh`

### Running our application on a Container

 `cd app/`

 `docker-compose up --build`

After you typed the commands above, the container will be up and running and you can start making service calls via browser or using curl:

ADD: `http://localhost:5000/add?a=1&b=5` | Ex. 1 + 5 = 6

SUBTRACT: `http://localhost:5000/subtract?a=1&b=5` | Ex. 1 - 5 = -4

MULTIPLY: `http://localhost:5000/multiply?a=2&b=5` | Ex. 2 * 5 = 10

DIVIDE: `http://localhost:5000/divide?a=10&b=2` | Ex. 10 / 2 = 5

## LAB 03

### Deploying a Container into Minikube

Run our app from Docker Hub:
`docker run -d -p 5000:5000 andrealmar/calculator`

We are going to deploy our app on Kubernetes using Minikube. Let's start by running our app inside a container:

`kubectl run my-calculator-app --image=andrealmar/calculator --port=5000`

To ensure our deploy was created just run:

`kubectl get deploy`

Check the status of our pods using: 

`kubectl get pods`

If the status is _RUNNING_ everything should be ok for now. 

Now we have our app running inside a container on Kubernetes via Minikube. We'll need to provide access to the server by creating a service to make a port available. This is called EXPOSE our service to external world. 

`kubectl expose deployment my-calculator-app --type=LoadBalancer`

Let's see if the Service was created:

`kubectl get services`

It will return something like:

```shell
NAME                TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
kubernetes          ClusterIP      10.96.0.1        <none>        443/TCP          6h
my-calculator-app   LoadBalancer   10.103.237.134   <pending>     5000:32737/TCP   26s
```

Note what we did here. We've just **EXPOSED** the port **5000** from OUR container to port **32737** of Kubernetes (Minikube).

Take not of the port Minikube has exposed for you. In my case was `32737`

Check the IP Minikube has assigned for you:

`minikube ip`

In my case, the IP Minikube has assigned for me was:

`192.168.99.100`

Open your browser and type:

`YOUR_MINIKUBE_IP:32737` - which is the port Minikube has exposed for us.

Or if you prefer, just use `curl`:

`curl http://192.168.99.100:32737`

The answer will be:

`Hello #CPMG3 !!!`

## LAB 04

Check how many pods we have running:

`kubectl get pods`

We just have ONE pod running:

```shell
NAME                                 READY     STATUS    RESTARTS   AGE
my-calculator-app-599576dd47-rzblq   1/1       Running   0          20m
```

Let's scale our app:

`kubectl scale deploy my-calculator-app --replicas=5`

```shell
$ kubectl get pods

NAME                                 READY     STATUS    RESTARTS   AGE
my-calculator-app-599576dd47-j2lks   1/1       Running   0          1m
my-calculator-app-599576dd47-nshkv   1/1       Running   0          1m
my-calculator-app-599576dd47-rzblq   1/1       Running   0          22m
my-calculator-app-599576dd47-s2kd9   1/1       Running   0          1m
my-calculator-app-599576dd47-sqdkt   1/1       Running   0          1m
```
When we asked Kubernetes to scale our _my-calculator-app_ deployment, a **ReplicaSet** was created. A ReplicaSet ensures that a specified number of pod replicas are running *at any given time.*

Now, try to delete some pods:

`kubectl delete pods my-calculator-app-599576dd47-j2lks my-calculator-app-599576dd47-nshkv`

 ```shell
$ kubectl get pods

NAME                                 READY     STATUS              RESTARTS   AGE
my-calculator-app-599576dd47-46ctd   0/1       ContainerCreating   0          6s
my-calculator-app-599576dd47-j2lks   1/1       Terminating         0          2m
my-calculator-app-599576dd47-nshkv   1/1       Terminating         0          2m
my-calculator-app-599576dd47-rzblq   1/1       Running             0          23m
my-calculator-app-599576dd47-s2kd9   1/1       Running             0          2m
my-calculator-app-599576dd47-sqdkt   1/1       Running             0          2m
my-calculator-app-599576dd47-tkbvg   0/1       ContainerCreating   0          6s
 ```

 It doesn't matter if you have deleted two or more pods, new pods have been created to keep the infrastructure the way you described when you scaled to 5 replicas! The service continues to keep track of all pods and route traffic to them as soon as they are available.

 Now you can *downscale* our calculator application to one Pod again:

 `kubectl scale deploy my-calculator-app --replicas=1 `

## LAB 05

Creating a Namespace:

`kubectl create ns calculator-stg`

**OR**

`kubectl apply -f namespace.yml`

Deployment of our Calculator app:

`kubectl apply -f deployment.yml`

Exposing our Deployment:

`kubectl apply -f service.yml`

Check your port: 

`kubectl get services`

Access your app:

`YOUR_MINIKUBE_IP:PORT`
