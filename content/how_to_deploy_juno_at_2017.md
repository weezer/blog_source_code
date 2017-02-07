Title: How to deploy JUNO at 2017.
Date: 2017-02-02 16:20
Category: tech
Tags: openstack, openstack-ansible
Slug: how_to_deploy_juno_at_2017 
Authors: Weezer Su
Summary: Deploy openstack-ansible Juno with AIO-multinode.

```
git clone https://github.com/rcbops-qe/openstack-ansible-ops
cd multi-node-aio
#the better run each task individually rather than just the build.sh
RUN_OSA=false PARTITION_HOST=true OSA_BRANCH=stable/mitaka ./build.sh
#downgrade the kernel of each VMs
cd tools/
KERNEL_VERSION=3.13.0-98 ./downgrade-all-VMs.sh
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
ansible-playbook playbooks/infrastructure/haproxy-install.yml playbooks/setup-everything.yml
#GOOD LUCK
```
