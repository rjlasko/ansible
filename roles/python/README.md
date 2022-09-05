# Ansible Role: Python

Installs any number of Python versions, optionally using system package managers or `pyenv`, which is also used to manage them. `pyenv` is provided as a system installation on MacOS, whereas Linux only supports `/home/$USER/.pyenv` installations. The requested `python` versions are installed under `/home/$USER/.pyenv/versions` for all operating systems.

Also configures `pip`.

## Requirements

`system`
  - MacOS: `brew` is installed
  - Linux: `sudo` privileges

`pyenv`
  - MacOS: `brew` is installed
  - Linux: `git` is installed, `sudo` if `pyenv_install_build_dependencies == true`

## Role Variables

#### Settable Variables
```yaml
python_installation: # required. Method to perform installation of `python`. Valid values are ['system', 'pyenv', 'none']
python_versions: # list of python versions to install, default([]). Quote versions to prevent float interpolation issues (eg. 3.10 == 3.1). `system` installations only support minor versions (eg. "3.10"), whereas `pyenv` installations require full SEMVER specification (eg. "3.10.6").
python_system_packages: # list, default([]). Additional packages to install via OS package manager

pyenv_global_versions: # string, space separated list of versions to put into PATH, defaults to the same list as `python_versions`
pyenv_install_build_dependencies: # boolean, default(false). will install Python build dependencies. Requires `sudo` privileges.
pyenv_reset: # boolean, default(false), delete preexisting pyenv
pyenv_init_file: # filepath, default('~/.bashrc'), updates PATH with pyenv completions (& executable, for MacOS).
python_init_file: # filepath, default(<pyenv_init_file>), updates PATH with pyenv shims to installed python binaries

# If pip_extra_index_url is provided, then all 3 of the below variables above must be provided.
pip_extra_index_url: # string (optional), URL for PyPi repository
pip_username: # string (optional), username for PyPi repository
pip_password: # string (optional), password for PyPi repository
```

#### Set Facts
```yaml
pyenv_root: # path to pyenv configuration directory
pip_config_installed: # indicates pip config has been installed
```

## Dependencies

None

## Example Playbook
```yaml
- hosts: servers
  roles:
    - role: python
      vars:
        pyenv_reset: false
        python_versions:
          - 2.7.18
          - 3.9.13
        python_global_versions: "3.9.13"
```

## License

MIT

## References

[PyEnv](https://github.com/pyenv/pyenv)
