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

class get:
    def cpu_cores():
        ret = multiprocessing.cpu_count()
        return ret

    def cpu_model():
        otpt = subprocess.check_output("lscpu | grep 'Model name'", shell=True, text=True)
        model = otpt.replace("Model name:", "").strip()
        ret = model
        return ret

    def py_ver():
        otpt = subprocess.check_output("python --version", shell=True, text=True)
        version = otpt.replace("Python", "").strip()
        ret = version
        return ret

    def avg_cpu_freq():
        otpt = subprocess.check_output("cat /proc/cpuinfo", shell=True, text=True)
        lines = otpt.split("\n")

        freq_l = [line for line in lines if 'MHz' in line]

        freq_arr = []

        for line in freq_l:
            prt = line.split(":")
            value = float(prt[1].strip())
            freq_arr.append(value)

        freq_avg = 0
        freq_total = 0
        index = 0

        for i in freq_arr:
            freq_total += freq_arr[index]
            index += 1

        freq_avg = int(round((freq_total / (get.cpu_cores())), 0))

        return freq_avg