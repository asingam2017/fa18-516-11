# Context

This project has two goals - (1) How to deploy machine learning algorithm to production and make it to work as serverless function to get best scalability and (2) Explore OpenFaaS and related tools to develop, test and deploy onto public cloud providers such as Azure, AWS and Google Cloud.

Detailed report can be reviewed [HERE](https://github.com/cloudmesh-community/fa18-516-11/blob/master/project-paper/report.md).


## Get FaaS-CLI
```
curl -sSL https://cli.openfaas.com | sudo sh
```

## Build and deploy
```
faas-cli build -f openfaas_functions.yml
faas-cli deploy -f openfaas_functions.yml
```

### OpenFaaS function can be tested using:

```
curl -X POST -H  \
  --data-binary @data/tiger.png \
  "http://127.0.0.1:8080/function/vggnet_predefined_classify" 
```  

```
curl -X POST -H  \
  --data-binary @data/tiger.png \
  "http://127.0.0.1:8080/function/resnet_predefined_classify" 
```  