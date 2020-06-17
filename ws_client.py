# WS server example that synchronizes state across clients

import asyncio
import json
import logging
import websockets

import buddy_manager

logging.basicConfig()

STATE = {"value": 0}
JSON = {"wingle": "middle", "wing": "low", "heart": False, "color": "NOCOLOUR", "value": 0}
USERS = set()

global websockets


def state_event():
    return json.dumps({"type": "state", **JSON})


def users_event():
    return json.dumps({"type": "users", "count": len(USERS)})


async def notify_state():
    if USERS:  # asyncio.wait doesn't accept an empty list
        message = state_event()
        print(message)
        await asyncio.wait([user.send(message) for user in USERS])


async def notify_users():
    if USERS:  # asyncio.wait doesn't accept an empty list
        message = users_event()
        await asyncio.wait([user.send(message) for user in USERS])


async def register(websocket):
    USERS.add(websocket)
    await notify_users()


async def unregister(websocket):
    USERS.remove(websocket)
    await notify_users()


async def counter(websocket, path):
    # register(websocket) sends user_event() to websocket
    await register(websocket)
    try:
        await websocket.send(state_event())
        async for message in websocket:
            data = json.loads(message)
            if data["action"] == "minus":
                JSON["value"] -= 1
                await notify_state()
            elif data["action"] == "plus":
                JSON["value"] += 1
                await notify_state()
            else:
                logging.error("unsupported event: {}", data)
    finally:
        await unregister(websocket)


def stsrv():
    start_server = websockets.serve(counter, "192.168.0.60", 6789)

    loop = asyncio.get_event_loop()

    loop.run_until_complete(start_server)
    loop.run_forever()

