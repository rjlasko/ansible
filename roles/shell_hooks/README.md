# Ansible Role: Shell Hooks

Installs a hook system to generically manage login, interactive and non-interactive shell sessions.

## Requirements

- `bash` as target user's shell interface.

## Role Variables

#### Settable Variables
```yaml
shell_hooks_directory: # default('~/.shell_hooks'), location to install shell hooks
shell_hooks_reset: # boolean, default(false), deletes the ~/.shell_hooks directory when true
```

#### Set Facts
```yaml
shell_hooks_login: "{{ shell_hooks_directory }}/login"
shell_hooks_startup: "{{ shell_hooks_directory }}/startup"
shell_hooks_interactive: "{{ shell_hooks_directory }}/interactive"
shell_hooks_resource: "{{ shell_hooks_directory }}/resource"
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
