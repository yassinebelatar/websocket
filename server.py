from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from simple_websocket import WebSocket

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, websocket=WebSocket)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('my_event')
def test_message(message):
    emit('my_response', {'data': message['data']})

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
