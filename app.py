from flask import Flask, request, render_template, redirect, url_for

from scripts.downloader import Downloader
from scripts.upload import Uploader


app = Flask(__name__)
yt_downloader = Downloader()
yt_uploader = Uploader()

@app.route('/', methods=['GET'])
def index():
    download_info = Downloader.check_downloads()
    upload_info = Uploader.check_upload()

    return render_template('index.html',
        download_status=download_info['status'],
        downloads=download_info['list'],
        upload_status=upload_info['status'],
        uploads=upload_info['list']
    )

@app.route('/download', methods=['POST'])
def api_v1_download():
    yt_url = request.form.get('url', None)

    if yt_url is None:
        return 'Invalid url', 400

    Downloader.add_url_to_queue(yt_url)
    return redirect(url_for('index'))
    
@app.route('/status', methods=['GET'])
def check_downloads():
    download_info = Downloader.check_downloads()
    upload_info = Uploader.check_upload()

    return render_template('status.html',
        download_status=download_info['status'],
        downloads=download_info['list'],
        upload_status=upload_info['status'],
        uploads=upload_info['list']
    )

