from pytube import YouTube
from scripts.upload import upload_to_server

DOWNLOAD_OUTPUT_PATH = 'downloads'


def download_url(yt_url):
    try:
        yt = YouTube(
            yt_url,
            on_complete_callback=upload_to_server
        )

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
