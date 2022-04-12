# Ansible Role: Python

Installs any number of Java versions and `jenv` to manage them.

## Requirements

- MacOS: Homebrew must be installed

## Role Variables

#### Settable Variables
```yaml
java_reset_jenv: # boolean, delete preexisting jenv
java_brew_versions: # list of Java packages to install via brew
java_global_versions: # list of Java versions to put into PATH
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
        python_global_versions: 1.8
```

## License

MIT

## References

[jEnv](https://github.com/jenv/jenv)
