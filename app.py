from flask import Flask, render_template, request, redirect, url_for, flash
from pytube import YouTube
from pytube.exceptions import PytubeError

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flashing messages

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        video_url = request.form.get('video_url')
        try:
            yt = YouTube(video_url)
            video_stream = yt.streams.get_highest_resolution()
            video_stream.download(output_path='downloads')  # Specify your download path
            flash('Download completed!')
        except PytubeError as e:
            flash(f'An error occurred: {e}')
        except Exception as e:
            flash(f'An unexpected error occurred: {e}')
        return redirect(url_for('index'))
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
