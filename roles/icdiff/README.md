# Ansible Role: `icdiff`

Installs `icdiff` to the host, and facilitates per-user configuration.

## Requirements

`system`
  - MacOS: `brew` must be installed
  - Linux: ***unsupported***

`pipx`: `pipx` must be installed

## Role Variables

#### Settable Variables
```yaml
icdiff_installation: # required. How to install `icdiff`. One of ['system', 'pipx'].
icdiff_version: # optional, default(~latest~). version of icdiff to install.  Only when `icdiff_installation == 'pipx'`
```

## Dependencies

None

## Example Playbook
```yaml
- hosts: servers
  become: true
  roles:
    - role: icdiff
      vars:
        icdiff_installation: pipx
```

## Notes
https://github.com/jeffkaufman/icdiff#using-with-git

## License

MIT
