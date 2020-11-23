from flask import Flask, request

from scripts.downloader import download_url


app = Flask(__name__)


@app.route('/download', methods=['POST'])
def api_v1_download():
    yt_url = request.json.get('url', None)

    if yt_url is None:
        return 'Invalid url', 400

    download_success, message = download_url(yt_url)
    if not download_success:
        return f'Failed to download: {message}', 400

    return f'Successfully downloaded: {message}', 200
    