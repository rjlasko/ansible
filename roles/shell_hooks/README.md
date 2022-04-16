# Ansible Role: Shell Hooks

Installs a hook system to generically manage login, interactive and non-interactive shell sessions.

## Requirements

- `bash` as target user's shell interface.

## Role Variables

- None

## Dependencies

None

## Example Playbook
```yaml
- hosts: servers
  roles:
    - role: shell_hooks
```

## License

MIT
