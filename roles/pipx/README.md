# Ansible Role: pipx

Installs latest version of `pipx`, and
Installs `python` package(s) via `pipx`.

Also configures `pip`.

## Requirements

`system`
  - MacOS: `brew` must be installed
  - Linux: ***unsupported***

`pipv`
  - All: `python3` & `pip` are accessible from `PATH`

## Role Variables

#### Settable Variables
```yaml
## Credential Installation ##
pip_user_cfg: # boolean, default(false). installs pip user config
pip_extra_index_url: # string (optional), URL for PyPi repository
# If pip_extra_index_url is provided, then both of the below variables above must be provided.
pip_username: # string (optional), username for PyPi repository
pip_password: # string (optional), password for PyPi repository

## pipx Installation ##
pipx_installation: # required. How to install `pipx`. One of ['pipv', 'system', 'none'].
pipx_reset: # boolean, default(false). will uninstall all pipx managed applications.
pipx_init_file: # filepath, optional. adds `pipx` apps to PATH, and executable for pipv installation.
pipx_completions_file: # filepath, default(<pipx_init_file>). adds `pipx` completions to PATH.

## Package Installation ##
pipx_packages: # required, string(package_spec) or list(string(package_spec)). The first item in the list is pipx application, and all other packages are injected into the (first) application directory.

## new package spec ##
pipx_app:
  name: package_spec1==1.2.3 # required. Application to install. Follows pip requirement specifier format.
  inject_packages: # optional, list(String). Additional pip packages to add to application installation. Follows pip requirement specifier format.
      - package_spec2>=1.0.0
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
        pipx_installation: pipv
        pipx_init_file: ~/.bash_profile
        pipx_completions_file: ~/.bashrc
        pip_user_cfg: true
        pip_extra_index_endpoint: company.jfrog.io/artifactory/api/pypi/pypi/simple
        pip_username: "{{ vault.username }}"
        pip_password: "{{ vault.password }}"
```

## License

MIT
