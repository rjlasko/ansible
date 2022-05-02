# Ansible Role: pipx

Installs latest version of `pipx`, and configures its repository settings.

## Requirements

- MacOS: Homebrew must be installed

## Role Variables

#### Settable Variables
```yaml
pip_username: # string (optional), username for PyPi repository
pip_password: # string (optional), password for PyPi repository
pip_extra_index_endpoint: # string (optional), URL for PyPi repository
```

Note, if either username or password are provided, then all 3 of the variables above must be provided.

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
