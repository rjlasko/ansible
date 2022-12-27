# Ansible Role: `simple_storage`

Performs the following operations, for filesystems that live on a single partition on a single disk.

- Create partitions on given disks
- Install filesystem on partition

Single-disk+partition filesystems as well as labeled filesystems are mounted to the host and persisted via `/etc/fstab`.

## Requirements

- Linux
- Filesystems identified by label must be built independent of this role

## Role Variables

#### [Settable Variables](./meta/argument_specs.yml)

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

          - label: buttah
            mount: /mnt/buttah
            fstype: btrfs
            opts: autodefrag
            state: mounted
```

## License

MIT
