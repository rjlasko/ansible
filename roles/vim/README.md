# Ansible Role: Vim

Installs `vim` to the host, and facilitates per-user configuration.

## Requirements

- MacOS: `brew` must be installed.
- Linux: none

## Role Variables

#### Settable Variables

All the following variables are optional.  If none are specified, this role will simply try to install `vim`. If `vim` is found in the `PATH`, installation will be skipped.

```yaml
nanorc_settings: # list, see: http://vimdoc.sourceforge.net/htmldoc/options.html
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
