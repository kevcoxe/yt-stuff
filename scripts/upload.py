import os
import pysftp


SERVER = os.getenv('SERVER')
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')


def upload_to_server(stream, filepath):
    with pysftp.Connection(SERVER, username=USERNAME, password=PASSWORD) as sftp:
        with sftp.cd('public'):
            sftp.put(filepath)