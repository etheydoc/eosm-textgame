# The client for the Ethan & Owen's Splendiferous Misadventures RPG,
# a multiplayer interactive fiction game.
# (c) Ethan Block, 2018

import dice, entity, item, room
import requests, jsonpickle, argparse

class Client:

    def __init__(self, host='127.0.0.1', port=5000):
        self.host = host
        self.port = port
        self.world = jsonpickle.decode(requests.get("http://"+host+":"+str(port)+"/world/get").json())
        self.player = entity.Player(input("What's your name? "), 20, 10, {}, 0)
        self.world.start.entities.append(self.player)
        requests.post("http://"+host+":"+str(port)+"/world/set", data=jsonpickle.encode(self.world))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="EOSM Text RPG v0.1")
    parser.add_argument('-h', help="Server host", dest="host", default="127.0.0.1")
    parser.add_argument('-p', help="Server port", dest="port", type=int, default=5000)
    opts = parser.parse_args()

    Client(host=opts.host, port=opts.port)
