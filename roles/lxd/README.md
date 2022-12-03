# Ansible Role: `lxd`

Installs the latest version of `lxd`.

## Requirements

- Linux: distributions that support `snap`
	- Tested on Debian, Ubuntu, Pop!_OS

## Role Variables

#### Settable Variables
https://github.com/rjlasko/ansible/blob/master/roles/lxd/meta/argument_specs.yml


```yaml
lxd:
  host: # targets a LXD host installation
    preseed:
      ... # the elements found in an LXD preseed configuration
      ... # see: https://linuxcontainers.org/lxd/docs/master/preseed/
    extra_profiles: # list of profile objects
      ... # see: https://docs.ansible.com/ansible/latest/collections/community/general/lxd_profile_module.html#parameters

  guests: # list of targets for LXD container/virtual-machine installation
    - create_mode: # mandatory, one of ['skip','build']
      name: # the name of the lxc instance
      dns_address: # DNS or IP address of the instance
      force_stop: # boolean, default(false). Used when clearing any preexisting guest of same name
      type: # see: https://docs.ansible.com/ansible/latest/collections/community/general/lxd_container_module.html#parameter-type
      server: # URL of LXC image host, defaults to https://images.linuxcontainers.org
      alias: # as listed when running command `lxc image list images:`
      protocol: # defaults to 'simplestreams', one of ['simplestreams','lxd']
      devices:
        ... # see: https://linuxcontainers.org/lxd/docs/master/instances/#devices-configuration
        ... # see: https://docs.ansible.com/ansible/latest/collections/community/general/lxd_container_module.html#parameter-devices
      profiles: # list of the names of profile names declared on the host
      config:
        ... # see: https://linuxcontainers.org/lxd/docs/master/instances/#key-value-configuration
        ... # see: https://docs.ansible.com/ansible/latest/collections/community/general/lxd_container_module.html#parameter-config

      # note that the following fields are mapped onto the above `config`, after converted from human-intuitive description.  Any preexisting `config` value will be overridden.
      cpu_mem:
         cpus: # list of logical core ids
           # becomes: `config.limits.cpu`
           # ids increment by logical cores, grouped by physical core
           # ie. [P0L0,P0L1,P1L0,P1L1] = [0,1,2,3]
         memory: # human friendly amount, eg 4GiB
           # becomes: `config.limits.memory`
         hugepages: # boolean, source memory from hugepages reservation
           # becomes: `config.limits.memory.hugepages`
         priority: # 1-10, shared CPU scheduling priority
           # becomes: `config.limits.cpu.priority`
      host_idmap: # names of user and group IDs to map from host to guest
        # becomes: `config.raw.idmap`
        both: # only for when user and group ID are same  value
        users: # for just user names
        groups: # for just group names

lxd_async_clear_retries: # integer, default(30). number of times to poll for async container stop+delete completion.
lxd_async_clear_retry_delay: # integer, default(5). number of seconds to wait in between polling for async container stop+delete completion.
lxd_async_start_retries: # integer, default(120). number of times to poll for async container start completion.
lxd_async_start_retry_delay: # integer, default(5). number of seconds to wait in between polling for async container  start completion.
```

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
