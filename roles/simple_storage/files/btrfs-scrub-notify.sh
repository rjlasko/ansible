#!/usr/bin/env bash

PATH=/sbin:/bin:/usr/sbin:/usr/bin
export PATH


if [ -f /etc/sysconfig/btrfsmaintenance ] ; then
	. /etc/sysconfig/btrfsmaintenance
fi

if [ -f /etc/default/btrfsmaintenance ] ; then
	. /etc/default/btrfsmaintenance
fi

# . $(dirname $(realpath "$0"))/btrfsmaintenance-functions
# BTRFS_SCRUB_MOUNTPOINTS=$(expand_auto_mountpoint "$BTRFS_SCRUB_MOUNTPOINTS")

btrfs scrub status /srv/media | mail --subject "BTRFS scrub status: $(hostname)" admin@rjlasko.com
