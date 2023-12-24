# This file is part of https://github.com/jainamoswal/Flask-Example.
# Usage covered in <IDC lICENSE>
# Jainam Oswal. <jainam.me> 


# Import Libraries 
from app import app
from flask import render_template
import slow
import ytpb

def slow_verb_processing(room_size, wet_level,  speed, link):
    try:
        ytpb.download(link, room_size, wet_level, speed)
        return True
    except:
        return False
    


# Define route "/" & "/<name>"
@app.route("/")
@app.route("/<name>")
def index(name=''):
    return render_template('simple.html',name=name)

