# Ansible Role: Java

Installs any number of Java versions and `jenv` to manage them.

## Requirements

- MacOS: Homebrew must be installed

## Role Variables

#### Settable Variables
```yaml
java_reset_jenv: # boolean, delete preexisting jenv
java_brew_versions: # list of Java packages to install via brew
java_global_versions: # list of Java versions to put into PATH

java_jenv_init_file: # filepath to update PATH update with jenv shims. default: ~/.bashrc
java_jenv_init_file_create: # boolean, create the jenv init file. default: false
```

## Dependencies

None

## Example Playbook
```yaml
- hosts: servers
  roles:
    - role: java
      vars:
        java_reset_jenv: false
        java_brew_versions:
          - adoptopenjdk/openjdk/adoptopenjdk8
          - adoptopenjdk/openjdk/adoptopenjdk11
        java_global_versions: 1.8
```

## License

MIT

## References

[jEnv](https://github.com/jenv/jenv)
