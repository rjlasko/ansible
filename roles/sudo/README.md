# SUDO

This Ansible role makes it such that sudoers do not need to enter in a password
any time that they seek to use the `sudo` command.

A sudoer is defined as a user belonging to the system's default administrator
group.

The default administrator group is queried from amongst the following, in order
of precedence.
- `wheel`
- `sudo`
