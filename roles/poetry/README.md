# Ansible Role: Poetry

Installs and configures the latest version of `poetry`.

## Requirements

`system`
  - MacOS: `brew` must be installed
  - Linux: ***unsupported***

`pipx`: `pipx` must be installed

`python`: `python3` & `pip` must be installed

`venv`: `python3` & `pip` must be installed

`poetry`: none

## Role Variables

#### Settable Variables
```yaml
poetry_installation: # required. How to install `pipx`. One of ['system', 'python', 'venv', 'pipx', 'poetry', 'none'].
poetry_version: # optional, default(~latest~). version of poetry to install.
poetry_pip: # string, optional. Enables explicit specification of pip executable to use, when `poetry_installation == 'python'`

poetry_init_file: # filepath, default('~/.bashrc'). adds `poetry` executable to PATH, when `poetry_installation in ['python', 'venv']`
poetry_completions_filepath: # filepath, default('~/.bashrc'). where to drop scripts that load poetry completions

poetry_pip_url: # string (optional), URL for PyPi repository
poetry_pip_username: # string (optional), username for PyPi repository
poetry_pip_password: # string (optional), password for PyPi repository
poetry_extra_configs: # list
```

## Dependencies

None

## Example Playbook
```yaml
- hosts: servers
  roles:
    - role: poetry
      vars:
        poetry_installation: venv
        poetry_version: 1.1.15 # XXX: 1.2.0 has a problem with its completions script
        poetry_pip_username: "{{ vault.username }}"
        poetry_pip_password: "{{ vault.password }}"
        poetry_pip_url: https://company.jfrog.io/artifactory/api/pypi/pypi/simple
        poetry_extra_configs:
          - virtualenvs.create false
```

## License

MIT
