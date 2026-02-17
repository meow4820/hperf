import os, subprocess, multiprocessing

def directory():
    try:
        temp = os.path.dirname(os.path.realpath(__file__))
        dir = temp[:-8] # getting a program directory, example: /home/user/hperf/
        return dir    
    except:
        return 0

def version():
    if directory() == 0:
        return 0
    else:
        dir = directory()

        try:
            with open(f"{dir}/.version", "r") as ver:
                version = ver.read() # getting a program version (in .version)
                return version
        except:
            return 0

def get(info):
    ret = ""
    
    if info == 1: # CPU cores
        ret = multiprocessing.cpu_count()
    elif info == 2: # CPU model
        otpt = subprocess.check_output("lscpu | grep 'Model name'", shell=True, text=True)
        model = otpt.replace("Model name:", "").strip()
        ret = model
    elif info == 3: # Python version
        otpt = subprocess.check_output("python --version", shell=True, text=True)
        version = otpt.replace("Python", "").strip()
        ret = version  

    return ret