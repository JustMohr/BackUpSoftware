import shutil
from datetime import datetime
import os
import time

def message(message):
    os.system('notify-send "BackupSoftware" "' + message + '"')
    return


# path to destination directory
dest_dir = '/media/justin/Justin'

# path to source directory
src_dir = '/mnt/ce9bf153-7b24-48a6-a0f8-610e192c7aa6/Prog'
 
# folder name path
now = datetime.now().strftime("%Y-%m-%d_%H-%M")
dest_flnm = dest_dir + '/' + format(now)




isdir = os.path.isdir(dest_flnm)
if isdir == False:
    shutil.copytree(src_dir, dest_flnm)
    message('create backup')
else:
    print('exist')


files = os.listdir(dest_dir)

if len(files) >= 6:

    files.sort(key=lambda flnm: os.path.getctime(os.path.join(dest_dir, flnm)))
    

    file_remove_path = os.path.join(dest_dir, files[0])
    shutil.rmtree(file_remove_path, ignore_errors=True)
    message('remove: {} '.format(file_remove_path))


time.sleep(5)
cmd = "udisksctl unmount -b /dev/sdb1"
os.system(cmd)
time.sleep(5)
cmd = "udisksctl power-off -b /dev/sdb"
os.system(cmd)

message('eject device')