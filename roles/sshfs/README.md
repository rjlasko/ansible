# Ansible Role: SSH (mounted) FileSystem

Installs `sshfs` for MacOS.  This is made possible by the combination of "macFUSE" and "SSHFS for macFUSE".

## Requirements

- MacOS: Homebrew must be installed

## Role Variables

None

## Dependencies

None

## Example Playbook
```yaml
- hosts: servers
  roles:
    - role: sshfs
```

## License

MIT

## References

[macFUSE](https://osxfuse.github.io/)
