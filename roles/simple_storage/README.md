# Ansible Role: `simple_storage`

Performs the following operations, for filesystems that live on a single partition, and for disks not used in pooled configurations.

- Create partitions on given disks
- Install filesystem on partition
- Mount filesystems via  `/etc/fstab`

## Requirements

- Linux

## Role Variables

#### Settable Variables

```yaml
simple_storage: # list
  - disk_id: # string following format of files under /dev/disk/by-id
    rebuild: # boolean, optional, default: false
    partitions: # list
      - mount: # path in filesystem to mount to
        fstype: # type of filesystem
        state: # one of [dismounted, mounted]
        format: # boolean, optional, default: false
```

## Dependencies

None

## Example Playbook
```yaml
- hosts: servers
  roles:
    - role: simple_disk
      vars:
        simple_disks:
          - dev: ata-Samsung_SSD_850_EVO_250GB_ABCDEFGHIJKLMNOPQRSTUVWXYZ
            rebuild: true
            partitions:
              - mount: /mnt/evo850
                fstype: ext4
```

## License

MIT
