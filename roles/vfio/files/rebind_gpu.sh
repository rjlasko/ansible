#!/usr/bin/env bash
set -x

echo "Beginning of teardown!"

# Unload VFIO-PCI Kernel Driver
modprobe -r vfio-pci
modprobe -r vfio_iommu_type1
modprobe -r vfio

# Re-Bind GPU to Display Driver
for pci_id in "${@:?'Requires PCI devices ID arguments to rebind. Ex: pci_0000_0a_00_1'}"
do
	virsh nodedev-reattach "${pci_id}"
done

# Rebind VT consoles (adapted from https://www.kernel.org/doc/Documentation/fb/fbcon.txt)
input="/tmp/vfio-bound-consoles"
while read consoleNumber; do
	if test -x /sys/class/vtconsole/vtcon${consoleNumber}; then
		if [ `cat /sys/class/vtconsole/vtcon${consoleNumber}/name | grep -c "frame buffer"` = 1 ]; then
			echo "Rebinding console ${consoleNumber}"
			echo 1 > /sys/class/vtconsole/vtcon${consoleNumber}/bind
		fi
	fi
done < "$input"

# Rebind framebuffer for nvidia
if test -e "/tmp/vfio-is-nvidia" ; then
	nvidia-xconfig --query-gpu-info > /dev/null 2>&1
	echo "efi-framebuffer.0" > /sys/bus/platform/drivers/efi-framebuffer/bind

	# Load NVIDIA drivers
	modprobe nvidia_drm
	modprobe nvidia_modeset
	modprobe nvidia_uvm
	modprobe nvidia
	#modprobe ipmi_devintf
	#modprobe ipmi_msghandler
fi

# Restart Display Manager
input="/tmp/vfio-store-display-manager"
while read displayManager; do
  if command -v systemctl; then
    systemctl start "$displayManager.service"
  else
    if command -v sv; then
      sv start $displayManager
    fi
  fi
done < "$input"

echo "End of teardown!"
