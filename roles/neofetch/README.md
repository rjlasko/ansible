# Ansible Role: Neofetch

Installs `neofetch` to the host, and facilitates per-user configuration.

## Requirements

- MacOS: `brew` must be installed.
- Linux: none

## Role Variables

#### Settable Variables

All the following variables are optional.  If none are specified, this role will simply try to install `git`. If `git` is found in the `PATH`, installation will be skipped.

```yaml
neofetch_install_home_bin: # boolean, installs to ~/bin instead of system package
```

## Dependencies

None

## Example Playbook
```yaml
- hosts: servers
  become: true
  roles:
    - role: neofetch
      vars:
        neofetch_install_home_bin: true
```

## License

MIT
