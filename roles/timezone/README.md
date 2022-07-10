# Ansible Role: Timezone

Sets the timezone for the target server.

## Requirements

- Linux

## Role Variables

#### Settable Variables

```yaml
timezone: # string, must be value in TZ database
```

## Dependencies

None

## Example Playbook
```yaml
- hosts: servers
  roles:
    - role: timezone
      vars:
        timezone: America/New_York
```

## License

MIT

## References

[TZ database names](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)
