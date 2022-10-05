# Ansible Role: Java

Installs any number of OpenJDK versions and uses `jenv` to manage them. `java` installations are provided OS package manager installations, or by preexisting system or user-declared installations. `jenv` is provided as a system installation on MacOS, whereas Linux only supports `/home/$USER/.jenv` installations.

## Requirements

- MacOS: `brew` is installed
- Linux: `sudo` privileges
- or, preexisting `java` installation(s)

## Role Variables

#### Settable Variables
```yaml
java_install: # boolean, default(false). Performs system installation of specified `java_versions` and `java_extra_system_packages`.
java_versions: # list, default([]). Java (numeric) versions of OpenJDK to install via OS package manager. It is possible the desired java version may not be available via system package, so please check if this gives an error.
java_extra_system_packages: # list, default([]). Additional packages to install via OS package manager
java_homes: # list, default([]). Suitable JAVA_HOME filepaths of installed JDKs

jenv_install: # boolean, default(false). Installs jenv for user management of Java installations.
jenv_reset: # boolean, default(true), delete preexisting jenv configuration (+installation for Linux)
jenv_java_version: # required. Java version to configure Jenv to use globally. For Java 8 and below, must use 1.x format.
jenv_init_file: # filepath, optional. filepath to update PATH with jenv shims + completions
```

## Dependencies

None

## Example Playbook
```yaml
- hosts: servers
  become: true
  roles:
    - role: java
      vars:
        java_install: true
        java_versions:
          - 8
          - 11
        jenv_install: true
        jenv_java_version: 1.8
        jenv_init_file: ~/.bashrc
```

## License

MIT

## References

[jEnv](https://github.com/jenv/jenv)
