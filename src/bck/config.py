import json, os
import bck.helper as help

def get(data):
    with open(f"{help.directory()}/config.json", "r") as cfg:
        f = json.load(cfg)

    if data == "update":
        return f["check_for_updates"]

    elif data == "warning":
        return f["show_test_warning"]

    elif data == "cpu_model":
        return f["show_cpu_model"]

    elif data == "setup":
        return f["setup_on_startup"]

def set(data, value):
    with open(f"{help.directory()}/config.json", "r") as cfg:
        f = json.load(cfg)

    f[data] = value

    with open(f"{help.directory()}/config.json", "w") as cfg:
        json.dump(f, cfg)