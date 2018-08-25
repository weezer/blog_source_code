Title: an example of import_tasks and include_tasks of ansible
Date: 04-27-2018
Category: tech
Tags: tech
Slug: ansible_inlcude_tasks_import_tasks 
Authors: Weezer Su
Summary: include_tasks and import_tasks

include is deprecated, include_tasks is dynamic, when only run once name can be a variable
import_tasks is static, so every task only been evaluated once, name cant be a variable

include had static: yes (behaved like import_tasks), and static: no (like include_tasks).

*x.yml*
```
- hosts: 127.0.0.1
  gather_facts: False
  tasks:
    - set_fact: mode=1
    - include_tasks: y.yml
      when: mode == "1"

    - set_fact: mode=1
    - import_tasks: y.yml
      when: mode == "1"
```

*y.yml*
```
- set_fact: mode="2"

- debug:
    msg: >
      Display in only `include_tasks`.
      `include_tasks` does NOT re-evaluate `mode` for every step.
      `import_tasks` DOES re-evaluate condition.
```

*output*
```
TASK [set_fact] *******************************************************
ok: [127.0.0.1]

TASK [include_tasks] **************************************************
included: /root/devops/ansible/y.yml for 127.0.0.1

TASK [set_fact] *******************************************************
ok: [127.0.0.1]

TASK [debug] **********************************************************
ok: [127.0.0.1] => {
    "msg": "Display in only `include_tasks`.
            `include_tasks` does NOT re-evaluate mode for every step.
            `import_tasks` DOES re-evaluate condition\n"
}

TASK [set_fact] *******************************************************
ok: [127.0.0.1]

TASK [set_fact] *******************************************************
ok: [127.0.0.1]

TASK [debug] **********************************************************
skipping: [127.0.0.1]
```

another example


