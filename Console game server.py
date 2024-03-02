#!/usr/bin/env python

import asyncio
import ast

from websockets.server import serve

players = {}

async def handler(websocket):
    print('New player connecting...')
    await websocket.send('hello!')

    name = await websocket.recv()

    print(f'{name} just joined!')

    players[name] = {'x': 0, 'y': 0}
    
    async for message in websocket:
        print(message)
        await websocket.send('a')

async def main():
    async with serve(handler, "localhost", 7000):
        await asyncio.Future()  # run forever

asyncio.run(main())
