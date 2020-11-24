import os
import _thread

DL_SSH_KEY = os.environ['DL_SSH_KEY']
DL_PATH = os.environ['DL_PATH']
DL_USERNAME = os.environ['DL_USERNAME']
DL_SERVER = os.environ['DL_SERVER']
DL_SERVER_PATH = os.environ['DL_SERVER_PATH']

# cmd = f'/usr/bin/rsync --remove-source-files -zvhr {DL_PATH} {DL_USERNAME}@{DL_SERVER}:{DL_SERVER_PATH} --progress'

def remove(filepath):
    cmd = f'rm -f {filepath}'
    os.system(cmd)
    return True

def upload(filepath):
    cmd = f'scp -i {DL_SSH_KEY} {filepath} {DL_USERNAME}@{DL_SERVER}:{DL_SERVER_PATH}/.'
    print(f'attemptint to run: {cmd}')
    if os.system(cmd) != 0:
        return False

    return remove(filepath)

def threaded_upload(stream, filepath):
    _thread.start_new_thread(upload, (filepath,))
    return True
