# USERS

This Ansible role adds a list of users to the system and given groups, also
allowing the specification of UID, email, and if they are expected to be a sudoer.

### General properties
- `user_definitions` - an object with child objects for each user (not a list)
	- each child object name is the name of the user it defines
		- `uid` - the integer value for this user's preferred UID
		- `group` - the user's primary group
			- `name` - primary group name
			- `id` - primary GID
		- `groups` - secondary groups
		- `sudoer` - default(false) - is the user a sudoer
		- `email` - email address inserted into `/etc/aliases`
