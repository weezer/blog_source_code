Title: How to deploy JUNO at 2017.
Date: 2017-02-02 16:20
Modified: 2017-03-16 16:13
Category: tech
Tags: openstack, openstack-ansible
Slug: how_to_deploy_juno_at_2017 
Authors: Weezer Su
Summary: Deploy openstack-ansible Juno with AIO-multinode.

[update](#update)
[update2](#update2)
ETH12 doesn't exist on VMs, bring it up manually or make a #TODO to change the code in the future

add eth12 and problem resolved.
[code](https://github.com/os-cloud/leapfrog-juno-config/blob/master/user_variables.yml#L88 )
[ticket](https://bugs.launchpad.net/openstack-ansible/+bug/1462570)

```
git clone https://github.com/rcbops-qe/openstack-ansible-ops
cd multi-node-aio
#the better run each task individually rather than just the build.sh
RUN_OSA=false PARTITION_HOST=true OSA_BRANCH=stable/mitaka ./build.sh
#downgrade the kernel of each VMs
cd tools/
KERNEL_VERSION=3.13.0-79 ./downgrade-all-VMs.sh
#get the juno code
git clone https://github.com/os-cloud/leapfrog-juno-playbooks.git /opt
mkdir /etc/rpc_deploy
git clone https://github.com/os-cloud/leapfrog-juno-config.git /etc/rpc_deploy
#pre config the deploy host.
./opt/leapfrog-juno-playbooks/scripts/pre-juno-setup.sh
#deploy the juno, HAproxy first
echo "cd /opt/leapfrog-juno-playbooks/rpc_deployment" >> /etc/rpc_deploy/user_variables.yml
echo "lxc_container_backing_store: dir" >> /etc/rpc_deploy/user_variables.yml
ehco "tempest_public_subnet_cidr: 172.29.248.0/22"  >> /etc/rpc_deploy/user_variables.yml
echo "neutron_l2_population: True" >> /etc/rpc_deploy/user_variables.yml
echo "glance_default_store: swift >> /etc/rpc_deploy/user_variables.yml"
#Cange the container_create playbook, bdev to dir delete those lvm related parameters.
ansible-playbook -e @/etc/rpc_deploy/user_variables.yml playbooks/infrastructure/haproxy-install.yml playbooks/setup-everything.yml
#GOOD LUCK
```

<a name="update">Update</a>
Ok for ubuntu  the linux-image-generic is the pure source code, linux-image-extra-generic is for those device drivers, if you dont need to compile your own driver or kernel code, you dont need to care
about the linux-image-header.
We dont need to care about the eth12 because we dont need to use the FLAT network, thats a known issue for openstack neutron, not osad's issue.

What i have changed?
--------------------

1. the enviroment_version of rpc_user_config.yml. [link](https://github.com/weezer/juno-rpc-config/commit/12c5b05e8bd0348f7f6e2004909745e1504c364c)
2. the cinder_volumes_container set to is_metal. [link](https://github.com/weezer/juno-rpc-config/blob/492ae1df34a9a70722e9ffb426fdab6d5b443cfc/rpc_environment.yml#L138)
3. add libxml2=2.9.1+dfsg1-3ubuntu4.8 to rpc_deployment/inventory/group_vars/all.yml. [link](https://github.com/weezer/leapfrog-juno-playbooks/commit/8cbdb8f22f2c4b5a3bf082a9aef85dbdded6488d)
4. add force:yes to repos.yml. [ilink](https://github.com/weezer/leapfrog-juno-playbooks/commit/e914ddeb31ba691627538d79327ca0e73c4e2f87)
5. change the container bdev from "lvm" to "dir". [link](https://github.com/weezer/leapfrog-juno-playbooks/commit/b50862bdb9cfea14c64f56a69a6a126efb895edf)

```
git clone https://github.com/openstack/openstack-ansible-ops
cd multi-node-aio
#the better run each task individually rather than just the build.sh
DEFAULT_KERNEL=3.13.0-79 RUN_OSA=false PARTITION_HOST=true OSA_BRANCH=stable/mitaka ./build.sh
#get the juno code
git clone https://github.com/weezer/leapfrog-juno-playbooks.git /opt
mkdir /etc/rpc_deploy
git clone https://github.com/weezer/leapfrog-juno-config.git /etc/rpc_deploy
#pre config the deploy host.
./opt/leapfrog-juno-playbooks/scripts/pre-juno-setup.sh
#deploy the juno, HAproxy first
echo "cd /opt/leapfrog-juno-playbooks/rpc_deployment" >> /etc/rpc_deploy/user_variables.yml
echo "lxc_container_backing_store: dir" >> /etc/rpc_deploy/user_variables.yml
ehco "tempest_public_subnet_cidr: 172.29.248.0/22"  >> /etc/rpc_deploy/user_variables.yml
echo "neutron_l2_population: True" >> /etc/rpc_deploy/user_variables.yml
echo "glance_default_store: swift >> /etc/rpc_deploy/user_variables.yml"
#Cange the container_create playbook, bdev to dir delete those lvm related parameters.
ansible-playbook -e @/etc/rpc_deploy/user_variables.yml playbooks/infrastructure/haproxy-install.yml playbooks/setup-everything.yml
#GOOD LUCK
```

<a name="update2">Update2</a>

I did a lot of changes for juno configuration. [link](https://github.com/weezer/juno-rpc-config/tree/new_juno). this one will install the cinder on phisical host and no cinder volumn container.
