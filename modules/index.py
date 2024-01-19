
# Import Libraries 
from app import app
from flask import render_template
from flask import request
import slow
import ytpb

@app.route("/process_data", methods=["POST"])
def process_data():
    client_ip = request.remote_addr
    if request.method == "POST":
        room_size = request.form.get("roomSize")
        wet_level = request.form.get("wetness")
        speed = request.form.get("speed")
        link = str(request.form.get("link"))

        # Type conversion
        try:
            room_size = float(room_size)
            wet_level = float(wet_level)
            speed = float(speed)
        except ValueError:
            return "Invalid numeric input", 400
        speed +=  1
        success = ytpb.download(link, room_size, wet_level, speed)
        

        if success:
            return render_template('song.html', song_name = success)
        else:
            return "Processing failed. Please check inputs and try again."  # Handle errors


# Define route "/" & "/<name>"
@app.route("/")
def index():
    return render_template('index.html')

