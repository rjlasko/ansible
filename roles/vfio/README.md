# Ansible Role: VFIO

Configures a virtualization host to support the passthrough of specific hardware devices to guest VMs.

## Requirements

- Linux
- Supported boot managers:
  - Kernelstub (ie. Pop!_OS)
  - Grub (ie. Debian, Ubuntu)

## Role Variables

#### Settable Variables
```yaml
# required parameters
boot_manager:
  cmdline:
    present: # dict, of key/values to be added/changed into current kernel boot parameters
    absent: # list, of keys to be omitted from the current kernel boot parameters

# optional parameters
kernelstub_cfgpath: # location of kernelstub configuration file, default: /etc/kernelstub/configuration
kernelstub_cfg_backup: # backup target for kernelstub_cfgpath, default: /etc/default/kernelstub.configuration.BAK
grub_filepath: # location of grub configuration file, default: /etc/default/grub
```

## Dependencies

None

## Example Playbook
```yaml
- hosts: servers
  roles:
    - role: boot_manager
      vars:
        boot_manager:
          cmdline:
            present:
              amd_iommu: 'on'
              iommu: pt
            absent:
              - quiet
```

## License

MIT

## References

[Kernelstub](https://github.]com/isantop/kernelstub)
