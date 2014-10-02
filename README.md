##How to Install

#Ubuntu Installation
```
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