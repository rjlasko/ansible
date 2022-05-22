# Ansible Role: AWS Utilities
Installs and configures applications that support usage of the AWS platform.

#### Details
This Ansible role performs the following actions.
1. Installs the following packages.
  - `awscliv2`
  - `gimme-aws-creds`
2. Installs a caller-provided AWS configuration that details the named environments accessible with `awscli`.
3. Creates the configuration that is used by `gimme-aws-creds`, to retrieve AWS access credentials starting from Okta.
4. Installs the `aws-login` script and associated `launchd` service to support hands-off AWS login and credential upkeep.

The following files are written by this role:
- `~/.aws/config`
- `~/.okta_aws_login_config`
- `~/bin/aws-login`
- `~/Library/LaunchAgents/{{ aws_gimme_creds_plist_domain }}.aws_login.plist`

The following file is created upon running `aws-login` for the first time, and will be kept up to date by the `launchd` service.
- `~/.aws/credentials`

## Requirements
User provides an AWS `config` file.
MacOSx

## Role Variables

#### Settable Variables
```yaml
aws_config_file: # path of file to copy over ~/.aws/config
aws_gimme_creds_plist_domain: # string, a unique string to include in plist filename and other XML attribute
aws_gimme_creds_pretest: # (optional) string, a bash command predicate for login

aws_login_rolename: # The ARN of the role you want temporary AWS credentials for. The reserved word 'all' can be used to get and store credentials for every role the user is permissioned for.
aws_okta_app_url: # the url to the aws application configured in Okta.
okta_org_url: # Okta organization url, which is typically something like https://companyname.okta.com
okta_username: # (optional), username for Okta to authenticate. default: host's $USER

aws_login_filepath: # (optional) string, location to install `aws-login` script to. default: ~/bin/aws-login
aws_completions_filepath: # filepath to load aws completions. default: ~/.bashrc
```

## Example Playbook
```yaml
- name: Install things
  hosts: localhost
  connection: local
  roles:
    - role: aws_utils
      vars:
        aws_gimme_creds_plist_domain: beep.boop
        aws_gimme_creds_pretest: ping -o -c 1 robot.beep.boop
        aws_config_file: "~/path/to/aws_config.ini"
```

#### Initiate periodic automatic login
```bash
# Create an Ansible playbook and run via the following invocation.
ansible-playbook playbook.yml
# run login for the first time, which should ask for login information, and store it in the keychain. You will not need to do this again, unless you rerun this role.
aws-login
```

#### Using a different role than the login
```bash
# Given the name of a profile declared in `~/.aws/config`
export AWS_PROFILE=dev
# any aws command will use that profile by default without having to specify it.  For example:
aws s3 ...
# alternatively, you can provide the profile directly, which will also override the ENV variable if it is set
aws --profile dev s3
```

## License

MIT

## References
* GitHib for [gimme-aws-creds](https://github.com/Nike-Inc/gimme-aws-creds)
* Ansible run playbook with [variables from a YAML file](https://docs.ansible.com/ansible/latest/user_guide/playbooks_variables.html#vars-from-a-json-or-yaml-file)
* AWS Command Line Interface [Docs](https://docs.aws.amazon.com/cli/index.html)
* AWS Command Line Interface [Configuration & credential file settings](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html)
* MacOSX [Creating Launchd Agents and Daemons](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/CreatingLaunchdJobs.html#//apple_ref/doc/uid/10000172i-SW7-BCIEDDBJ)
