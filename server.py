from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from websocket import WebSocketApp

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('my_event')
def test_message(message):
    print('Received my_event with data:', message['data'])
    # do something with the data

    response_data = { 'status': 'success' }
    emit('my_response', response_data)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
