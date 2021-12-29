# LXD

## TODO:
* add support for `qemu` virtual machines
* Virtual machine feature parity with `libvirt` role
* Run, backup, snapshot, restore to/from ZFS
	* --> update ZFS trim & FSTrim roles

## REQUIREMENTS
This role requires `community.general.lxd_container` Ansible module, that is version [4.1.0](https://github.com/ansible-collections/community.general/blob/4.1.0/plugins/modules/cloud/lxd/lxd_container.py#L109) or newer.  This is because v4.1.0 enables the `type` option, which allows the module to specify a virtual machine under QEMU.

Note: The version of `community.general` that comes with Ansible CORE is not recent, and must be [upgraded](https://github.com/ansible-collections/community.general#using-this-collection). Run the following command to upgrade:
```
ansible-galaxy collection install community.general --upgrade
```

See relevant documentation using:
```
ansible-doc community.general.lxd_container
```
