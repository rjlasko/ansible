# SSH

This Ansible role configures SSH access and keys for the active user.


### General Properties
- `ssh` - the parent object argument for this role
	- `purge_keys` - `default(false)` - removes all key files in `~/.ssh`
	- `key_definitions` - a list of individual key definitions
		- key definition - properties to create an SSH key
			- `primary` - `default(false)` - If false, `name` must be present. When `true`, standard key naming conventions will be applied.
			- `name` - name of non-primary key. If absent, `primary` must be `true`. If present, it will
			- `source` - use a pre-existing key
				- `private` - path to private key file
				- `public` - path to public key file
			- `decrypt` - `default(omit)` - boolean indicating whether the source file needs to be decrypted with Ansible Vault.
			- `type` - The desired SSH key type. `default('ed25519')` when generating a new key. Required when `source` is defined and `primary` is `true`.
			- `replace` - `default(false)` - force replace pre-existing key
			- `comment` - Used as the public key-file's comment field. Defaults to `<user>@<hostname>` if absent.
	- `purge_known_hosts` - `default(false)` - removes `~/.ssh/known_hosts`
	- `purge_authorized_keys` - `default(false)` - removes `~/.ssh/authorized_keys`
	- `authorized_keys` - list of public key strings to add to `~/.ssh/authorized_keys`. Pre-existing keys having the same comment field will be replaced.
	- `authorize_self` - `default(false)` - add user's public key to their `~/.ssh/authorized_keys`
