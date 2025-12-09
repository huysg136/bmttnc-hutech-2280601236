import tornado.ioloop
import tornado.websocket
import asyncio

class WebSocketClient:
    def __init__(self, io_loop):
        self.connection = None
        self.io_loop = io_loop
        self.url = "ws://localhost:8888/websocket/"

    def start(self):
        self.connect_and_read()

    def stop(self):
        self.io_loop.stop()

    def connect_and_read(self):
        print("Client: Reconnecting...")
        tornado.websocket.websocket_connect(
            url=self.url,
            callback=self.maybe_retry_connection, 
            on_message_callback=self.on_message, 
            ping_interval=10,
            ping_timeout=30,
        )

    def maybe_retry_connection(self, future):
        try:
            self.connection = future.result()
            print("Client: Connection established.")
        except Exception as e:
            print(f"Client: Could not connect: {e}, retrying in 3 seconds...")
            self.io_loop.call_later(3, self.connect_and_read)

    def on_message(self, message):
        if message is None:
            print("Client: Disconnected, reconnecting...")
            self.connection = None
            self.connect_and_read()
            return

        print(f"Client: Received word from server: {message}")
        
        if self.connection:
             self.connection.read_message(callback=self.on_message)

def main():
    io_loop = tornado.ioloop.IOLoop.current()
    client = WebSocketClient(io_loop)
    
    io_loop.add_callback(client.start)
    
    print("Client: Starting I/O loop...")
    io_loop.start()

if __name__ == "__main__":
    main()