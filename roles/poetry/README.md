# Ansible Role: Poetry

Installs and configures the latest version of `poetry`.

## Requirements

None

## Role Variables

#### Settable Variables
```yaml
poetry_pip_username: # string (optional), username for PyPi repository
poetry_pip_password: # string (optional), password for PyPi repository
poetry_pip_url: # string (optional), URL for PyPi repository
poetry_extra_configs: # list

# optional
poetry_completions_filepath: # filepath to load poetry completions. default: ~/.bashrc
```

## Dependencies

None

## Example Playbook
```yaml
- hosts: servers
  roles:
    - role: poetry
      vars:
        poetry_pip_username: "{{ vault.username }}"
        poetry_pip_password: "{{ vault.password }}"
        poetry_pip_url: https://company.jfrog.io/artifactory/api/pypi/pypi/simple
        poetry_extra_configs:
          - virtualenvs.create false
```

## License

MIT
