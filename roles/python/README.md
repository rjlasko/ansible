# Ansible Role: Python

Installs any number of Python versions using `pyenv`, which is also used to manage them.

## Requirements

- MacOS: Xcode CLI tools & `brew` must be installed
- Linux: `sudo` to `root` to install Python build dependencies

## Role Variables

#### Settable Variables
```yaml
python_reset_pyenv: # boolean, deafult(false), delete preexisting pyenv
python_pyenv_versions: # list of python versions to install, default([2.7.18, 3.9.11])
python_global_versions: # string, space separated list of versions to put into PATH, defaults to the same list as `python_versions_installed`
python_pyenv_init_file: # filepath, default('~/.bashrc'), adds update to PATH with pyenv shims + completions.
python_system_install_dependencies: # boolean, default(true), will install Python build dependencies.  Requires `sudo` privileges.
```

## Dependencies

None

## Example Playbook
```yaml
- hosts: servers
  roles:
    - role: python
      vars:
        python_reset_pyenv: false
        python_pyenv_versions:
          - 2.7.18
          - 3.9.11
        python_global_versions: "3.9.11"
```

## License

MIT

## References

[PyEnv](https://github.com/pyenv/pyenv)
