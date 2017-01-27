Title:Best practices for KVM 
Date: 2017-01-24 16:23
Category: openstack
Tags: tech, openstack
Slug: best_practices_for_KVM 
Authors: Weezer Su
Summary: KVM tuning
好吧，其实我什么都干不了，摘抄几个链接过来。

1. [IBM Best practices for KVM](https://www.ibm.com/support/knowledgecenter/linuxonibm/liaat/liaatbpkickoff.htm)
2. [OpenStack Local LVM Instance Storage](http://ops.anthonygoddard.com/OpenStack/openstack-local-lvm-instance-storage/)

    ```bash
    images_type=lvm
    libvirt_images_volume_group=nova_local
    ```

3. mitaka开始，可以使用`preallocate_images = space` 来开启file 的aio native。[aio](https://github.com/dianaclarke/openstack-notes/wiki/aio) 

4. 还可以更改`l2-cache-size`, eg. `qemu-system-x86_64 -drive file=disk_image.qcow2,l2-cache-size=4194304,refcount-cache-size=262144`. [qemu img io performance](https://blogs.igalia.com/berto/2015/12/17/improving-disk-io-performance-in-qemu-2-5-with-the-qcow2-l2-cache/). openstack 还没有这个feature， 这里是[blueprint](https://blueprints.launchpad.net/nova/+spec/qcow2-l2-cache-size-configuration)
