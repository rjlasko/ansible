# ZFS on Linux

ZFS snapshots & scrubbing definitions are only referred to in the `zfs_packages` section, but have no defined configuration.  It is assumed that these are addressed elsewhere...

## Snapshots:
The `zfs-auto-snapshot` package enables automatic snapshots.

Manual: `man zfs-auto-snapshot`

When the ZFS pool and its datasets are created, there is an opportunity to define properties that are used in snapshot automation.  Properties for the pool and each dataset can be inherited by their children.  Example:

```
zfs set snapdir=hidden                       zDisk/home
zfs set com.sun:auto-snapshot=false          zDisk/home
zfs set com.sun:auto-snapshot:frequent=true  zDisk/home
zfs set com.sun:auto-snapshot:hourly=true    zDisk/home
zfs set com.sun:auto-snapshot:daily=true     zDisk/home
zfs set com.sun:auto-snapshot:monthly=true   zDisk/home
zfs set snapdir=visible                     zDisk/home/user
zfs set com.sun:auto-snapshot=true          zDisk/home/user
```

Look at the list of available snapshots
`zfs list -t snapshot`

They can be found underneath the `.zfs` directory, at the root of each zpool or dataset.
`ls /zDisk/software/.zfs/`

This appears to be enacted by the following file:
`/etc/cron.d/zfs-auto-snapshot`

## Scrubbing:
The `zfsutils-linux` package enables automatic scrubbing, once a month.

This appears to be enacted by the following file:
`/etc/cron.d/zfsutils-linux`
