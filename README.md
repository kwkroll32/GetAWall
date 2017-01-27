<pre>
GetAWall will retrieve a hot image URL from reddit, suitable for use as a wallpaper.

usage: GetAWall.py [-h] [-w WIDTH] [-e HEIGHT] [-s SUBREDDIT] -c CREDENTIALS

optional arguments:
  -h, --help            show this help message and exit
  -w WIDTH, --width WIDTH
                        Width of your display [1920 px]
  -e HEIGHT, --height HEIGHT
                        Height of your display [1080 px]
  -s SUBREDDIT, --subreddit SUBREDDIT
                        Subreddit [earthporn]
  -c CREDENTIALS, --credentials CREDENTIALS
                        txt file of reddit api credentials, json

Todo: 
  1. Add ability to poll more than one subreddit for a suitable image.
  2. Pull fewer posts at once, then looping until a suitable image is found.

Examples:
Quickstart: 
python GetAWall.py -c reddit_cred.json

Combined with feh: 
feh $(python /home/karl/Tools/scripts/GetAWall.py -c /home/karl/Tools/scripts/reddit_cred.json)

Setting a new wallpaper on login to i3wm (add the following to the i3 .config):
exec_always --no-startup-id feh --bg-fill $(python GetAWall.py -c reddit_cred.json)
<pre>
