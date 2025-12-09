import random
import tornado.ioloop
import tornado.web
import tornado.websocket

class WebSocketServer(tornado.websocket.WebSocketHandler):
    clients = set()
    def open(self):
        print("A client connected.")
        WebSocketServer.clients.add(self)

    def on_close(self):
        print("A client disconnected.")
        WebSocketServer.clients.remove(self)

    @classmethod
    def send_message(cls, message: str):
        print(f"Sending message '{message}' to {len(cls.clients)} client(s).")
        for client in cls.clients:
            client.write_message(message)

class RandomWordSelector:
    def __init__(self, word_list):
        self.word_list = word_list

    def sample(self):
        return random.choice(self.word_list)

def main():
    app = tornado.web.Application([
        (r"/websocket/", WebSocketServer),
    ],
    websocket_ping_interval=10, 
    websocket_ping_timeout=30, 
    )
    
    app.listen(8888)

    io_loop = tornado.ioloop.IOLoop.current()

    word_selector = RandomWordSelector(['apple', 'banana', 'orange', 'grape', 'melon'])

    periodic_callback = tornado.ioloop.PeriodicCallback(
        callback=lambda: WebSocketServer.send_message(word_selector.sample()),
        callback_time=3000
    )
    periodic_callback.start()
    
    print("WebSocket Server started on port 8888. Sending random words every 3 seconds.")
    io_loop.start()

if __name__ == "__main__":
    main()