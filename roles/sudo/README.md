# Ansible Role: `sudo`

Installs the `sudo` utility, and optionally makes it such that sudoers do not need to enter a password any time that they seek to use the `sudo` command.

A sudoer is defined as a user belonging to the system's default administrator group.

The default administrator group is queried from amongst the following, in order
of precedence.
- `wheel`
- `sudo`

## Requirements

- Linux: run as `root` user

## Role Variables

#### Settable Variables
```yaml
sudoer_nologin: # boolean, default(false). Users in 'sudo' group can `sudo` without password prompt.
```

## Dependencies

None

## Example Playbook
```yaml
- hosts: servers
  become: true
  roles:
    - role: sudo
      vars:
        sudoer_nologin: true
```

## License

MIT
