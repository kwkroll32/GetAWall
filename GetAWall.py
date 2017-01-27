'''
GetAWall will retrieve a hot image from reddit, suitable for use as a wallpaper
'''
from __future__ import print_function
import argparse
import urllib
import cStringIO
import json
import praw
from PIL import Image

def qualifies(width, height, width_o, height_o):
    '''
    qualifies will determine whether the given image dimensions are suitable for use as a wallpaper.
    checks total size and aspect ratio
    '''
    if width < width_o or height < height_o:
        # too small
        return False
    elif howclose(width, height, width_o, height_o) > 0.2:
        # wrong aspect ratio
        return False
    else:
        return True

def howclose(width, height, width_o, height_o):
    '''
    howclose will determine the percent error in aspect ratio
    between the given reddit image (width, height) and the desired resolution (width_o, height_o)
    '''
    return ((float(width_o)*height/width)-height_o)/float(height_o)

def getsize(url):
    '''
    getsize accepts the url of an image and returns the dimensions of that image
    '''
    img_file = cStringIO.StringIO(urllib.urlopen(url).read())
    try:
        img = Image.open(img_file)
    except IOError:
        return 1, 1
    width, height = img.size
    return width, height

def getcreds(cred_file):
    '''
    getcreds will parse the given file path for reddit credentials
    Example credentials json file:
    {
	    "client_id":     "abcdefghijklm",
        "client_secret": "ABCDEFGHIJLKMNOPQRSTUVWXYZ"
    }
    '''
    with open(cred_file) as data_file:
        data = json.load(data_file)
    return data["client_id"], data["client_secret"]

def main():
    '''
    GetAWall will retrieve a hot image from reddit, suitable for use as a wallpaper
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument("-w", "--width", type=int, default=1920,
                        help="Width of your display, px")
    parser.add_argument("-e", "--height", type=int, default=1080,
                        help="Height of your display, px")
    parser.add_argument("-s", "--subreddit", default="earthporn",
                        help="Subreddits")
    parser.add_argument("-c", "--credentials", required=True,
                        help="txt file of reddit api credentials, json")
    args = parser.parse_args()

    ra_id, ra_sec = getcreds(args.credentials)
    reddit = praw.Reddit(client_id=ra_id, client_secret=ra_sec,
                         user_agent='Python :GetAWall:v1.0 (by /u/kwkroll32)')

    for submission in reddit.subreddit(args.subreddit).hot(limit=7):
        width, height = getsize(submission.url)
        if qualifies(width, height, args.width, args.height):
            print(submission.url)
            return 0

if __name__ == "__main__":
    main()
