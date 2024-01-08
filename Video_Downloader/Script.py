from flask import Flask, render_template, request, send_file
from pytube import YouTube
import os
import re

app = Flask(__name__)

def sanitize_filename(filename):
    # Remove invalid characters from the filename
    return re.sub(r'[\/:*?"<>|]', '', filename)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    if request.method == 'POST':
        video_url = request.form['video_url']
        try:
            yt = YouTube(video_url)
            video = yt.streams.get_highest_resolution()
            # Sanitize the filename before saving
            subdirectory = 'downloads'
            filename = f'{subdirectory}/{sanitize_filename(yt.title)}.mp4'
            video.download(f'{subdirectory}/')
            return send_file(filename, as_attachment=True)
        except Exception as e:
            return render_template('index.html', error=str(e))
if __name__ == '__main__':
    app.run(debug=True)
