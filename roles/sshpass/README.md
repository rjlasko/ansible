# Ansible Role: sshpass

Installs `sshpass` for MacOS, which supports prompt-less login by Ansible to SSH targets that do not have a SSH key present.

## Requirements

- MacOS: Homebrew must be installed

## Role Variables

None

## Dependencies

None

## Example Playbook
```yaml
- hosts: servers
  roles:
    - role: sshpass
```

## License

MIT

## References

[Stack Overflow Article](https://stackoverflow.com/questions/32255660/how-to-install-sshpass-on-mac/62623099#62623099)
