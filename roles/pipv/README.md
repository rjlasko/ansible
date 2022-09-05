# Ansible Role: pipv

Installs `python` package(s) via `pip` into a dedicated virtual environment.

## Requirements

`python3` & `pip`

## Role Variables

#### Settable Variables
```yaml
pipv_package: # required, the name of the python package to install
pipv_package_version: # optional, the package version
pipv_executables: # string or list[string], default(<pipv_package>). Used to symlink specific executables into `pipv_bin_path`.
pipv_copies: # boolean, default(false). Prefer file copies over symlinks when building the virtual environment.

pipv_python: # string, default('python3'). Python interpreter to use to create venv. Resolved via PATH, unless absolute filepath is given.
pipv_command: # default('<pipx_python> -m venv --copies'). see: https://docs.ansible.com/ansible/latest/collections/ansible/builtin/pip_module.html#parameter-virtualenv_command
```

#### Set Facts
```yaml
pipv_bin_path: # path to directory containing installed executables
```

## Dependencies

None

## Example Playbook
```yaml
- hosts: servers
  roles:
    - role: pipv
      vars:
        pipv_package: pipx
        pipv_copies: true
        pipv_executables:
          - pipx
          - register-python-argcomplete
```

## License

MIT
