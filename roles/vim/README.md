# Ansible Role: Vim

Installs `vim` to the host, and facilitates per-user configuration.

## Requirements

- MacOS: `brew` is installed.
- Linux: `sudo` privileges

## Role Variables

#### Settable Variables
```yaml
vim_install: # required, boolean. installs system package
vimrc_settings: # list, default(['syntax on', 'set noswapfile']). see: http://vimdoc.sourceforge.net/htmldoc/options.html
vimrc_reset: # boolean, default(true). Rebuilds the config
```

## Dependencies

None

## Example Playbook
```yaml
- hosts: servers
  become: true
  roles:
    - role: vim
      vars:
        vimrc_settings:
          - syntax on
          - set noswapfile
```

## License

MIT
