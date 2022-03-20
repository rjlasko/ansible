#!/usr/bin/env bash

# XXX: This is a slightly modified version of:
# 	https://github.com/PassthroughPOST/VFIO-Tools/blob/master/libvirt_hooks/qemu

GUEST_NAME="$1"
HOOK_NAME="$2"
STATE_NAME="$3"
MISC="${@:4}"

BASEDIR="$(dirname $0)"

# HOOKPATH="$BASEDIR/$GUEST_NAME/$HOOK_NAME/$STATE_NAME"
HOOKPATH="$BASEDIR/$GUEST_NAME/$HOOK_NAME"

set -e # If a script exits with an error, we should as well.

# check if it's a non-empty executable file
if [ -f "$HOOKPATH" ] && [ -s "$HOOKPATH" ] && [ -x "$HOOKPATH" ]; then
    eval \"$HOOKPATH\" "$@"
elif [ -d "$HOOKPATH" ]; then
    while read file; do
        # check for null string
        if [ ! -z "$file" ]; then
          eval \"$file\" "$@"
        fi
    done <<< "$(find -L "$HOOKPATH" -maxdepth 1 -type f -executable -print;)"
fi
