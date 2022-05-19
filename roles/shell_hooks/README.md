# Ansible Role: Shell Hooks

Installs a hook system to generically manage login, interactive and non-interactive shell sessions.

## Requirements

- `bash` as target user's shell interface.

## Role Variables

#### Settable Variables
```yaml
shell_hooks_directory: # location to install shell hooks, default ~/.shell_hooks
shell_hooks_reset: # boolean, deletes the ~/.shell_hooks directory when true
```

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
