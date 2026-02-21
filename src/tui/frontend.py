import os, time
import bck.helper as help
import bck.upd as updater
import bck.bench as bench
import bck.config as cfg

version = ""

def update():
    os.system("clear||cls")
    print("Checking for updates...")
    upd = updater.check()
    if upd == 2:
        print("Update detected!\nYou can download the newest version from GitHub" +
            "\nhttps://github.com/meow4820/hperf")
        print("\nPress ENTER to continue...")
        input()

    elif upd == 1:
        print("Lastest version is already installed")
        time.sleep(0.5)

    elif upd == 3:
        print("Update failed :(\n\n" +
              "curl is not installed!\n\n" +
              "Press ENTER to continue...")
        input()

    elif upd == 4:
        print("Update failed :(\n\n" +
              "Cannot open .version file\n\n" +
              "Press ENTER to continue...")
        input()
    
    else:
        print(f"Update failed :(\n\n" +
               "{upd}\n\n" +
               "Press ENTER to continue...")
        input()

def b_result(avg_t, pts, type, tests): # benchmark result
    os.system("clear||cls")
    print("============== Results ==============")
    print(f"\nTest type: {type}, {tests} test(s)" +
            f"\nAverage time: {round(avg_t, 3)} sec" +
            f"\nPoints: {round(pts, 1)} pts")
    print("\n\nPress ENTER to continue")
    input()

def benchmark(type, tests):
    if cfg.get("show_test_warning"):
        os.system("clear||cls")
        print("============== WARNING ==============")
        print("For better accuracy, you need to close all heavy apps!")
        print("Press ENTER to continue...")
        input()

    if type == 1: # single core
        os.system("clear||cls")

        time_total = 0

        for test in range(tests):
            os.system("clear||cls")
            print(     "============= Single-core test =============")
            if test != 9:
                print(f"============= {test + 1} / 10 =======================")
            elif test == 9: # handling the last test
                print(f"============= {test + 1} / 10 ======================")
            if cfg.get("show_cpu_freq") == 1:
                print(f"\nCPU average freq: {help.get.avg_cpu_freq()} MHz\n\n")
            start = time.time() # test start time
            bench.spd(1, 25_000_000)
            end = time.time() # test end time
            time_total += (end - start)

        time_avg = (time_total / tests)
        points = 10_000 / time_avg

        os.system("clear||cls")
        b_result(time_avg, points, "Single-core", tests)

    elif type == 2: # multi core
        os.system("clear||cls")

        time_total = 0

        for test in range(tests):
            os.system("clear||cls")
            print( "============= Multi-core test ==============")
            if test != 9:
                print(f"============= {test + 1} / 10 =======================")
            elif test == 9: # handling the last test
                print(f"============= {test + 1} / 10 ======================")
            if cfg.get("show_cpu_freq") == 1:
                print(f"\nCPU average freq: {help.get.avg_cpu_freq()} MHz\n\n")
            start = time.time()
            bench.spd(2, 25_000_000)
            end = time.time()
            time_total += (end - start)

        time_avg = (time_total / tests)
        points = 10_000 / time_avg

        os.system("clear||cls")
        b_result(time_avg, points, "Multi-core", tests)
    
    mm(False)

def mm(check_update):
    version = help.version()

    if check_update and cfg.get("check_for_updates") == 1:
        update()
    
    os.system("clear||cls")
    print("=============== hPerf ===============")
    print("\nSelect test type:\n\n" +
            "1. Single-core test\n" +
            "2. Multi-core test\n\n" +
            
            "3. Information\n" +
            "4. Exit")
    ans = input("\n>> ")

    if ans == "1": # single core
        benchmark(1, 10)

    elif ans == "2": # multi core
        benchmark(2, 10)

    elif ans == "3":
        os.system("clear||cls")
        print(     "============ Information ============")
        print(  f"\nCPU cores: {help.get.cpu_cores()}")
        if cfg.get("show_cpu_model") == 1:
            print(    f"CPU model: {help.get.cpu_model()}")
        print(  f"\nProgram version: {version}")
        print(    f"Program directory {help.directory()}")
        print(    f"Python version: {help.get.py_ver()}")

        print("\n\nPress ENTER to continue...\n")
        input()
        mm(False)

    elif ans == "4": # exit
        os.system("clear||cls")
        exit()