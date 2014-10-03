##How to Install

#Ubuntu Installation
```
sudo apt-get install build-essential libssl-dev libffi-dev python-dev
sudo pip install virtualenv
sudo pip install virtualenvwrapper
sudo apt-get install python-pip
sudo apt-get install python-dev
sudo apt-get install libxml2-dev libxslt1-dev
export WORKON_HOME=~/.virtualenvs
mkdir -p $WORKON_HOME
source /usr/local/bin/virtualenvwrapper.sh
mkvirtualenv agora
pip install -r requirements.txt
```

##Vagrant Installation

###Prerequisites
```
sudo apt-get vagrant
vagrant plugin install vagrant-aws
```

###AWS
```
export AWS_ACCESS_KEY_ID=<ACCESS_KEY>
export AWS_SECRET_ACCESS_KEY=<SECRET_KEY>
export AWS_SSH_KEY_PATH=~/Development/vagrant.pem
export AWS_SUBNET_ID=subnet-7faca71d
vagrant up --provider=aws
```