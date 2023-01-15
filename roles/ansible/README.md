# Ansible Role: `ansible`

Installs `ansible` to the host.

## Requirements

`system`
- MacOS: `brew` must be installed
- Linux: none

`pipx`: `pipx` must be installed

`pipv`: `python3` & `pip` must be installed

## Role Variables

#### Settable Variables
```yaml
ansible_installation: # required. How to install `ansible`. One of ['system', 'pipv', 'pipx'].
ansible_version: # optional, default(~latest~). version of ansible to install.  Only when `ansible_installation == 'pipv'`
ansible_init_file: # filepath, optional. adds `ansible` executable to shell environment, when `ansible_installation == 'pipv'`
```

## Dependencies

None

## Example Playbook
```yaml
- hosts: servers
  become: true
  roles:
    - role: ansible
      vars:
        ansible_installation: pipv
        ansible_init_file: ~/.bashrc
```

## License

MIT
