# Ansible Role: Flexible I/O tester

Installs `fio` to the host.

## Requirements

- Linux: Debian based distribution

## Role Variables

#### Settable Variables

All the following variables are optional.  If none are specified, this role will simply try to install the latest version of `fio`. If `fio` is found in the `PATH`, installation will be skipped if a new version is detected, or if the installed version is different that what is explicitly requested.

```yaml
fio_version: # string denoting the git-tagged version to install
```

## Dependencies

None

## Example Playbook
```yaml
- hosts: servers
  roles:
    - role: fio
      vars:
        fio_version: fio-3.30
```

## License

MIT
