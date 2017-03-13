
from channels.routing import route
from talk.consumers import  ws_disconnect,ws_connect
from channels.routing import route

channel_routing = [
    route("websocket.connect", ws_connect),
#    route("websocket.receive", ws_message),
    route("websocket.disconnect", ws_disconnect),
]
