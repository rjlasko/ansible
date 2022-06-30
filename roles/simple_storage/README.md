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
simple_storage:
  - disk_id: ata-Samsung_SSD_850_EVO_250GB_S21NNXBGA26614A
    rebuild: true
    partitions:
      - mount: /mnt/myNewFilesystem
        fstype: ext4
        state: mounted # one of [dismounted, mounted]
        format: true
      # TODO - another
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
          - dev: ata-Samsung_SSD_850_EVO_250GB_S21NNXBGA26614A
            # rebuild: true
            partitions:
              - mount: "{{ managed_folders.virt.path }}"
                fstype: ext4
```

## License

MIT
