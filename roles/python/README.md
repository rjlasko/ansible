# Ansible Role: Python

Installs any number of Python versions using `pyenv`, which is also used to manage them.

## Requirements

- MacOS: Homebrew must be installed

## Role Variables

#### Settable Variables
```yaml
python_reset_pyenv: # boolean, delete preexisting pyenv, default: false
python_pyenv_versions: # list of python versions to install
    # defaults: [2.7.18,3.9.11]
python_global_versions: # list of versions to put into PATH
    # defaults to the same list as `python_versions_installed`
python_pyenv_init_file: # filepath to update PATH with pyenv shims + completions. default: ~/.bashrc
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
