# Ansible Role: pipx

Installs latest version of `pipx`, and supports python package installations using `pipx`.

Also configures `pip`.

## Requirements

- MacOS: `brew` or `pip` must be installed
- Linux: `python` and `pip` must be installed

## Role Variables

#### Settable Variables
```yaml
pipx_installation: # How to install `pipx`. One of ['python', 'venv', 'brew'], default('brew' if MacOS else 'python').
pipx_pip: # string, optional. Enables explicit specification of pip executable to use.
pipx_venv_python: # string, default('python3'). Python interpreter to use to install `pipx` and optional venv. Resolved via PATH, unless absolute filepath is given.
pipx_venv_command: # default('<pipx_python> -m venv --copies'). see: https://docs.ansible.com/ansible/latest/collections/ansible/builtin/pip_module.html#parameter-virtualenv_command
pipx_init_file: # filepath, default('~/.bashrc'), updates PATH with pipx completions & apps (+ executable, for venv installation).

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
        pip_username: "{{ vault.username }}"
        pip_password: "{{ vault.password }}"
        pip_extra_index_endpoint: company.jfrog.io/artifactory/api/pypi/pypi/simple
```

## License

MIT
