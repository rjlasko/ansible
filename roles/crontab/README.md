# Ansible Role: `crontab`

Configures the user's `crontab`.

## Requirements

- MacOS: none
- Linux: none

## Role Variables

#### Settable Variables

```yaml
crontab:
  reset: # boolean, default(false). Clears preexisting crontab
  file: # filepath, optional. Replaces the preexisting crontab with its contents
  entries: # list, optional. Cron jobs and environment variables to add to the crontab
    - name: # Required. Description of a crontab entry or, if env is set, the name of environment variable.
      job: # Required. The command to execute or, if env is set, the value of environment variable. The command should not contain line breaks.
      env: # Optional. Manages a crontab’s environment variable. New variables are added on top of crontab. `name` and `value` parameters are the name and the value of environment variable.
      # Either of the following values must be specified, but not both.
      special_time: # Special time specification nickname. One of: [annually, daily, hourly, monthly, reboot, weekly, yearly]
      crontime: # Array of 5 values following standard cron specification.
```

## Dependencies

None

## Example Playbook
```yaml
- hosts: servers
  roles:
    - role: crontab
      vars:
        crontab:
          reset: true
          entries:
            - name: my job
              job: echo "hello world"
              crontime: ['10','4','*','*','*']
```

## License

MIT
