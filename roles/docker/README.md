# Ansible Role: Docker

Installs the latest version of `docker` & `docker-compose`.

## Requirements

- Linux: None
- MacOS: Homebrew must be installed

## Role Variables

#### Settable Variables:
```
# (linux only) usernames to be added to the `docker` group
docker_linux_group_users:
  - user1
  - user2
```

## Dependencies

None.

## Example Playbook
```
- hosts: servers
  roles:
    - role: docker
      vars:
        docker_linux_group_users:
          - orca
          - humpback
```

## License

MIT
