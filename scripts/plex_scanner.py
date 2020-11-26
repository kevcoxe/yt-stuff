
import os

PLEX_USERNAME = os.environ['PLEX_USERNAME']
PLEX_ITEM_ID = os.environ['PLEX_ITEM_ID']

DL_USERNAME = os.environ['DL_USERNAME']
DL_SERVER = os.environ['DL_SERVER']
DL_SERVER_PASSWORD = os.environ['DL_SERVER_PASSWORD']


def scan_plex():
    cmd = f"""sshpass -p "{DL_SERVER_PASSWORD}" ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null {DL_USERNAME}@{DL_SERVER} 'sudo runuser -l {PLEX_USERNAME} -c "/usr/lib/plexmediaserver/Plex\ Media\ Scanner --scan --refresh --section {PLEX_ITEM_ID}"'"""
    if os.system(cmd) != 0:
        return False

    return True