from flask import Flask
from flask_websockets import WebSockets
import random

app = Flask(__name__)
sockets = WebSockets(app)


@sockets.on_message
def create_message(message):
    if message == 'Generate number':
        return f'{generate_number()}*{generate_number()}'
    else:
        return 'Неизвестная команда'


def generate_number():
    number = str(random.randint(0, 999))
    if len(number) == 1:
        return f'00{number}'

    elif len(number) == 2:
        return f'0{number}'

    else:
        return number


if __name__ == '__main__':
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler
    server = pywsgi.WSGIServer(
        ('localhost', 12345), app, handler_class=WebSocketHandler)
    server.serve_forever()
