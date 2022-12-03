# Ansible Role: `lxd`

Installs the latest version of `lxd`.

## Requirements

- Linux: distributions that support `snap`
	- Tested on Debian, Ubuntu, Pop!_OS

## Role Variables

#### Settable Variables
https://github.com/rjlasko/ansible/blob/master/roles/lxd/meta/argument_specs.yml

[link1](https://github.com/rjlasko/ansible/blob/master/roles/lxd/meta/argument_specs.yml)

[link2](./meta/argument_specs.yml)

Note: for any pre-existing `lxd.host.preseed.storage_pools` declared, having `driver == 'zfs'`, the entire dataset will be destroyed and recreated in the parent zpool.

Note: for any LXC instance, when `create_mode == 'build'`, any pre-existing instance (vm or container) will be deleted to make way for the new one.

## Dependencies
Ansible collection `community.general` >= 4.1.0

- This role requires `community.general.lxd_container` Ansible module, that is version [4.1.0](https://github.com/ansible-collections/community.general/blob/4.1.0/plugins/modules/cloud/lxd/lxd_container.py#L109) or newer.  This is because v4.1.0 enables the `type` option, which allows the module to specify a virtual machine under QEMU.
- Note: The version of `community.general` that comes with Ansible CORE may not be recent, and must be [upgraded](https://github.com/ansible-collections/community.general#using-this-collection). Run the following command to upgrade:
```
ansible-galaxy collection install community.general --upgrade
```
- See relevant documentation using:
```
ansible-doc community.general.lxd_container
```

## Example Playbook
Host example
```yaml
- hosts: servers
  roles:
    - role: lxd
      vars:
        lxd:
          host:
            preseed:
              networks: []
              storage_pools:
                - name: default
                  description: "default storage pool (zfs)"
                  driver: zfs
                  config:
                    source: tank/lxc
              profiles:
                - name: default
                  description: "default profile"
                  config: {}
                  devices:
                    root:
                      path: /
                      pool: default
                      type: disk
                    eth0:
                      name: eth0
                      nictype: bridged
                      parent: br0
                      type: nic
            extra_profiles:
              - name: docker_support
                description: basic support for docker
                config:
                  security.nesting: "true"
```

Instance example
```yaml
- hosts: lxd_containers
  roles:
    - role: lxd
      vars:
        lxd:
          guests:
            - create_mode: build
              name: mylxc
              dns_address: mylxc.home.lan
              alias: ubuntu/focal/cloud/amd64
              devices:
                eth0:
                  name: eth0
                  nictype: bridged
                  parent: br0
                  type: nic
                  hwaddr: F1-09-CE-07-C0-70
              profiles:
                - default
                - docker_support
              config:
                boot.autostart: "true"
              host_idmap:
                both:
                  - root
```

## License

MIT

## TODO:
* Enhance support for `qemu` virtual machines
* Virtual machine feature parity with `libvirt` role
* Run, backup, snapshot, restore to/from ZFS
