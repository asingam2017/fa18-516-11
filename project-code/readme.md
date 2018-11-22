# Context

This project has two goals - (1) How to deploy machine learning algorithm to production and 
make it to work as serverless function to get best scalability and (2) Explore OpenFaaS and 
related tools to develop, test and deploy onto public cloud providers such as Azure, AWS and Google Cloud.

The purpose of our OpenFaaS Function is to classify an animal image with predictions up to 3 different animals with probabilities.

* use a deep learning convolutional neural network model in **Keras** with tensorflow for image recognition and classification
* use a serverless function deployed by **OpenFaaS** in the docker image.

Detailed documentation for this project can be reviewed [HERE](https://github.com/cloudmesh-community/fa18-516-11/blob/master/project-report/report.md).

This section describes how to build and deploy a microservice - OpenFaaS function for classifying an animal image. 


## Install Docker Swarm (Single-Node Cluster), Docker and OpenFaaS

* **Prerequisites:** Windows 10 Professional or Enterprise Edition, open the command prompt in Administrator moode
* **Step 1:** Install Docker [Community Edition](https://store.docker.com/editions/community/docker-ce-desktop-windows)
* **Step 2:** Install Git Bash for pulling the latest OpenFaaS artifacts and all the other software from GitHub
* **Step 3:** Run **docker swarm init** to set up the single-node docker swarm cluster
* **Step 4:** Create an account with Docker Hub, if the created docker images to be shared with others through internet
* **Step 5:** Run **docker login** to make sure docker is linked to your account
* **Step 6:** Download latest **faas-cli.exe** from [HERE](https://github.com/openfaas/faas-cli/releases)
* **Step 7:**  Copy the **faas-cli.exe** to *C:\windows* folder to make it available for the command prompt. 
                Or you will need to add the path of the faas-cli.exe into the system environment variables
* **Step 8:** Test the faas-cli using the command - **faas-cli version** 
* **Step 9:** Clone the OpenFaaS artifacts from GitHub using : git clone https://github.com/openfaas/faas
* **Step 10:** Go into the **faas** folder that to checkout the git master repository - cd faas and  git checkout master
* **Step 11:** Run **deploy_stack.sh --no-auth**  to deploy the latest OpenFaaS into our environment
* **Step 12:** Run **docker service ls** to verify whether openfaas has been deployed to our environment

## Trouble Shooting

If there are any issues with the docker and/or OpenFaaS functions, we can reset the environment using the following commands

* **restart docker** - to restart the docker
* **docker stack rm func** - to remove all the functions
* **docker swarm leave --force** - to shutdown the docker cluster
* **docker swarm init** - to initialize docker swarm cluster
* **{open_faas_github_folder}/deploy_stack.sh** - to pull the latest code from openfaas GitHub


## Build and deploy a serverless OpenFaaS function 

### Build Docker Container with OpenFaaS function and all the python dependencies

```
docker build -t docker-img-faas-function .
Note: we will need to be in the OpenFaaS function parent fodler where dockerfile exists
```

## Deploy Docker Container Image with our OpenFaaS Function
```
faas-cli deploy --image docker-img-faas-function --name faas-function
```

### OpenFaaS function can be tested using:

```
curl -X POST -H  \
  --data-binary @data/tiger.png \
  "http://127.0.0.1:8080/function/fass-function" 
```  

### Push Our Docker Container Image with OpenFaaS Function

* **Step 1:** Create a tag for our docker image using: **docker tag {img_name} {your_docker_hub_account_name}/{img_name}**
* **Step 2:** Run **docker push your_docker_hub_account_name}/{img_name}**



