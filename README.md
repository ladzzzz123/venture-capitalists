Venture-Capitalists
=========
The venture capitalists repository.
Python: 2.7.6
Django: 1.6

Local Development Environment
----------
> Requirements: Vagrant and Virtual Box

> It will be assumed that you are familiar with vagrant.

> ####Local Mysql port: 5433

> ####Local http port: 3001

> ####Mysql username: root

> ####Mysql password: root

> ####Existing database: django_app_default
- Before anything, navigate to the vagrant VM, go to the /vagrant folder, then run
```
pip install -r requirements.txt
```

###Notes:
>* If you have an issue with mysql not connecting, you may need to restart mysql by running 'sudo service mysql restart'
>* Be sure to delete the .git folder after cloning this repo if you intend to use it for a completely unrelated project.
>* Because of the nature of vagrant, you will need to run the Django server from your Vagrant VM on port 0.0.0.0 to be able to acces it from your local machine with the following script.
```
python manage.py runserver 0.0.0.0:8000
```
>* South is being used for database migrations. See http://south.readthedocs.org/en/latest/tutorial/part1.html if unfamiliar. DO NOT MAKE ANY CHANGES TO ANY MODELS UNTIL YOU UNDERSTAND HOW SOUTH WORKS.
>* Be sure to take note of the available fixtures and install them.

###Notes for elastic beanstalk users:
>* Install Elastic Beanstalk command line tools. If using a mac, you can use homebrew and use the following:
```
brew install aws-elasticbeanstalk
```
>* Before you can push to Elastic Beanstalk for the first time, you will need to navigate to your git repo on your local machine then run the following
```
eb init
```
>*AFTER YOU DO THIS, MAKE SURE .elasticbeanstalk/ and .ebextensions/ ARE NOT in .gitignore.
>* It is recommended that after you run 'eb init', you update the path to your AWS credential file as found in /.elasticbeanstalk/config to /usr/local/AWS/.elasticbeanstalk/ENVIRONMENTNAME_credentials being sure to move the original file to the new path. You will likely have to create that path. This will prevent collisions when you have multiple projects using Elastic Beanstalk on one machine.
