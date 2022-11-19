> [Back to Index](README.md)


## Setting up the Environment on Saturn Cloud - Tensorflow

### Tutorial for #mlzoomcamp

[Full video](https://www.youtube.com/watch?v=WZCjsyV8hZE&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR&index=76)

[Create ssh keys on github if you don't have](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent?platform=windows)

Step by step [video](https://www.youtube.com/watch?v=8X4u9sca3Io)

Register on [Saturn Cloud](https://saturncloud.io), go to secrets and hit new

![ECS10](https://github.com/dimzachar/mlzoomcamp_projects/blob/master/00-midterm_project/Images/Amazon-ECS%20(10).png)

Add the id_ed25519 and paste your ssh key. Add an empty line after and a dot at the end and hit add.

![ECS10](https://github.com/dimzachar/mlzoomcamp_projects/blob/master/00-midterm_project/Images/Amazon-ECS%20(10).png)

Then, go to Resources, select New Resource from a Template and find Tensorflow Python

![ECS10](https://github.com/dimzachar/mlzoomcamp_projects/blob/master/00-midterm_project/Images/Amazon-ECS%20(10).png)

Add a name and click create

![ECS10](https://github.com/dimzachar/mlzoomcamp_projects/blob/master/00-midterm_project/Images/Amazon-ECS%20(10).png)

Select your newly resource and hit edit

![ECS10](https://github.com/dimzachar/mlzoomcamp_projects/blob/master/00-midterm_project/Images/Amazon-ECS%20(10).png)

Find environment, go to Pip, add scipy and select the "This is a requirements.txt" box. Hit save at the bottom.

![ECS10](https://github.com/dimzachar/mlzoomcamp_projects/blob/master/00-midterm_project/Images/Amazon-ECS%20(10).png)

Now go back to the resource and select secrets and attach secret file

![ECS10](https://github.com/dimzachar/mlzoomcamp_projects/blob/master/00-midterm_project/Images/Amazon-ECS%20(10).png)

Select the key from the dropdown and edit the path as in the photo

![ECS10](https://github.com/dimzachar/mlzoomcamp_projects/blob/master/00-midterm_project/Images/Amazon-ECS%20(10).png)

Go back to overview and click Start

![ECS10](https://github.com/dimzachar/mlzoomcamp_projects/blob/master/00-midterm_project/Images/Amazon-ECS%20(10).png)

Once it finishes, select jupyter notebook, click new on top right and select terminal

![ECS10](https://github.com/dimzachar/mlzoomcamp_projects/blob/master/00-midterm_project/Images/Amazon-ECS%20(10).png)

Write on terminal 
ssh -T git@github.com 
and add your passphrase if any. Congrats you can now use git commands like init, commit, add, clone for github

![ECS10](https://github.com/dimzachar/mlzoomcamp_projects/blob/master/00-midterm_project/Images/Amazon-ECS%20(10).png)
