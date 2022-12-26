# Deploy ML service to AWS Lambda

In order to deploy our service to AWS we push the docker image. Make sure you have an account and install AWS CLI. Instructions can be found [here](https://mlbookcamp.com/article/aws)

First, create a repository on Amazon Elastic Container Registry (ECR) with an appropriate name
![registry2](https://github.com/dimzachar/mlzoomcamp_projects/blob/master/00-midterm_project/Images/Elastic-Container-Registry%20(2).png)

![registry](https://github.com/dimzachar/capstone_mlzoomcamp/blob/master/Extra/Elastic-Container-Registry.png)

You will find the push commands there to tag and push the latest docker image
![ECR](https://github.com/dimzachar/capstone_mlzoomcamp/blob/master/Extra/Elastic-Container-push.png)

which you find on your system with

```bash
docker images
```

Next, we publish to AWS Lambda.

Go to AWS Lambda, create function, select container image and add a name. Then, browse your image and finally hit create function 
![function](https://github.com/dimzachar/capstone_mlzoomcamp/blob/master/Extra/Create-function-Lambda.png)

Go to configuration, change timeout to 30 seconds and increase memory RAM (e.g. 1024)
![settings](https://github.com/dimzachar/capstone_mlzoomcamp/blob/master/Extra/Edit-basic-settings-Lambda.png)

Test the function by changing the event json
![eventjson](https://github.com/dimzachar/capstone_mlzoomcamp/blob/master/Extra/event-json.png)

Expose the lambda function using API Gateway. Go to API Gateway, select REST API and build a new API
![apigate](https://github.com/dimzachar/capstone_mlzoomcamp/blob/master/Extra/API-Gateway.png)

Create a new API, give a name
![apigatecreate](https://github.com/dimzachar/capstone_mlzoomcamp/blob/master/Extra/API-Gateway-Create-API.png)

Create new resource, name it predict
![apiresource](https://github.com/dimzachar/capstone_mlzoomcamp/blob/master/Extra/api_resource.png)

Create new method, select POST and hit click. Choose Lambda function as integration type and on Lambda function give the name of the function you created and hit save 
![post](https://github.com/dimzachar/capstone_mlzoomcamp/blob/master/Extra/post.png)

Hit Test, add a JSON document on request body
```bash
 {"url": "https://URL.jpg" }
```

or other image

![posttest](https://github.com/dimzachar/capstone_mlzoomcamp/blob/master/Extra/post_test.png)
![testjson](https://github.com/dimzachar/capstone_mlzoomcamp/blob/master/Extra/test-json.png)


Hit Deploy on Actions, select New Stage and give a name

![deployapi](https://github.com/dimzachar/capstone_mlzoomcamp/blob/master/Extra/deploy-api.png)

Copy the invoke URL, put it in your /test.py file and run it
![testinvoke](https://github.com/dimzachar/capstone_mlzoomcamp/blob/master/Extra/test_invoke_url.png)

Make sure you remove/delete everything after testing if necessary. 

Video of cloud deployment 


https://user-images.githubusercontent.com/113017737/209078429-1038914d-f64f-40d3-a97e-70033a4266d4.mp4
