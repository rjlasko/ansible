# Ansible Role: Vim

Installs `vim` to the host, and facilitates per-user configuration.

## Requirements

- MacOS: `brew` is installed.
- Linux: `sudo` privileges

## Role Variables

#### Settable Variables
```yaml
vim_install: # required, boolean. installs system package
vim_default_editor: # boolean, default(false). Set vim as default shell text editor
vim_init_file: # default('~/.bashrc'), filepath to update when 'vim_default_editor=true'
vimrc_settings: # list, default(['syntax on', 'set noswapfile']). see: http://vimdoc.sourceforge.net/htmldoc/options.html
vimrc_user_cfg: # boolean, default(false). Builds the user's config
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
