import os
import _thread

DL_USERNAME = os.getenv('DL_USERNAME', None)
DL_SERVER = os.getenv('DL_SERVER', None)
DL_SERVER_PASSWORD = os.environ['DL_SERVER_PASSWORD']
DL_SERVER_PATH = os.environ['DL_SERVER_PATH']


def remove(filepath):
    cmd = f'rm -f {filepath}'
    if os.system(cmd) != 0:
        return False

    return True

def upload(filepath):
    cmd = f'sshpass -p "{DL_SERVER_PASSWORD}" scp -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -q {filepath} {DL_USERNAME}@{DL_SERVER}:{DL_SERVER_PATH}/.'
    print(f'attemptint to run: {cmd}')
    if os.system(cmd) != 0:
        return False

    return remove(filepath)

def threaded_upload(stream, filepath):
    if DL_USERNAME is not None and DL_SERVER is not None:
        _thread.start_new_thread(upload, (filepath,))
    return True
