#!/usr/bin/env bash
set -ueo pipefail


BRIDGE_NAME=$1

# actual interfaces ('lo' is not present)
INTERFACES=$(ip token | awk '{print $4}')
IFACE_MAC_PAIRS=""

for IFACE in $INTERFACES ; do
	INFO=$(ip address show $IFACE)
	# filter by those in the "UP" state
	if grep --quiet 'UP' <<< "$INFO" ; then
		# filter by those with an "inet" address
		if grep --quiet 'inet' <<< "$INFO" ; then
			MAC=$(echo "$INFO" | grep 'link/ether' | awk '{print $2}')
			if [ -n "${IFACE_MAC_PAIRS}" ] ; then
				IFACE_MAC_PAIRS="${IFACE_MAC_PAIRS}\n"
			fi
			IFACE_MAC_PAIRS="${IFACE_MAC_PAIRS}${IFACE} ${MAC}"
		fi
	fi
done

# sort by MAC address
# use interface with earliest MAC address
echo ${IFACE_MAC_PAIRS} | sort -k2 | head -n1 | awk '{print $1}'
