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

## LAB 02

### Run your 1st Container

`docker run -it --name firstContainer alpine /bin/sh`

### Run our application on a Container

 `cd app/`

 `docker-compose up --build`

After you typed the commands above, the container will be up and running and you can start making service calls via browser or using curl:

ADD: `http://localhost:5000/add?a=1&b=5` | Ex. 1 + 5 = 6

SUBTRACT: `http://localhost:5000/subtract?a=1&b=5` | Ex. 1 - 5 = -4

MULTIPLY: `http://localhost:5000/multiply?a=2&b=5` | Ex. 2 * 5 = 10

DIVIDE: `http://localhost:5000/divide?a=10&b=2` | Ex. 10 / 2 = 5
