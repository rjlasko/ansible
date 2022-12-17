# Ansible Role: `libvirt`

Installs `libvirt` and associated libraries to build and run VMs.

This Ansible role can be used to:
- install libvirt on a host, and
- install guest VMs

## Requirements

- Linux: distributions that support `apt`
  - Tested on Debian, Ubuntu, Pop!_OS

## Role Variables

#### [Settable Variables](./meta/argument_specs.yml)

### Example properties for linux guest
```yaml
libvirt_guests:
  - name: linbox
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
```yaml
libvirt:
  guests:
    - name: winbox
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
