import asyncio
import zmq


class Server:
    def __init__(self, port_listen, port_speak):
        listen_context = zmq.Context()
        self.socket_listen = listen_context.socket(zmq.SUB)
        self.socket_listen.bind("tcp://*:%s" % port_listen)
        self.socket_listen.setsockopt_string(zmq.SUBSCRIBE, '')

        speak_context = zmq.Context()
        self.socket_speak = speak_context.socket(zmq.PUB)
        self.socket_speak.bind("tcp://*:%s" % port_speak)

    async def listen(self, timeout=0.01):
        while True:
            try:
                socket_data = self.socket_listen.recv_json(flags=zmq.NOBLOCK)
                print(socket_data)
            except zmq.Again:
                await asyncio.sleep(timeout)

    async def speak(self, timeout=1):
        while True:
            self.socket_speak.send_json({'server': 'heart'})
            await asyncio.sleep(timeout)

if __name__ == '__main__':

    server = Server(9090, 9080)
    tasks = [
        server.listen(),
        server.speak(),
    ]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()