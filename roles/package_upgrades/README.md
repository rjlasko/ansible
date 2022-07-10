# Ansible Role: Package Upgrades

Upgrades all system packages already installed on the server.

If Debian is installed, the contrib, non-free and backports repos will also be installed.

## Requirements

- Linux: Debian-based distribution

## Role Variables

None

## Dependencies

None

## Example Playbook
```yaml
- hosts: servers
  roles:
    - role: package_upgrades
```

## License

MIT
