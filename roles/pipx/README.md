# Ansible Role: pipx

Installs latest version of `pipx`, and supports python package installations using `pipx`.

Also configures `pip`.

## Requirements

`system`
  - MacOS: `brew` must be installed
  - Linux: ***unsupported***

`python`
  - All: `python3` & `pip` must be installed

`venv`
  - All: `python3` & `pip` must be installed

## Role Variables

#### Settable Variables
```yaml
pipx_installation: # required. How to install `pipx`. One of ['python', 'venv', 'system', 'none'].
pipx_pip: # string, optional. Enables explicit specification of pip executable to use, when `pipx_installation == 'python'`
pipx_reset: # boolean, default(false). will uninstall all pipx managed applications.
pipx_init_file: # filepath, default('~/.bashrc'), adds `pipx` executable to PATH, for venv installation.
pipx_interactive_file: # filepath, default(<pipx_init_file>). adds `pipx` completions & apps to PATH.

# If pip_extra_index_url is provided, then all 3 of the below variables above must be provided.
pip_extra_index_url: # string (optional), URL for PyPi repository
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
        pip_username: "{{ vault.username }}"
        pip_password: "{{ vault.password }}"
        pip_extra_index_endpoint: company.jfrog.io/artifactory/api/pypi/pypi/simple
```

## License

MIT
