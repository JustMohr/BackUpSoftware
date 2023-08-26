import os

cmd = "udisksctl unmount -b /dev/sdb1"
os.system(cmd)
cmd = "udisksctl power-off -b /dev/sdb"
os.system(cmd)

#bind:
#cmd = "echo '1-9' |tee /sys/bus/usb/drivers/usb/bind"
#os.system(cmd)