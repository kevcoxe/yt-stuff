from flask import Flask, request, render_template, redirect, url_for

from scripts.downloader import Downloader


app = Flask(__name__)
yt_downloader = Downloader()

@app.route('/', methods=['GET'])
def index():
    info = Downloader.check_downloads()
    return render_template('index.html', message=message, status=info['status'], downloads=info['list'])


@app.route('/download', methods=['POST'])
def api_v1_download():
    yt_url = request.form.get('url', None)

    if yt_url is None:
        return 'Invalid url', 400

    Downloader.add_url_to_queue(yt_url)
    return redirect(url_for('index'))
    
@app.route('/status', methods=['GET'])
def check_downloads():
    info = Downloader.check_downloads()
    return render_template('status.html', status=info['status'], downloads=info['list'])

