# Ansible Role: Python

Installs any number of Python versions using `pyenv`, which is also used to manage them. `pyenv` is provided as a system installation on MacOS, whereas Linux only supports `/home/$USER/.pyenv` installations. The requested `python` versions are installed under `/home/$USER/.pyenv/versions` for all operating systems.

Also configures `pip`.

## Requirements

- MacOS: Xcode CLI tools & `brew` must be installed
- Linux: `sudo` to `root` to install Python build dependencies

## Role Variables

#### Settable Variables
```yaml
python_versions: # list of exact python versions to install. default([3.9.13])
python_global_versions: # string, space separated list of versions to put into PATH, defaults to the same list as `python_versions`
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
