### Cloud deployment with BentoML

![logo](https://github.com/dimzachar/mlzoomcamp/blob/master/Notes/Images/awsbento.png)

In order to deploy our BentoML service to AWS we push the docker image. Make sure you have an account and install AWS CLI. Instructions can be found [here](https://mlbookcamp.com/article/aws) and the instructions to publish are described [here](https://www.youtube.com/watch?v=aF-TfJXQX-w&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR&index=72).

First, create a repo on Amazon Elastic Container Registry (ECR) with an appropriate name
![registry2](https://github.com/dimzachar/mlzoomcamp_projects/blob/master/00-midterm_project/Images/Elastic-Container-Registry%20(2).png)

![registry](https://github.com/dimzachar/mlzoomcamp_projects/blob/master/00-midterm_project/Images/Elastic-Container-Registry%20.png)

You will find the push commands there to push the docker image
![ECR](https://github.com/dimzachar/mlzoomcamp_projects/blob/master/00-midterm_project/Images/Elastic-Container-push.png)

Then, tag the latest image which you find on your system with

```bash
docker images
```

and push the image.  

Next, go to Elastic Container Service to create a cluster 
![ECS](https://github.com/dimzachar/mlzoomcamp_projects/blob/master/00-midterm_project/Images/Amazon-ECS.png)

Select Networking only and go to next step

![ECS1](https://github.com/dimzachar/mlzoomcamp_projects/blob/master/00-midterm_project/Images/Amazon-ECS%20(1).png)

Then, choose your cluster name, hit create and then view cluster
![ECS2](https://github.com/dimzachar/mlzoomcamp_projects/blob/master/00-midterm_project/Images/Amazon-ECS%20(2).png)
![ECS3](https://github.com/dimzachar/mlzoomcamp_projects/blob/master/00-midterm_project/Images/Amazon-ECS%20(3).png)

Now, you need to create a new task and choose FARGATE
![ECS4](https://github.com/dimzachar/mlzoomcamp_projects/blob/master/00-midterm_project/Images/Amazon-ECS%20(4).png)
![ECS5](https://github.com/dimzachar/mlzoomcamp_projects/blob/master/00-midterm_project/Images/Amazon-ECS%20(5).png)

Enter 
* a task definition name
* task role
* Linux as operating system family
* Task memory (0.5 GB)
* Task CPU (0.25 vCPU)

![ECS6](https://github.com/dimzachar/mlzoomcamp_projects/blob/master/00-midterm_project/Images/Amazon-ECS%20(6).png)

Then, select add container and choose a container name.
On memory limits select 256 Soft limit and 3000 on Port mappings with TCP.
![ECS7](https://github.com/dimzachar/mlzoomcamp_projects/blob/master/00-midterm_project/Images/Amazon-ECS%20(7).png)

For the image you need to have pushed the image and find the URI on your created repo
![imageurl](https://github.com/dimzachar/mlzoomcamp_projects/blob/master/00-midterm_project/Images/Elastic-Container-Registry%20(3).png)

Click add and then create. Go back to clusters,select the created cluster and go to tasks. 

![ECS8](https://github.com/dimzachar/mlzoomcamp_projects/blob/master/00-midterm_project/Images/Amazon-ECS%20(8).png)

Choose run new task and select

* Launch type FARGATE
* Linux as operating system family
* Cluster VPC and Subnets

![ECS9](https://github.com/dimzachar/mlzoomcamp_projects/blob/master/00-midterm_project/Images/Amazon-ECS%20(9).png)

Go to Security groups and add a custom TCP with port 3000 and save

![ECS10](https://github.com/dimzachar/mlzoomcamp_projects/blob/master/00-midterm_project/Images/Amazon-ECS%20(10).png)

Finally, hit run task.

Once the task is running, you will get a public IP for the deployed service like in the video below.

https://user-images.githubusercontent.com/113017737/200716975-7d780f6e-6d6d-4aeb-ba0e-843f34f240de.mp4
