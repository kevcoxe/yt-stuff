# yt-to-plex 

The purpose is to be able to download YouTube videos and add them to a plex server for safe keeping.
I have saved playlists of how to videos on YouTube and then the author or YouTube take them down and
I am unable to refer back to the video.

You can spin this up in a container or run it on a server, it will download the video and then scp it
over to your server that you specify.


### Setup Environment variables

create `.env` file from `.env.example`

```
DL_DOWNLOAD_PATH=       # place to download videos to (/app/downloads)
DL_SERVER_PASSWORD=     # password to the plex server or where you save them
DL_USERNAME=            # username for that server (with ssh access)
DL_SERVER=              # server to scp files to
DL_SERVER_PATH=         # directory on the server to save the files

                        # not used yet
PLEX_USERNAME='plex'    # the plex user on the server
PLEX_ITEM_ID='8'        # the id of the library in plex you want to refresh
```

### Run with docker-compose

```
docker-compose up --build
```
