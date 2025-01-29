from flask import Flask, render_template
from flask_socketio import SocketIO
import pyautogui
import os

# Initialize Flask app
app = Flask(__name__, template_folder="templates")
socketio = SocketIO(app, cors_allowed_origins="*")

# Route to serve the HTML page
@app.route('/')
def index():
    return render_template("index.html")

@socketio.on('mousemove')
def handle_mouse_move(data):
    """Move mouse relative to the touch movement"""
    dx = data['dx']
    dy = data['dy']
    pyautogui.moveRel(dx, dy)

@socketio.on('leftclick')
def handle_left_click():
    """Simulate a left-click"""
    pyautogui.click()

@socketio.on('rightclick')
def handle_right_click():
    """Simulate a right-click"""
    pyautogui.rightClick()

@socketio.on('zoom')
def handle_zoom(data):
    """Simulate zoom in or out using Ctrl + mouse wheel"""
    if data['dy'] > 0:
        pyautogui.hotkey('ctrl', '+')  # Zoom in
    else:
        pyautogui.hotkey('ctrl', '-')  # Zoom out

if __name__ == '__main__':
    # Ensure the templates folder exists
    if not os.path.exists("templates"):
        os.makedirs("templates")
    
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
