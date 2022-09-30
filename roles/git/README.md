# Ansible Role: Git

Installs `git` to the host, facilitates per-user configuration, and supports cloning and seeding of repositories to the target.

## Requirements

- MacOS: `brew` must be installed, if installing `git`.
- Linux: none

## Role Variables

#### Settable Variables

All the following variables are optional.  If none are specified, this role will simply try to install `git`. If `git` is found in the `PATH`, installation will be skipped.

```yaml
git_install: # boolean, default(false). Installs system package
git_global_config: # default({}). object declaring user's global configuration key-value pairs
git_clones: # default([]). list of repositories to clone
  - src: # required. URL of repository to clone
    dest: # required. location repository will be cloned to
    config: # default({}). object declaring repository's local configuration key-value pairs
git_seeds: # default([]). list of repositories on host to clone to target
  - src: # required. location of repository on host to clone from
    dest: # required. location repository will be cloned to
    config: # default({}). object declaring repository's local configuration key-value pairs
git_prompt: # boolean, default(false). install git prompt configuration
git_prompt_init_file: # default('~/.bashrc'). Location to install prompt configuration into
git_prompt_vars: # default({}). object declaring ENV key-value pairs for git prompt
git_prompt_filepath: # default(<system default>). location of git-prompt.sh
```

## Dependencies

None

## Example Playbook
```yaml
- hosts: servers
  roles:
    - role: git
      vars:
        git_global_config:
          user.name: First Last
          user.email: first.last@service.com
        git_clones:
          - src: ssh://user@host:/path/to/repo
            dest: ~/workspace/repo
            config:
              user.name: nickname
        git_seeds:
          - src: ~/workspace/another_repo
            dest: ~/workspace/another_repo
        git_prompt: true
```

## License

MIT
