# Ansible Role: Network UPS Tools (aka NUT)

Installs NUT and configuration for server in `standalone` mode.

###### Limitations
The server configuration only supports a single UPS

## Requirements

- Linux

## Role Variables

#### [Settable Variables](./meta/argument_specs.yml)

## Dependencies

None

## Example Playbook
```yaml
- hosts: servers
  roles:
    - role: network_ups_tools
      vars:
        nut:
          mode: standalone
          user: monuser
          email: admin@mysite.com
```

## License

MIT

## References

[Network UPS Tools](https://networkupstools.org)
[Arch Wiki](https://wiki.archlinux.org/index.php/Network_UPS_Tools)
