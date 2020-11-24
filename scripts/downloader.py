import time
import threading
import math

from pytube import YouTube, Playlist
from scripts.upload import threaded_upload
from scripts.utils import clean_filename

DOWNLOAD_OUTPUT_PATH = 'downloads'


def download_url(yt_url):
    try:
        print(f'Attempting to download: {yt_url}')

        yt = YouTube(yt_url)

        yt.register_on_complete_callback(threaded_upload)
        title = yt.title

        download_path = yt.streams.filter(
            progressive=True,
            file_extension='mp4'
            ).order_by('resolution')[-1].download(
                output_path=DOWNLOAD_OUTPUT_PATH
            )

        print(f'Successfully downloaded: {title} to {download_path}')
        return True, title

    except Exception as e:
        print(f'Failed to download url because: {e}')
        return False, e


def finish_callback(stream, filepath):
    print(f'Finished downloading: {filepath}')

def progress_callback(stream, chunk, bytes_remaining):
    filesize = stream.filesize
    total_left = 100 - math.floor((bytes_remaining / filesize) * 100)
    print(f'Downloading with remaining: {total_left}')


class Downloader(threading.Thread):
    __instance          = None
    __stream            = None
    __status            = None
    __stop_thread       = False
    __interval_delay    = 2
    __yt_objs           = []

    def __init__(self, interval_delay=2):
        if Downloader.__instance is not None:
            raise Exception('This class is a singleton')
        else:
            threading.Thread.__init__(self)
            Downloader.__instance = self
            self.start()

    @classmethod
    def is_running(cls):
        if Downloader.__instance is None:
            return False
        else:
            return Downloader.__instance.isAlive()

    @classmethod
    def stop_watching(cls):
        if Downloader.is_running():
            Downloader.__stop_thread = True

    @classmethod
    def add_url_to_queue(cls, yt_url, progress_callback=progress_callback, finished_callback=threaded_upload):
        if 'index=' in yt_url:
            pl = Playlist(yt_url)
            yt_list = pl.videos

        else:
            yt_list = [YouTube(yt_url)]
        
        for yt in yt_list:
            if progress_callback is not None:
                yt.register_on_progress_callback(progress_callback)

            if finished_callback is not None:
                yt.register_on_complete_callback(finished_callback)

            Downloader.__yt_objs.append({
                'stream': yt,
                'title': yt.title,
                'status': 'waiting'
            })

    @classmethod
    def check_downloads(cls):
        return_object = {
            'status': Downloader.__status,
            'list': Downloader.__yt_objs
        }

        return return_object

    def run(self):
        self.start_download()

    def start_download(self):
        if Downloader.__status is not None:
            return False

        while not Downloader.__stop_thread and Downloader.__interval_delay > 0:
            # grab a yt obj and start the download and update progress
            while Downloader.__yt_objs:
                Downloader.__status = 'DOWNLOADING'
                yt_obj = Downloader.__yt_objs[0]
                yt = yt_obj['stream']

                # update status so the check_downloads will show it
                Downloader.__yt_objs[0]['status'] = 'downloading'

                safe_filename = clean_filename(yt.title)

                # download the object
                download_path = yt.streams.filter(
                    progressive=True,
                    file_extension='mp4'
                ).order_by('resolution')[-1].download(
                    output_path=DOWNLOAD_OUTPUT_PATH,
                    filename=safe_filename
                )

                # remove the obj at the end
                del Downloader.__yt_objs[0]

                Downloader.__status = None
            time.sleep(Downloader.__interval_delay)

        Downloader.__stop_thread = False
        return True

