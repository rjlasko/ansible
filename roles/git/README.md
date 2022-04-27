# Ansible Role: Git

Installs Git to the host, facilitates per-user configuration, and supports cloning and pushing of repositories to the target.

## Requirements

- MacOS: `brew` must be installed, if installing `git`.
- Linux: none

## Role Variables

#### Settable Variables

All the following variables are optional.  If none are specified, this role will simply try to install `git`. If `git` is found in the `PATH`, installation will be skipped.

```yaml
git:
  global:
    user.name: # The user's git global username
    user.email: # The user's git global email address
  clones: # list of repos to clone and destinations on target
    - src: # the URL of the source (origin) git repo
      dest: # the target repository folder path
      config:
        user.name: # The local username for this repo
        user.email: # The local email address for this repo
  pushes: # list of repos to create on the target from the host
    - src: # the source folder path on the controller
      dest: # the target repository folder path
      config:
        user.name: # The local username for this repo
        user.email: # The local email address for this repo
  utils_path: # location to install git_utils.sh to
```

## Dependencies

None

## Example Playbook
```yaml
- hosts: servers
  roles:
    - role: shell_hooks
      vars:
        git:
          bin_path: /opt/git/bin
          global:
            user.name: First Last
            user.email: first.last@service.com
          clones:
            - src: ssh://user@host:/path/to/repo
              dest: ~/workspace/repo
              config:
                user.name: nickname
          pushes:
            - src: ~/workspace/another_repo
              dest: ~/workspace/another_repo
          utils_path: ~/.shell_hooks/interactive/99_git_utils.sh
```

## License

MIT
