# Ansible Role: AWS CLI
Installs and configures the AWS CLI.

#### Details
This Ansible role performs the following actions.
1. Installs the following packages.
  - `awscliv2`
2. Installs a caller-provided AWS configuration that details the named environments accessible with `awscli`.

The following files are written by this role:
- `~/.aws/config`

## Requirements
MacOSx
User provides an AWS `config` file.

## Role Variables

#### [Settable Variables](./meta/argument_specs.yml)

## Example Playbook
```yaml
- name: Install things
  hosts: localhost
  connection: local
  roles:
    - role: aws_cli
      vars:
        aws_config_src: "~/path/to/aws_config.ini"
```

## License

MIT

## References
* AWS Command Line Interface [Docs](https://docs.aws.amazon.com/cli/index.html)
* AWS Command Line Interface [Configuration & credential file settings](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html)
