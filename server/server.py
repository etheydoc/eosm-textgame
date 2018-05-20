# This class defines the server for the EOSM text rpg.
# (c) Ethan Block, 2018

from flask import Flask, jsonify, request

class Server:

    def __init__(self, world):
        self.world = world
