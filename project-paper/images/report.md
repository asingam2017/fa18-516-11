 # Explore OpenFaaS on AWS and Azure AKS :hand: fa18-516-11

| Murali Cheruvu
| mcheruvu@iu.edu
| Indiana University
| hid: fa18-516-11
| github: [:cloud:](https://github.com/cloudmesh-community/fa18-516-11/blob/master/project-paper/report.md)
| code: [:cloud:](https://github.com/cloudmesh-community/fa18-516-11/blob/master/project-code/report.md)

---

Keywords: OpenFaaS, Serverless, Micro-Services, Function-as-service

---

## Abstract

Explore creating micro-services using OpenFaaS that makes serverless functions simple for containers like Docker and Kubernetes. Integrate OpenFaaS serverless functions into public cloud offerings such as, AWS and Azure, to make it even better.

## Introduction

Goals of this project is to learn how to create cloud-native micro-services using server-less concepts for better scalability and cheaper to maintain. Function-as-service (FaaS) methodology allows to decouple each functionality from the rest of the application, for better support, isolated deployment and scalability at each function level.  

## Requirements

High level requirements include: setting up OpenFaaS locally within the development environment in Windows and also create deployable aspects: containerized OpenFaaS to be able to deploy to public cloud offerings including AWS, Azure and Google Cloud. Create python based project exploring high level concepts of serverless/micro-services for web. Explore container features in the process. 

* Development Environment: Windows 10 Enterprise
* Install Docker Community Edition and Docker Swarm with single-node cluster
* Setup developer account with Docker Hub for publishing Docker Images on the internet
* Install OpenFaaS CLI - command line interface for OpenFaaS
* Deploy OpenFaaS into the development environment to make it ready to use
* Install Python and related libraries to make it ready for the actual project for machine learning algorithms to run and also write OpenFaaS functions in python.

## Design 

Part of the design, let us introduce some of the key concepts that are needed for this project.

### Micro-Services

Micro-Services is a new paradigm in the software architecture to break down complex monolithic applications into more manageable and decoupled components that can be created and supported in silos. Loosely coupled components offer scalability and also we can use programming-of-choice based on the nature and complexity of the component, anywhere from advanced object-Oriented Programming (OOP) languages like Java, C#.net to modern functional-programming (FP) languages like Scala or Python. Deploying micro-services can be as flexible as deploying each individual functionality as a separate micro-service to grouping related micro-services into one deployment package. Micro-Services can be implemented as simple REST-based API methodology. 

### API Gateways

Micro-Services offer flexibility and scalability but they bring complexity into the deployment and support. Too many micro-services can create confusion in discovering them and also, client applications may have to make multiple micro-service calls, hence create more network traffic even to populate a single webpage. As an example, Amazon has more than 30 micro-services to display a typical product search result webpage. To reduce the network round-trips, it is advised to create a gateway - API gateway, so that clients make unified calls to the gateway and all the related micro-services to fulfill a request will be made within the server and the results of these micro-services are bundled into one result, hence reduce the number of calls to make.

## Architecture

## Dataset

## Implementation

## Benchmark

## Conclusion

## Acknowledgement

The author would like to thank Dr. Gregor von Laszewski and the Teaching Assistants for their support and valuable suggestions. Author would also like to thank OpenFaas and the community of OpenFaaS for great collaboration and providing invaluable documentation and sample projects. 
