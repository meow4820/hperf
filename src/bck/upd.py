import subprocess, shutil, os
import bck.helper as help

def check():
    if os.name != "nt": # works only on Unix-based OSes
        if shutil.which("curl") is None:
            return 3 # curl is not installed
        else:
            if help.version() == 0:
                return 4 # version isn't detected
            else:
                try:
                    dir = help.directory()
                    cmd = f"curl https://raw.githubusercontent.com/meow4820/hperf/refs/heads/main/.version >> {dir}/.ver"
                    subprocess.run(cmd, 
                                    shell=True, 
                                    stdout=subprocess.DEVNULL, 
                                    stderr=subprocess.DEVNULL) # getting lastest version
                    with open(f"{dir}/.ver", "r") as rem_ver:
                        if help.version() in rem_ver:
                            os.remove(f"{dir}/.ver")
                            return 1 # lastest version is already installed
                        else:
                            os.remove(f"{dir}/.ver")
                            return 2 # found newer version
                except Exception as e:
                    return e # some error