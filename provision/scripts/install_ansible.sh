#! /bin/bash
IS_ANSIBLE_INSTALLED=$(rpm -qa | grep ansible)
# If the string above is empty, then ansible is not installed.
if [[ -z "${IS_ANSIBLE_INSTALLED// }" ]]
then
    echo Ansible was not found... installing
    #install ansible
    sudo yum -y update
    sudo yum -y install epel-release
    sudo yum -y install ansible
fi



# install python 34
# sudo yum -y install gcc
# sudo yum -y install wget
# sudo yum -y install python34
# sudo wget https://bootstrap.pypa.io/get-pip.py
# sudo python3.4 get-pip.py

# # disable selinux
# sudo vi /etc/sysconfig/selinux
 # probably execute another ansible playbook here?
