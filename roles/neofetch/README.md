# Ansible Role: Neofetch

Installs `neofetch` to the host, and facilitates per-user configuration.

## Requirements

- `~/bin`: none
- system
  - Linux: `sudo` privileges
  - MacOS: `brew` is installed

## Role Variables

#### Settable Variables
```yaml
neofetch_installation: # required. Valid values are 'home', 'system', 'none'
neofetch_reset: # boolean, default(true). Rebuilds the config
neofetch_configs: # list of 2-element lists, default([]). configs to update in neofetch config file
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
        neofetch_installation: system
        neofetch_configs:
          - ['color_blocks', '"off"']
```

## License

MIT
