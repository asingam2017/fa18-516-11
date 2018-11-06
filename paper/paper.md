# Cloud Foundry - Open Source PaaS Alternative :hand: fa18-516-11
 
| Murali Cheruvu
| mcheruvu@iu.edu
| Indiana University
| hid: fa18-516-11
| github: [:cloud:](https://github.com/cloudmesh-community/fa18-516-11/blob/master/paper/paper.md)
  
---
 
Keywords: Cloud Foundry, Open Source, PaaS
 
---

## Cloud Foundry Overview
Cloud Foundry (CF) is, an open source, Platform as a Service (PaaS) 
available through a variety of private and public cloud distributions, 
which is developed and operated by VMware and then transferred to Pivotal Software, 
a joint venture by EMC, VMware and General Electric. Pivotal Cloud Foundry is 
an alternative paid version with additional commercial features, support and documentation.

As opposed to most of the PaaS oferings in the market, which are
*tied to proprietary implementations*, Cloud Foundry is an open
source sofware with fexibility to allow integrations with exter-
nal systems. Cloud Foundry provides all the PaaS capabilities like
the popular public and private PaaS Providers - built-in scalable
infrastructure, middleware, and various tools for development, de-
ployment and support. To enable infrastructure-agnostic archi-
tecture, Cloud Foundry focused on three main categories: *Clouds,
Frameworks and Services* [@Badola2015].

![Cloud Foundry - Open Source PaaS [@Harris2011]](images/Cloud-Foundry-as-Open-PaaS.jpg?raw=true "Cloud Foundry - Open PaaS"){#fig:foundary}

:o: +@fig:foundary shows that and that and the other. Figures must be
mentioned, also see how you cite them here. Fix your other images


### Category: Clouds

:o: we recommend inverting the argumet. Write what cloudfoundary does and if explanations are needed for what they do do it afterwards or refer to the section in epub that explain them

Public and private clouds have their advantages and disadvantages.
While public clouds provide fexibility and faster deployments, private 
clouds ofer operational efciency and total control. *Hybrid
cloud approach* gives best of both public and private cloud oferings: 
infrastructure scalability, deployment and monitoring tools, data
locality, industry regulations, zero-changes to the existing appli-
cations or develop with cloud-native mindset - API Gateways in
combination of Micro-Services. Cloud Foundry is an open PaaS
with ability to extend and collaborate with other private and public
cloud systems. It can co-exist with other PaaS and IaaS platforms,
in a way, it can be hosted on top of popular cloud environments
like AWS, Azure, Google Cloud and OpenStack.

### Category: Frameworks

Most of the cloud environments are *restricted to fewer frameworks*
and programming languages. Tough there is a good coverage
of runtime environments and programming languages ofered by
most of the public clouds including AWS and Azure, there are still
some restrictions either in the way we will need to use them or in
the pricing and licensing models. Cloud Foundry, at architecture
level, is generic and intended to host any programming language.
It is writen in Ruby and currently supports popular programming
languages like Spring, Java, Ruby and NodeJS.

### Category: Services

Similarly most of the clouds have limited set of support for various
types of data, messaging and other services, restricting companies
anddevelopmentteamsbyforcingthemtousespecifctechnologies.
Cloud Foundry, out of the box, shipped with support to various
services like relational (MySQL, PostgreSQL), NoSQL (MongoDB),
Key-Value pair (Redis) databases and RabbitMQ message queuing
system along with extensibility to allow third-party systems to be
added later.

## Key Components

Cloud Foundry comes with lots of ready-made components to sup-
port all the key aspects of PaaS cloud computing in a scalable
fashion [@Nimalsiri2016]. *Figure 2* is a good representation of the major components
of Cloud Foundry:

![Alt text](images/Cloud-Foundry-arch.png?raw=true "Cloud Foundry Architecture")
*Figure 2: Cloud Foundry Architecture*
[Source: @cialisalto2018]

### Router

Router is responsible for controlling all the external and application
level trafc, and also directing the incoming trafc to appropriate
components. Routerconfgurationallowstohavenumberofrouters
to enable proper load balancing and high availability of the cloud
foundry environment. Each router maintains a dynamic route table
with all details of the deployed applications. Gorouter interacts
with Cloud Controller and Droplet Execution Agent (*DEA*) to fa-
cilitate the updated routing information across the Cloud Foundry
Environment. Router is implemented in Go programming language
that can ofer optimal performance.

### UAA and Login Server

User Account and Authentication (*UAA*) and Login Server compo-
nentsaretheidentitymanagementsysteminCloudFoundry. Cloud
Foundry uses OAuth2 (Open Authorization) standards driven token-
based authentication and authorization to manage user security
tokens.

### Cloud Controller

We can think of Cloud Controller (*CC*) as the brain of Cloud Foundry
Environment and the main responsibility of Cloud Controller is to
manage the applications life cycle - deployment, application meta-
data, staging and running the applications. CC uses *Diego Brain*,
CC-Bridge and Diego Cells to stage and run the applications. CC
redirects the frst requests to the appropriate Droplet Execution
Engine (DEA) available in the load balancing pool. CC user per-
missions are maintained at various levels - Orgs, Spaces and Roles
for greater scalability to the role-based access control. Application
deployment artifacts - code packages, build-packs and droplets are
maintained in Blob Store.

### Execution and Storage

Droplet Execution Engine (*DEA*) is responsible for application de-
ployment and runtime management - selecting appropriate build-
pack, stage the application and ensuring end-to-end life cycle man-
agement of the application instance. Build packs are the scripts
to identify the required framework for applications to run prop-
erly. Droplet is the unit of execution - deployed build pack of the
application along with the application metadata. Wardens are con-
tainers to host the droplets and isolate them in resource-controlled
environments. *BOSH* is used as tool for release management of
complex distributed systems.

### Service Brokers

Most of the applications have aspects like interacting with database,
sending messages using Service-Oriented Architecture (*SOA*) and
interfacing third-party components. Services cannot directly inter-
act with the applications given they run in the containers which are
not persistent. Cloud Foundry uses service brokers in a decoupled
fashion through which application developers can facilitate and use
theservicesinapplications. Cloud Controller uses *NATS* based messaging system.
It uses a light-weight publish-subscribe mechanism to distribute
the queued messages among applications.

### Monitoring and Logging

CC provides various tools for continuous monitoring - *(a)* Health
Manager: Responsible for monitoring health of the application
instances by interacting with DEA and CC, *(b)* Metric Collector:
Gathers various application metrics from the running instances,
and *(c)* Log Aggregator: Streams application logs. Developers and
support teams can access these logs and metrics to monitor, support
and take necessary actions to keep systems up and running.

## Conclusion

Lots of Fortune 500 companies from all over the world - various
industries and government organizations, rely on Cloud Foundry
for all the benefts of fexible open source PaaS oferings. Cloud
Foundry is seting the new standards for cloud computing with
emphasis on scalability and industry best practices by promoting
12-factor application development.

