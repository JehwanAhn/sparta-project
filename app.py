from flask import Flask, render_template, jsonify, request
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.tools import argparser

from itertools import chain
from collections import defaultdict

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/youtube', methods=['GET'])
def youtube_get():
    DEVELOPER_KEY = "AIzaSyDtpUpeVe3BiMoW2c-WHhOLknfx6Ce9KQo"
    YOUTUBE_API_SERVICE_NAME = "youtube"
    YOUTUBE_API_VERSION = "v3"
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

    videos = []
    cm1 = youtube.playlistItems().list(
        playlistId="UUtwxuughKbSAV0e4bnz4ORg",
        part="snippet",
        maxResults=20
    ).execute()

    cm2 = youtube.playlistItems().list(
        playlistId="UU3DNe5b3NYZ5ojre8YE1_xw",
        part="snippet",
        maxResults=20
    ).execute()

    cm3 = youtube.playlistItems().list(
        playlistId="UUHPuCs7c4jJmDJHdOn3mIDA",
        part="snippet",
        maxResults=20
    ).execute()

    cm4 = youtube.playlistItems().list(
        playlistId="UU4a9C90kI9QzTVx9HRdlsjw",
        part="snippet",
        maxResults=20
    ).execute()

    cm5 = youtube.playlistItems().list(
        playlistId="UUfsdRdf5YvHDb3bWxkF_0_g",
        part="snippet",
        maxResults=20
    ).execute()

    cm6 = youtube.playlistItems().list(
        playlistId="UUotjQBM9iMsYS0sY-FB0kNw",
        part="snippet",
        maxResults=20
    ).execute()

    cm7 = youtube.playlistItems().list(
        playlistId="UUul4FTKARC-EaBq0e8UH7RA",
        part="snippet",
        maxResults=20
    ).execute()

    cm8 = youtube.playlistItems().list(
        playlistId="UUOVjr02SIkhawHoJzT3WuhQ",
        part="snippet",
        maxResults=20
    ).execute()

    cm9 = youtube.playlistItems().list(
        playlistId="UUXvftM-43hGjGc1TA-8Y_IA",
        part="snippet",
        maxResults=20
    ).execute()

    cm = defaultdict(list)
    for k, v in chain(cm1.items(), cm2.items(), cm3.items(), cm4.items(), cm5.items(), cm6.items(), cm7.items(), cm8.items(), cm9.items()):
        cm[k].append(v)

    for i in cm['items']:
        videos.append(i)

    print(videos)
    return jsonify({'all_videos': videos})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
