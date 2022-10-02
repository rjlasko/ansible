# Ansible Role: Neofetch

Installs `neofetch` to the host, and facilitates per-user configuration.

## Requirements

`~/bin`: none

`system`
  - Linux: `sudo` privileges
  - MacOS: `brew` is installed

## Role Variables

#### Settable Variables
```yaml
neofetch_installation: # required. Valid values are 'home', 'system', 'none'
neofetch_reset: # boolean, default(true). Rebuilds the config
neofetch_configs: # list of 2-element lists, default([]). configs to update in neofetch config file
neofetch_image_source: # define image for neofetch to use instead of default
  src: # required, filepath for source image on controller
  dest: # required, filepath for image to be saved on target
  mode: # file permissions string, default('u=r,go-rwx').
neofetch_init_file: # filepath, optional. filepath to add neofetch to PATH for home installation, and place to install neofetch command when `neofetch_init_start=true`
neofetch_init_start: # boolean, default(false). run neofetch on start of user's interactive shell
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
        neofetch_installation: home
        neofetch_configs:
          - ['color_blocks', '"off"']
        neofetch_init_file: ~/.bashrc
        neofetch_init_start: true
```

## License

MIT
