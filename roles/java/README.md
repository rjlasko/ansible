# Ansible Role: Java

Installs any number of OpenJDK versions and uses `jenv` to manage them. `java` installations are provided OS package manager installations, or by user-declared pre-installations.  `jenv` is provided as a system installation on MacOS, whereas Linux only supports `/home/$USER/.jenv` installations.

## Requirements

- MacOS: `brew` must be installed
- Linux: `apt` must be installed
- or known preexisting Java installation(s)

## Role Variables

#### Settable Variables
```yaml
java_system_versions: # list of Java (numeric) versions of OpenJDK to install via OS package manager
java_system_packages: # list of packages to install via OS package manager
java_homes: # list of suitable JAVA_HOME filepaths of installed JDKs

jenv_java_version: # default(11). Java version to configure Jenv to use globally. For Java 8 and below, must use 1.x format.
java_reset_jenv: # boolean, default(false), delete preexisting jenv configuration (+installation for Linux)
jenv_init_file: # default('~/.bashrc'), filepath to update PATH with jenv shims + completions
```


## Dependencies

None

## Example Playbook
```yaml
- hosts: servers
  roles:
    - role: java
      vars:
        java_reset_jenv: true
        java_system_versions:
          - 8
          - 11
        java_jenv_version: 1.8
```

## License

MIT

## References

[jEnv](https://github.com/jenv/jenv)
