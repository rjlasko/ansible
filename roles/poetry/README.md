# Ansible Role: Poetry

Installs and configures the latest version of `poetry`.

## Requirements

`system`
  - MacOS: `brew` must be installed
  - Linux: ***unsupported***

`pipx`: `pipx` must be installed

`venv`: `python3` & `pip` must be installed

`poetry`: none

## Role Variables

#### Settable Variables
```yaml
poetry_installation: # required. How to install `pipx`. One of ['system', 'venv', 'pipx', 'poetry', 'none'].
poetry_version: # optional, default(~latest~). version of poetry to install.
poetry_init_file: # filepath, optional. adds `poetry` completions to shell environment. adds `poetry` executable to PATH, when `poetry_installation == 'venv'`

# a user configuration will be created if `poetry_extra_configs` or `poetry_pip_url` is provided
poetry_extra_configs: # list, default([])
poetry_pip_url: # string (optional), URL for PyPi repository
# If poetry_pip_url is provided, then both of the below variables above must be provided.
poetry_pip_username: # string (optional), username for PyPi repository
poetry_pip_password: # string (optional), password for PyPi repository
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
        poetry_init_file: ~/.bashrc
        poetry_pip_username: "{{ vault.username }}"
        poetry_pip_password: "{{ vault.password }}"
        poetry_pip_url: https://company.jfrog.io/artifactory/api/pypi/pypi/simple
        poetry_extra_configs:
          - virtualenvs.create false
```

## License

MIT
