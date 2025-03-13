import asyncio
import websockets


connected_clients = set()


async def handle_client(websocket):
    
    connected_clients.add(websocket)
    try:
        
        async for message in websocket:
            print(f"Received message: {message}")  
            await asyncio.gather(
                *(client.send(message) for client in connected_clients if client != websocket),
                return_exceptions=True
            )
    except websockets.exceptions.ConnectionClosed:
        print("Client disconnected")
    finally:
        
        connected_clients.discard(websocket)


async def main():
    async with websockets.serve(handle_client, "localhost", 12345):
        print("WebSocket server running on ws://localhost:12345")
        await asyncio.Future()  


if __name__ == "__main__":
    asyncio.run(main())