from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)

@socketio.on('sendSms')
def sendSms(json, methods=['GET', 'POST']):
	print(str(json))
	socketio.emit('sendResponse', 'feedback here', callback='Successfully send sms')

@socketio.on('loadQuickInbox')
def loadQuickInbox(methods=['GET', 'POST']):
	socketio.emit('quickInboxResponse', 'quick inbox data here', callback='Successfully loaded inbox')

@socketio.on('loadUnregisteredInbox')
def loadQuickInbox(methods=['GET', 'POST']):
	socketio.emit('unregisteredInboxResponse', 'unregistered inbox data here', callback='Successfully loaded inbox')

@socketio.on('loadEventInbox')
def loadQuickInbox(methods=['GET', 'POST']):
	socketio.emit('eventInboxResponse', 'event inbox data here', callback='Successfully loaded inbox')

@socketio.on('loadBlockedInbox')
def loadQuickInbox(methods=['GET', 'POST']):
	socketio.emit('blockedInboxResponse', 'blocked inbox data here', callback='Successfully loaded inbox')

if __name__ == '__main__':
    socketio.run(app, host='localhost', port=5000, debug=True)
