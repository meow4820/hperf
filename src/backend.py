import multiprocessing, subprocess, os, shutil

def directory():
    try:
        temp = os.path.dirname(os.path.realpath(__file__))
        dir = temp[:-4] # getting a program directory, example: /home/user/hperf/
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

def update_check():
    if os.name != "nt": # works only on Unix-based OSes
        if shutil.which("curl") is None:
            return 3 # curl is not installed
        else:
            if version() == 0:
                return 4 # version isn't detected
            else:
                try:
                    dir = directory()
                    cmd = f"curl https://raw.githubusercontent.com/meow4820/hperf/refs/heads/main/.version >> {dir}/.ver"
                    subprocess.run(cmd, 
                                    shell=True, 
                                    stdout=subprocess.DEVNULL, 
                                    stderr=subprocess.DEVNULL) # getting lastest version
                    with open(f"{dir}/.ver", "r") as rem_ver:
                        if version() in rem_ver:
                            os.remove(f"{dir}/.ver")
                            return 1 # lastest version is already installed
                        else:
                            os.remove(f"{dir}/.ver")
                            return 2 # found newer version
                except Exception as e:
                    return e # some error

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

def cnt(start, end): # counting benchmark
    result = 0
    for i in range(start, end):
        result += 1
    return result

def spd(type, num): # types: 1 - single core, 2 - multi core
    if type == 1: # single core
        res = cnt(0, num)
        if res == num:
            return 1 # success
        else:
            return res # some error
    
    elif type == 2: # multi core
        total = num
        proc = multiprocessing.cpu_count() # cpu cores count
        chunk_size = num // proc # for example, 4 cores and 5,000,000 num - 5 000 000 / 4

        with multiprocessing.Pool(processes=proc) as pool:
            res = pool.starmap(cnt, [(i * chunk_size, (i + 1) * chunk_size
                                    if i != proc - 1 else total)
                                    for i in range(proc)])

        # i * chunk_size - "start" arg for "cnt" func
        # (i + 1) * chunk_size if i != proc - 1 else total - "end" arg for "cnt" func. 
        #                      ^^^^^^^^^^^^^^^^ if else block here for handling the last core

        result = sum(res)

        if result == total:
            return 1 # success
        else:
            return result # some error