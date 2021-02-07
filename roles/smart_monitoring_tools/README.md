# S.M.A.R.T. Monitoring Tools

This Ansible role will do the following:
1. install smartmontools
2. setup a schedule of common device scans
3. mail any alerts to a given email account

This role assumes that the host system supports `sendmail`, and is running systemd, as `systemctl` will be invoked to find the location of its environment file.

## General properties
- `smartmontools_email` - the email account to send alerts to
