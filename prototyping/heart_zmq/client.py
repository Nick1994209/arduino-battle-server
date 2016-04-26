import asyncio
import random
import zmq


class Client:
    def __init__(self, client_id, host, port_speak, port_listen):
        self.id_client = client_id

        speak_context = zmq.Context()
        self.socket_speak = speak_context.socket(zmq.PUB)
        self.socket_speak.connect("tcp://{0}:{1}".format(host, port_speak))

        listen_context = zmq.Context()
        self.socket_listen = listen_context.socket(zmq.SUB)
        self.socket_listen.connect("tcp://{0}:{1}".format(host, port_listen))
        self.socket_listen.setsockopt_string(zmq.SUBSCRIBE, '')

    async def listen(self, timeout=0.01):
        while True:
            socket_data = self.socket_listen.recv_json()
            print(socket_data)
            await asyncio.sleep(timeout)

    async def speak(self, timeout=1):
        while True:
            self.socket_speak.send_json({'id': self.id_client})
            await asyncio.sleep(timeout)


if __name__ == '__main__':
    id_client = random.randint(1000, 8000)
    host = 'localhost'
    client = Client(id_client, host, 9090, 9080)
    tasks = [
        client.listen(),
        client.speak(),
    ]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()