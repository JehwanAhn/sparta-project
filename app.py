from flask import Flask, render_template, jsonify, request
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.tools import argparser
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
  cm = youtube.playlistItems().list(
    playlistId="UUM31rBPQdifQKUmBKtwVqBg",
    part="snippet",
    maxResults=10
  ).execute()

  for i in cm['items']:
    videos.append(i)

  print(videos)
  return jsonify({'all_videos':videos})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)