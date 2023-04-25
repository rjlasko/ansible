# Ansible Role: File Drop
A set operations available to be performed on arrays of file targets. Includes deletion, creation, transfer, and copy of files.

## Requirements

None

## Role Variables

#### [Settable Variables](./meta/argument_specs.yml)

## Dependencies

None

## Example Playbook
```yaml
- hosts: servers
  roles:
    - role: file_drop
      vars:
        empty:
          - ~/scratch
        files:
          - path: ~/workspace
            state: directory
            mode: u=rwx,go-rwx
```

## License

MIT
