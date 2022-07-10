# Ansible Role: Initial Login

Adds a new user login via a separate admin user.  It is presumed that the admin account is the one being used to connect to the target.

## Requirements

- Linux

## Role Variables

#### Settable Variables

```yaml
initial_login:
  user: # string. the name of the user whose password to change
  initial_password: # (Optional) string. the admin user's initial password
  become_password: # (Optional) string. the admin user's password to gain sudo privileges
  new_password: # string. the new password
```

## Dependencies

None

## Example Playbook
```yaml
- hosts: servers
  roles:
    - role: initial_password
      vars:
        initial_login:
          user: admin_user
          initial_password: abcd
          become_password: abcd
          new_password: my_new_pass
```

## License

MIT

## References

[TZ database names](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)
