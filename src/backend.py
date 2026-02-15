import multiprocessing, subprocess

def get(info):
    ret = ""
    
    if info == 1: # CPU cores
        ret = multiprocessing.cpu_count()
    elif info == 2: # CPU model
        otpt = subprocess.check_output("lscpu | grep 'Model name'", shell=True, text=True)
        model = otpt.replace("Model name:", "").strip()
        ret = model

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