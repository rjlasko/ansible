# Ansible Role: pipv

Installs a `python` application and other specified package(s) into a dedicated virtual environment, using the python interpreter found in the `PATH`.

## Requirements

`python3` & `pip` are accessible from `PATH`

## Role Variables

#### Settable Variables
```yaml
## `venv` Installation ##
pipv_home: # string, default("~/bin"). Base directory to install pipv applications to.
pipv_python: # filepath, default(<resolved by Ansible via PATH>). Path to Python3 interpreter to use to create venv.
pipv_command: # string, default('<pipv_python> -m venv'). see: https://docs.ansible.com/ansible/latest/collections/ansible/builtin/pip_module.html#parameter-virtualenv_command
pipv_copies: # boolean, default(false). Prefer file copies over symlinks when building the virtual environment.

# XXX: All `package_spec` strings follow pip requirement specifier format.
pipv_name: # string, default(<name of pipv_packages[0]>). Used as the name of pipv app directory.
pipv_packages: # required, string(package_spec) or list(string(package_spec)). All packages to install into pipv application directory
pipv_executables: # string or list(string), default([]). Applications in pipv app directory to symlink into `pipv_app_bin`.
```

#### Set Facts
```yaml
pipv_app_bin: # path to directory containing linked application executables
```

## Dependencies

None

## Example Playbook
```yaml
- hosts: servers
  roles:
    - role: pipv
      vars:
        pipv_packages: pipx
        pipv_executables: register-python-argcomplete
```

## License

MIT
