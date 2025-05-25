from flask import Flask, request, send_file, render_template
import yt_dlp
import os
import glob
import uuid

app = Flask(__name__)

DOWNLOAD_FOLDER = "/tmp"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form["url"]
        formato = request.form["format"]
        unique_id = str(uuid.uuid4())[:8]

        if formato == "mp3":
            outtmpl = os.path.join(DOWNLOAD_FOLDER, f"{unique_id} - %(title)s.%(ext)s")
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': outtmpl,
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'quiet': True,
            }
            ext = "mp3"

        elif formato == "mp4":
            outtmpl = os.path.join(DOWNLOAD_FOLDER, f"{unique_id} - %(title)s.%(ext)s")
            ydl_opts = {
                'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',
                'outtmpl': outtmpl,
                'merge_output_format': 'mp4',
                'quiet': True,
            }
            ext = "mp4"

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

            result_file = glob.glob(os.path.join(DOWNLOAD_FOLDER, f"{unique_id}*.{ext}"))[0]
            filename = os.path.basename(result_file)
            return send_file(result_file, as_attachment=True, download_name=filename)

        except Exception as e:
            return render_template("index.html", mensaje=f"❌ Error: {str(e)}")

    return render_template("index.html", mensaje=None)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
