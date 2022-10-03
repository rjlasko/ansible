# Ansible Role: pipx

Installs latest version of `pipx`, and supports python package installations using `pipx`.

Also configures `pip`.

## Requirements

`system`
  - MacOS: `brew` must be installed
  - Linux: ***unsupported***

`venv`
  - All: `python3` & `pip` must be installed

## Role Variables

#### Settable Variables
```yaml
pipx_installation: # required. How to install `pipx`. One of ['venv', 'system', 'none'].
pipx_reset: # boolean, default(false). will uninstall all pipx managed applications.
pipx_init_file: # filepath, optional. adds `pipx` apps to PATH, and executable for venv installation.
pipx_completions_file: # filepath, default(<pipx_init_file>). adds `pipx` completions to PATH.

pip_user_cfg: # boolean, default(false). installs pip user config
pip_extra_index_url: # string (optional), URL for PyPi repository
# If pip_extra_index_url is provided, then both of the below variables above must be provided.
pip_username: # string (optional), username for PyPi repository
pip_password: # string (optional), password for PyPi repository
```

#### Set Facts
```yaml
pipx_executable: # path to pipx executable file or symlink
pip_config_installed: # indicates pip config has been installed
```

## Dependencies

None

## Example Playbook
```yaml
- hosts: servers
  roles:
    - role: pipx
      vars:
        pipx_installation: venv
        pipx_init_file: ~/.bash_profile
        pipx_completions_file: ~/.bashrc
        pip_user_cfg: true
        pip_extra_index_endpoint: company.jfrog.io/artifactory/api/pypi/pypi/simple
        pip_username: "{{ vault.username }}"
        pip_password: "{{ vault.password }}"
```

## License

MIT
