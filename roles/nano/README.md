# Ansible Role: Nano

Installs `nano` to the host, and facilitates per-user configuration.

## Requirements

- MacOS: `brew` is installed.
- Linux: `sudo` privileges

## Role Variables

#### Settable Variables
```yaml
nano_install: # required, boolean. installs system package
nano_default_editor: # boolean, default(false). Set nano as default shell text editor
nano_init_file: # default('~/.bashrc'), filepath to update when 'nano_default_editor=true'
nanorc_settings: # list, default(['set autoindent', 'set tabsize 4']). see: https://www.nano-editor.org/dist/latest/nanorc.5.html
nanorc_user_cfg: # boolean, default(false). Builds the user's config
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
        nano_install: true
        nanorc_user_cfg: true
        nanorc_settings:
          - set smooth
          - set autoindent
          - set tabsize 4
```

## License

MIT
