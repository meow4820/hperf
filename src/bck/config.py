import json, os
import bck.helper as help

def get(data):
    with open(f"{help.directory()}/config.json", "r") as cfg:
        f = json.load(cfg)

    return f[data]

def set(data, value):
    with open(f"{help.directory()}/config.json", "r") as cfg:
        f = json.load(cfg)

    f[data] = value

    with open(f"{help.directory()}/config.json", "w") as cfg:
        json.dump(f, cfg)