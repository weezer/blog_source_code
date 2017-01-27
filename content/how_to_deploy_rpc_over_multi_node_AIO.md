Title: How to deploy RPC with AIO multi node.
Date: 2016-11-02 17:35
Category: tech
Tags: openstack, openstack-ansible
Slug: deploy_RPC_AIO_multinode
Authors: Weezer Su
Summary: Deploy RPC with AIO multi node on baremetal

we’d better backup the /etc/apt/source.lists before deployment, cuz the playbook will change it.
```
git clone https://github.com/rcbops-qe/openstack-ansible-ops
cd multi-node-aio
RUN_OSA=false PARTITION_HOST=true OSA_BRANCH=stable/mitaka ./build.sh
git clone —-recursive https://github.com/rcbops/rpc-openstack/
git checkout tags/r13.0.03 (or any tag u like)
git submodule update —recursive
#config the rpc settings. 
cp -R openstack-ansible/etc/openstack_deploy /etc/openstack_deploy
mv /etc/openstack_deploy/user_secrets.yml /etc/openstack_deploy/user_osa_secrets.yml
cp rpcd/etc/openstack_deploy/user_*_defaults.yml /etc/openstack_deploy
cp rpcd/etc/openstack_deploy/user_rpco_secrets.yml /etc/openstack_deploy
cp rpcd/etc/openstack_deploy/env.d/* /etc/openstack_deploy/env.d
DEPLOY_ELK=no
DEPLOY_HARDENING=no
DEPLOY_TEMPEST=yes
./scripts/deploy.sh
```

check /etc/ansible/roles for roles. this variable been set up at openstack-ansible/scripts/openstack-ansible.rc
