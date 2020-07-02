# LIBVIRT

This Ansible role can be used to:
1. install libvirt on a host, and
2. it can be used to install guest VMs

### Guest installation properties

##### General
- `name` - the name of the vm, as seen by the host
- `create_mode` - mode by which the role will create the VM. Is one of the following values: `skip`, `restore`, `build`
- `backup_dir` - location to backup VM to, or restore VM from
- `check_manual` - default(false) - VM restart waits for manual input to continue
- `check_ssh` - default(true) - VM start waits for SSH response to continue, requires `dns_address`
- `dns_address` - network resolvable address used to verify restart
- `alter_domain` - alters machine's XML definition
    - `iothread`
        - `count` - number of iothreads to pin
        - `physical_core_pool` - list of which host cpu cores to pin iothreads to
        - `logical_set_size` - how many logical cores per iothread
    - `vcpupin`
        - `count` - number of vcpus to pin
        - `physical_core_pool` - list of which host cpu cores to pin vcpus to
        - `logical_set_size` - default(1) - how many logical cores per vcpu
    - `emulator`
        - `physical_core_pool` - list of which host cpu cores to pin emulator process to
        - `logical_set_size` - default(1) - how many logical cores used by emulator process

##### Parameters specific to `create_mode` = `build`
- `iso` - location of the OS installation ISO file
- `virt_install_args` - command line arguments to pass to `virt-install`
- `preseed` - parameters to be passed into preseed template
    - `template` - path to the preseed (Jinja2 formatted) template to pass to `virt-install`

### Example properties for linux guest
```
libvirt_vm:
  name: linbox
  create_mode: build
  dns_address: linbox.home.lan
  backup_dir: /some/path/somewhere/linbox
  iso: /iso/os/linux/debian-10.3.0-amd64-netinst.iso
  virt_install_args:
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
    iothread:
      count: 2
      physical_core_pool: [1]
      logical_set_size: 2
    vcpupin:
      count: 4
      physical_core_pool: [2,3]
      logical_set_size: 1
    emulator:
      physical_core_pool: [1]
      logical_set_size: 2
```

### Example properties for windows guest
```
libvirt_vm:
  name: winbox
  create_mode: build
  check_manual: true
  check_ssh: false
  backup_dir: /some/path/somewhere/winbox
  iso: /iso/os/windows/Win10_1909_English_x64.iso
  virt_install_args:
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
    vcpupin:
      count: 6
      cpu_affinity:
        physical_pool: [1,2,3]
        logical_size: 1
    iothreads:
      count: 2
      cpu_affinity:
        physical_pool: [0]
        logical_size: 2
    emulatorpin:
      cpu_affinity:
        physical_pool: [0]
        logical_size: 2
```
