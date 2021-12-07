# LIBVIRT

This Ansible role can be used to:
1. install libvirt on a host, and
2. it can be used to install guest VMs

## General properties
- `libvirt` - the prefix property that host and guest VM properties should be declared under
    - `host` - properties for the host
    - `guests` - a list of guests to install

### Host installation properties
- `default_uri` - the default URI to access guests under
- `bridge` - the name of a network bridge available to be used
- `users` - a list usernames to add as VM admins
- `pools` - a list of file system locations that libvirt can use to store VMs and access ISOs
    - `name` - the name of the pool - `default` is the first location that libvirt looks at
    - `path` - the location of the pool

### Guest installation properties

##### General
- `name` - the name of the vm, as seen by the host
- `create_mode` - mode by which the role will create the VM. Is one of the following values: `skip`, `restore`, `build`
- `backup_dir` - location to backup VM to, or restore VM from
- `check_manual` - default(false) - VM restart waits for manual input to continue
- `check_ssh` - default(true) - VM start waits for SSH response to continue, requires `dns_address`
- `dns_address` - network resolvable address used to verify restart
- `alter_domain` - alters machine's XML definition
    - `cpu_mem` - define CPU topology and affinity
        - `cpus` - list of natural (not native) cpu ids to assign the VM
        - `emulator_cpus` - list of natural (not native) cpu ids to assign the VM's emulator processes
        - `io_cpus` - list of natural (not native) cpu ids to assign the VM's IO processes
        - `memory` - amount of memory to assign to the VM
        - `hugepages` - indication of whether the memory should be pulled from hugepages pool
        - `isolate` - indication of whether the VM's cpus should be isolated from host processes
    - `xpaths` - list of XPath modifications to domain XML
        - (list of definitions)
            - `xpath` - XPath to target XML element(s)
            - `attribute` - attribute name to set
            - `value` - value of attribute or element to set
            - `state` - default(present) add or remove XPath target. Values: `present`, `absent`


##### Parameters specific to `create_mode` = `build`
- `virt_install`
    - `iso` - location of the OS installation ISO file
    - `args` - command line arguments to pass to `virt-install`
    - `preseed` - parameters to be passed into preseed template
        - `template` - path to the preseed (Jinja2 formatted) template to pass to `virt-install`

### Example properties for linux guest
```
libvirt_vm:
  name: linbox
  create_mode: build
  dns_address: linbox.home.lan
  backup_dir: /some/path/somewhere/linbox
  virt_install:
    iso: /iso/os/linux/debian-10.3.0-amd64-netinst.iso
    args:
        - "--os-type=linux"
        - "--os-variant=debian10"
        - "--virt-type=kvm"
        - "--autostart"
        - "--cpu=host-passthrough"
        - "--vcpus=4,sockets=1,cores=2,threads=2"
        - "--memory=8192"
        - "--memorybacking=hugepages=yes"
        - "--network=bridge=br0,model=virtio"
        - "--disk=size=32,format=qcow2,io=threads,bus=virtio,serial=linbox-disk0"
    preseed:
        template: "/resource/libvirt/preseed-debian.cfg.j2"
        hostname: linbox
        domain: home.lan
        username: admin
        userpass: password
        rootpass: password
        partitions:
          - type: linux-swap
            method: swap
            priority: 4096
            size:
              min: 4096
              max: 4096
          - type: ext3
            primary: true
            bootable: true
            method: format
            filesystem: ext3
            mountpoint: /
            priority: 6144
            size:
              min: 6144
              max: 6144
          - type: ext3
            method: format
            filesystem: ext3
            mountpoint: /other
            priority: 1000000000
            size:
              min: 16384
              max: -1
  alter_domain:
    cpu_mem:
      cpus: "{{ range(16, 32) | list }}"
      emulator_cpus: [14]
      io_cpus: [15]
      memory: "32GiB"
      hugepages: true
      isolate: true
    xpaths:
      - xpath: /domain/devices/disk[@device='cdrom']
        state: absent
      - xpath: /domain/features/kvm/hidden
        attribute: state
        value: 'on'
```

### Example properties for windows guest
```
libvirt_vm:
  name: winbox
  create_mode: build
  check_manual: true
  check_ssh: false
  backup_dir: /some/path/somewhere/winbox
  virt_install:
    iso: /iso/os/windows/Win10_1909_English_x64.iso
    args:
        - "--os-type=windows"
        - "--os-variant=win10"
        - "--virt-type=kvm"
        - "--autostart"
        - "--cpu=host-passthrough"
        - "--vcpus=6,sockets=1,cores=3,threads=2"
        - "--memory=24576"
        - "--memorybacking=hugepages=yes"
        - "--network=bridge=br0,model=virtio"
        - "--disk=/iso/os/windows/virtio-win-0.1.171.iso,device=cdrom,bus=sata"
        - "--disk=size=128,format=qcow2,io=threads,bus=virtio,serial=winbox-disk0"
  alter_domain:
    cpu_mem:
      cpus: "{{ range(16, 32) | list }}"
      emulator_cpus: [14]
      io_cpus: [15]
      memory: "32GiB"
      hugepages: true
      isolate: true
    xpaths:
      - xpath: /domain/devices/disk[@device='cdrom']
        state: absent
      - xpath: /domain/features/kvm/hidden
        attribute: state
        value: 'on'
```
