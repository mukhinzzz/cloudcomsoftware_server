import asyncio
import random
import websockets

all_clients = []


async def send_message(message: str):
    for client in all_clients:
        await client.send(message)


async def new_client_connected(client_socket: websockets.WebSocketClientProtocol, path: str):
    print('New client connected')
    all_clients.append(client_socket)

    def generate_number():
        number = str(random.randint(0, 999))
        if len(number) == 1:
            return f'00{number}'

        elif len(number) == 2:
            return f'0{number}'

        else:
            return number

    while True:
        new_message = await client_socket.recv()
        print('New message from a client: ', new_message)
        await send_message(f'{generate_number()}*{generate_number()}')


async def start_server():
    await websockets.serve(new_client_connected, 'localhost', 12345)

if __name__ == '__main__':
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(start_server())
    event_loop.run_forever()
