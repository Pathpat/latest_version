# latest_version

Simple python script that returns the latest version
of moodle from githubapi and manipulate json file 
to return the latest version of a repository.

## Installing python ##

windows users:
Download python from https://www.python.org/downloads/

linux Ubuntu users:
1.Upgrade and update Ubuntu to the latest version
    sudo apt update && sudo apt upgrade

2.Install the required packages
    sudo apt install wget build-essential libncursesw5-dev libssl-dev \
    libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev

3.Download python 3.11
    sudo add-apt-repository ppa:deadsnakes/ppa

4.Install it
    sudo apt install python3.11

Mac users:
Install python via brew
    brew install python


## For the project you will need to install  ##

1.Package requests
    python -m pip install requests

## For run the script in your machine ##

Just in your directory that you git clone this repository:
    python script.py