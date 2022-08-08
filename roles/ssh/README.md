# Ansible Role: `ssh`

This Ansible role configures SSH access and keys for the active user.

## Requirements

- Linux
- MacOS

## Role Variables

#### Settable Variables

```yaml
ssh:
  purge_keys: # boolean, default(false), removes all key files in `~/.ssh`
  key_definitions: # list of individual definitions used to create or copy keys
    - name: # string, default('id_<type>'), used as filename for private + public keys. A named keydef cannot also be the primary keydef.
      primary: # boolean, default(false). A primary key cannot also be named. Only one primary key is supported.
      type: # string, default('ed25519'), eg. rsa, ecdsa, ed25519, dsa. Required when keydef.source is indicated.
      comment: # string, default(<user>@<hostname>), used as the public key-file's comment field
      source: # optional, indicates a predefined key
        public:
          key: # string, plaintext of public key, omitting type prefix or comment suffix
          # TODO: path: # optional, path to pubkey file
        private:
          path: # required, path to private key file
          decrypt: # boolean, default(true), indicates that provided private key file needs decryption
          # TODO: key: string, plaintext of private key, # TODO: determine how to format this
  purge_known_hosts: # boolean, default(false), removes `~/.ssh/known_hosts`
  known_hosts: # list of strings, fqdn of hosts to seed on target by keyscanning for machine public key
  purge_authorized_keys: # boolean, default(false), removes `~/.ssh/authorized_keys`
  authorize_keys: # list of public key strings to add to ~/.ssh/authorized_keys. Pre-existing keys having the same comment field will be replaced.
  authorize_self: # boolean, default(false), add user's public key to their own ~/.ssh/authorized_keys
```

## Dependencies

None

## Example Playbook
```yaml
```


## License

MIT


# SSH
