# Ansible Role: Backup & Restore

Backup of a given file, and if the file already exists, restores from the backup. If that targeted file never existed, a DNE marker will be created to ensure a new file doesn't begin to appear like an original.

## Requirements

- None

## Role Variables

#### Settable Variables
```yaml
br_target: # string (mandatory), the file targeted for backup and restoration
br_suffix: # string (optional), default "BAK"
br_backup: # string (optional), the path of the backup file
```

## Dependencies

None

## Example Playbook
```yaml
- hosts: servers
  roles:
    - role: backup_restore
      vars:
        br_target: /etc/smartd.conf
        br_suffix: ORIG
```

## License

MIT
