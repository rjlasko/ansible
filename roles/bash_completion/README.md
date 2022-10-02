# Ansible Role: Bash Completions

Installs the `bash-completion` shell utility, to enhance shell usability.

## Requirements

`bash`!

- Linux: `sudo` privileges
- MacOS: `brew` is installed

## Role Variables

#### Settable Variables
```yaml
bash_completion_install: # boolean, default(false). installs system package
bash_completion_init_file: # filepath, optional. filepath to initialize bash_completions in.
```

#### Set Facts
```yaml
bash_completion_filepath: # OS specific path to load bash completions
bash_completions_dir: # OS specific path for command completions
```

## Dependencies

None

## Example Playbook
```yaml
- hosts: servers
  roles:
    - role: bash_completion
      vars:
        bash_completion_install: true
        bash_completion_init_file: ~/.bashrc
```

## License

MIT
