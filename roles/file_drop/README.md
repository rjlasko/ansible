# Ansible Role: File Drop
A set operations available to be performed on arrays of file targets. Includes deletion, creation, transfer, and copy of files.

## Requirements

None

## Role Variables

#### Settable Variables
```yaml
file_drop:
  empty: # list of directory paths, default([]). Directories in this list will be emptied of all files, yet remain present.
  files: # default([]). Invokes the `ansible.builtin.file` module on each item in the list.
    - path: # required
      state: # required
      src: # optional
      force: # optional
      owner: # optional
      group: # optional
      mode: # default('u=r,g-rwx,o-rwx')
  templates: # default([]). Invokes the `ansible.builtin.template` module on each item in the list.
    - src: # required
      dest: # required
      owner: # optional
      group: # optional
      force: # optional
      mode: # default('u=r,g-rwx,o-rwx')
  copies: # default([]). Invokes the `ansible.builtin.copy` module on each item in the list.
    - remote_src: # optional
      src: # required
      dest: # required
      owner: # optional
      group: # optional
      force: # optional
      mode: # default('u=r,g-rwx,o-rwx')
```

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
