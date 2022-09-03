# Ansible Role: Maven

Installs Maven, and configures its repository settings. This role provides system or `/home/$USER/bin` installations, as well as user-declared pre-installations. It will also add binaries for home installations and maven completion scripts to the users initialization script.

## Requirements

- `~/bin`: `git`
- system
  - MacOS: `brew` is installed
  - Linux: `sudo` privileges
- all:
  - `java`


## Role Variables

#### Settable Variables
```yaml
maven_installation: # required. Valid values are 'home', 'system', 'none'.
maven_home: # pathname, optional. The path to a previously installed `mvn` home directory
maven_version: # string, default(<latest>). the Maven version to use for a home installation.  Only used when `maven_home_install=true`.
maven_reset: # boolean, default(false). will delete `~/.m2` when true. Will also delete preexisting home maven installation when true.
maven_completions_filepath: # default(<sourced from bash-completion role>). filepath to install maven bash completion script to. Requires override if performing a home installation.

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
        maven_username: "{{ vault.username }}"
        maven_password: "{{ vault.password }}"
        maven_mirror_release_url: https://company.jfrog.io/artifactory/libs-release
        maven_mirror_snapshot_url: https://company.jfrog.io/artifactory/libs-snapshot
```

## License

MIT
