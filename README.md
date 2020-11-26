
## Setup Environment variables

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

# Run with docker-compose

```
docker-compose up --build
```