# Ansible Role: Vim

Installs `vim` to the host, and facilitates per-user configuration.

## Requirements

- MacOS: `brew` is installed.
- Linux: `sudo` privileges

## Role Variables

#### Settable Variables
```yaml
vim_install: # boolean, default(false). installs system package
vim_init_file: # filepath, optional. filepath to add `EDITOR=vim` to shell environment
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
        vim_install: system
        vim_init_file: ~/.bashrc
        vimrc_user_cfg: true
```

## License

MIT
