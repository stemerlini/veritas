import os
from flask import Flask, render_template
import websockets
import asyncio
import threading
from veritas.utils.graph import generate_graph_json

app = Flask(__name__, static_folder="static", template_folder="templates")

@app.route("/")
def index():
    return render_template("index.html")

async def websocket_server(websocket, path):
    while True:
        # Send graph updates
        graph_data = generate_graph_json(".")
        await websocket.send(graph_data)
        await asyncio.sleep(1)  # Simulate real-time updates

def start_websocket_server():
    asyncio.get_event_loop().run_until_complete(
        websockets.serve(websocket_server, "localhost", 8765)
    )
    asyncio.get_event_loop().run_forever()

def start_web_app():
    # Start WebSocket server in a separate thread
    websocket_thread = threading.Thread(target=start_websocket_server)
    websocket_thread.daemon = True
    websocket_thread.start()

    # Start Flask app
    app.run(port=8000)

if __name__ == "__main__":
    start_web_app()