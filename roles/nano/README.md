# Ansible Role: Nano

Installs `nano` to the host, and facilitates per-user configuration.

## Requirements

- MacOS: `brew` must be installed.
- Linux: none

## Role Variables

#### Settable Variables

All the following variables are optional.  If none are specified, this role will simply try to install `nano`. If `nano` is found in the `PATH`, installation will be skipped.

```yaml
nanorc_settings: # list, see: https://www.nano-editor.org/dist/latest/nanorc.5.html
```

## Dependencies

None

## Example Playbook
```yaml
- hosts: servers
  become: true
  roles:
    - role: nano
      vars:
        nanorc_settings:
          - set smooth
          - set autoindent
          - set tabsize 4
```

## License

MIT
