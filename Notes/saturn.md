> [Back to Index](README.md)


## Setting up the Environment on Saturn Cloud - Tensorflow

![logo](https://github.com/dimzachar/mlzoomcamp/blob/master/Notes/Images/saturn%20tensorflow.png)

### Tutorial for #mlzoomcamp

[Full video](https://www.youtube.com/watch?v=WZCjsyV8hZE&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR&index=76)

[Create ssh keys on github if you don't have](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent?platform=windows)

Step by step [video](https://www.youtube.com/watch?v=8X4u9sca3Io)

Register on [Saturn Cloud](https://saturncloud.io), go to secrets and hit new

![sa](https://github.com/dimzachar/mlzoomcamp/blob/master/Notes/Images/Saturn-Cloud.png)

Add the id_ed25519 and paste your ssh key. Add an empty line after and a dot at the end and hit add.

![sa1](https://github.com/dimzachar/mlzoomcamp/blob/master/Notes/Images/Saturn-Cloud%20(1).png)

Then, go to Resources, select New Resource from a Template and find Tensorflow Python

![sa2](https://github.com/dimzachar/mlzoomcamp/blob/master/Notes/Images/Saturn-Cloud%20(2).png)

Add a name and click create

![sa3](https://github.com/dimzachar/mlzoomcamp/blob/master/Notes/Images/Saturn-Cloud%20(3).png)

Select your newly resource and hit edit

![sa4](https://github.com/dimzachar/mlzoomcamp/blob/master/Notes/Images/Saturn-Cloud%20(4).png)

Find environment, go to Pip, add scipy and select the "This is a requirements.txt" box. Hit save at the bottom.

![sa5](https://github.com/dimzachar/mlzoomcamp/blob/master/Notes/Images/Saturn-Cloud%20(5).png)

Now go back to the resource and select secrets and attach secret file

![sa6](https://github.com/dimzachar/mlzoomcamp/blob/master/Notes/Images/Saturn-Cloud%20(6).png)

Select the key from the dropdown and edit the path as in the photo

![sa7](https://github.com/dimzachar/mlzoomcamp/blob/master/Notes/Images/Saturn-Cloud%20(7).png)

Go back to overview and click Start

![sa8](https://github.com/dimzachar/mlzoomcamp/blob/master/Notes/Images/Saturn-Cloud%20(8).png)

Once it finishes, select jupyter notebook, click new on top right and select terminal

![sa9](https://github.com/dimzachar/mlzoomcamp/blob/master/Notes/Images/examples-examples-tensorflow-.png)

Write on terminal 
ssh -T git@github.com 
and add your passphrase if any. Congrats you can now use git commands like init, commit, add, clone for github

![sa10](https://github.com/dimzachar/mlzoomcamp/blob/master/Notes/Images/terminal_tensorflow.png)
