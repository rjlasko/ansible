# Ansible Role: Maven

Installs latest version of Maven, and configures its repository settings.

## Requirements

- MacOS: Homebrew must be installed

## Role Variables

#### Settable Variables
```yaml
maven_username: # string (optional), username for maven repository
maven_password: # string (optional), password for maven repository
maven_mirror_release_url: # string (optional), URL for release mirror
maven_mirror_snapshot_url: # string (optional), URL for snapshot mirror
```

Note, if either username or password are provided, then all 4 of the variables above must be provided.

## Dependencies

None

## Example Playbook
```yaml
- hosts: servers
  roles:
    - role: maven
      vars:
        maven_username: "{{ vault.username }}"
        maven_password: "{{ vault.password }}"
        maven_mirror_release_url: https://repo-a/libs-release
        maven_mirror_snapshot_url: https://repo-a/libs-snapshot
```

## License

MIT
