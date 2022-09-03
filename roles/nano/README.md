# Ansible Role: Nano

Installs `nano` to the host, and facilitates per-user configuration.

## Requirements

- MacOS: `brew` must be installed.
- Linux: `sudo` privileges

## Role Variables

#### Settable Variables
```yaml
nano_install: # required, boolean. installs system package
nanorc_settings: # list, default(['set autoindent', 'set tabsize 4']). see: https://www.nano-editor.org/dist/latest/nanorc.5.html
nanorc_reset: # boolean, default(true). Rebuilds the config
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
