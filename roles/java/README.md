# Ansible Role: Java

Installs any number of Java versions and uses `jenv` to manage them.

## Requirements

- MacOS: `brew` must be installed
- Linux: `apt` must be installed
- or known preexisting Java installation(s)

## Role Variables

#### Settable Variables
```yaml
java_homes: # list of suitable JAVA_HOME filepaths of installed JDKs. using this will skip brew/apt installation
java_system_versions: # list of Java packages to install via OS package manager
java_reset_jenv: # boolean, default(false), delete preexisting jenv
java_global_versions: # list of Java versions to put into PATH
java_jenv_user_dir: # default('~/.jenv'), path to user directory to install jenv from source
java_jenv_init_file: # default('~/.bashrc'), filepath to update PATH with jenv shims + completions
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
        java_system_versions:
          - adoptopenjdk/openjdk/adoptopenjdk8
          - adoptopenjdk/openjdk/adoptopenjdk11
        java_global_versions: 1.8
```

## License

MIT

## References

[jEnv](https://github.com/jenv/jenv)
