# Ansible Role: `smart_monitoring_tools`

This Ansible role will do the following:
1. install `smartmontools`, S.M.A.R.T. Monitoring Tools
2. configure a schedule of common device scans
3. mail any alerts to a given email account

## Requirements

- Linux: Debian derivative
- `sendmail`

## Role Variables

#### [Settable Variables](./meta/argument_specs.yml)

## Dependencies

None

## Example Playbook
```yaml
- hosts: servers
  roles:
    - role: smart_monitoring_tools
      smartmontools_email: who@me.com
```

## License

MIT

## References:
https://www.smartmontools.org
https://www.lisenet.com/2014/using-smartctl-smartd-and-hddtemp-on-debian/
https://help.ubuntu.com/community/Smartmontools#Advanced:_Running_as_Smartmontools_as_a_Daemon
https://wiki.archlinux.org/index.php/S.M.A.R.T.


#### DEVICESCAN parameters

Notes on scheduling choices:
- `DEVICESCAN` - scans all connected disk devices
- `-a` - monitors all attributes
- `-d sat` - includes devices connected via "SCSI to ATA Translation"
- `-S on` - enable attribute auto-save
- `-o off` - disable SMART Automatic Offline Testing (in favor of daily short tests)
- `-R 190 -R 194 -R 231` - use raw values (celsius) for Airflow Temp and Temperature for monitoring
- `-W 4,40,45` - track temperature changes (log 4deg changes, log hit 40deg, log & email warning @ 45deg)
- `-m ${ALERT_EMAIL}` - email alerts to that account
- `-M test` - send test email for each device on SMART daemon restart
- `-s (S/../(02|10|18|26)/./03|L/../28/./03)` - short @ 3am (2nd,10th,18th,26th of the month), long @ 3am (28th of the month)
