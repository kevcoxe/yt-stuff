import os
import time
import threading

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


def finished_upload(filepath):
    print(f'Finished uploading file: {filepath}')



class Uploader(threading.Thread):
    __instance          = None
    __status            = None
    __stop_thread       = False
    __interval_delay    = 2
    __upload_queue      = []

    def __init__(self, interval_delay=2):
        if Uploader.__instance is not None:
            raise Exception('This class is a singleton')
        else:
            threading.Thread.__init__(self)
            Uploader.__instance = self
            self.start()

    @classmethod
    def is_running(cls):
        if Uploader.__instance is None:
            return False
        else:
            return Uploader.__instance.isAlive()

    @classmethod
    def stop_watching(cls):
        if Uploader.is_running():
            Uploader.__stop_thread = True

    @classmethod
    def add_to_queue(cls, yt_obj, finished_callback=finished_upload):
        Uploader.__upload_queue.append(yt_obj)

    @classmethod
    def check_upload(cls):
        return_object = {
            'status': Uploader.__status,
            'list': Uploader.__upload_queue
        }

        return return_object

    def run(self):
        self.start_upload()

    def start_upload(self):
        if Uploader.__status is not None:
            return False

        while not Uploader.__stop_thread and Uploader.__interval_delay > 0:
            # grab a yt obj and start the download and update progress
            while Uploader.__upload_queue:
                Uploader.__status = 'DOWNLOADING'
                yt_obj = Uploader.__upload_queue[0]
                yt = yt_obj['stream']

                # update status so the check_downloads will show it
                yt_obj['status'] = 'uploading'

                # upload the file
                upload(yt_obj['file_path'])

                # remove the obj at the end
                del Uploader.__upload_queue[0]

                Uploader.__status = None
            time.sleep(Uploader.__interval_delay)

        Uploader.__stop_thread = False
        return True

