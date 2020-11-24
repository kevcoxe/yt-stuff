from flask import Flask, request, render_template

from scripts.downloader import Downloader


app = Flask(__name__)
yt_downloader = Downloader()

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/download', methods=['POST'])
def api_v1_download():
    yt_url = request.form.get('url', None)

    if yt_url is None:
        return 'Invalid url', 400

    Downloader.add_url_to_queue(yt_url)
    message = f'Successfully added to the queue'
    return render_template('index.html', message=message)
    
@app.route('/status', methods=['GET'])
def check_downloads():
    info = Downloader.check_downloads()
    return render_template('status.html', status=info['status'], downloads=info['list'])

