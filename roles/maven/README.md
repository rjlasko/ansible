# Ansible Role: Maven

Installs Maven, and configures its repository settings. This role provides system or `/home/$USER/bin` installations, as well as user-declared pre-installations. It will also add binaries for home installations and maven completion scripts to the users initialization script.

## Requirements

`java`!

`user`
  - All: `git`

`system`
  - MacOS: `brew` is installed
  - Linux: `sudo` privileges


## Role Variables

#### Settable Variables
```yaml
maven_installation: # required. Valid values are ['user', 'system', 'none'].
maven_home: # pathname, default(null). The path to a preexisting maven installation. Only used when `maven_installation=none`.
maven_version: # string, default(<latest>). the Maven version to use for a user installation. Only used when `maven_home_install=true`.
maven_reset: # boolean, default(false). When true, will delete `~/.m2` when true and preexisting maven user installation.
maven_init_file: # filepath, optional. filepath to add maven to shell environment when not a system installation. also includes optional maven aliases when `maven_init_aliases=true`
maven_init_aliases: # boolean, default(false). Adds helper aliases to `maven_init_file`
maven_completions_filepath: # default(<sourced from bash-completion role>). filepath to install maven bash completion script to. Requires override if performing a user installation.

# The following only apply when using authentication for a maven repository
maven_username: # string (optional), username
maven_password: # string (optional), password
maven_mirror_release_url: # string (optional), URL for release mirror
maven_mirror_snapshot_url: # string (optional), URL for snapshot mirror
```

Note, if either username or password are provided, then all 4 of the variables above must be provided.

## Dependencies

`bash-completion` role if using default location non-system or Linux installation of maven-completion

## Example Playbook
```yaml
- hosts: servers
  roles:
    - role: maven
      vars:
        maven_installation: user
        maven_init_file: ~/.bashrc
        maven_username: "{{ vault.username }}"
        maven_password: "{{ vault.password }}"
        maven_mirror_release_url: https://company.jfrog.io/artifactory/libs-release
        maven_mirror_snapshot_url: https://company.jfrog.io/artifactory/libs-snapshot
```

## License

MIT
