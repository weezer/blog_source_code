Title: The right posture to install ansible 
Date: 2017-03-07 11:17
Category: tech
Tags: tech, openstack
Slug: right-posture-to-install-ansible 
Authors: Weezer Su
Summary:The right posture to install ansible 

i'm facing  a werid issue yesterday, i installed ansible by ```apt-get install ansible``` on Trusty, but when I run the ansible playbook, everything just fucked up, so u need the RIGHT POSTURE TO INSTALL THE ANSIBLE.


After pip install -U pip
```
$ pip
/usr/bin/pip: No such file or directory
```
great, pip is fucked up 2
```
$ which pip
/usr/local/bin/pip

$ pip
-su: /usr/bin/pip: No such file or directory

$ type pip
pip is hashed (/usr/bin/pip)
```

and tks god this [guy](http://cheng.logdown.com/tags/pip) helped me.
```
$ hash -r
```

and then rerun the pip installation
```
pip install -U pip setuptools
```

then ansible
```
pip install ansible
```

BOOM~~

