import backend, os, time

version = ""

def start():
    version = backend.version()

    os.system("clear||cls")
    print("Checking for updates...")
    upd = backend.update_check()
    if upd == 2:
        print("Update detected!\nYou can download the newest version from GitHub" +
            "\nhttps://github.com/meow4820/hperf")
        print("\n Press ENTER to continue...")
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

    while True:
        os.system("clear||cls")
        print("=============== hPerf ===============")
        print("\nSelect test type:\n\n" +
                "1. Single-core test\n" +
                "2. Multi-core test\n\n" +
                
                "3. Information\n" +
                "4. Exit")
        ans = input("\n>> ")

        if ans == "1": # single core
            os.system("clear||cls")
            print("============== WARNING ==============")
            print("For better accuracy, you need to close all heavy apps!")
            print("Press ENTER to continue...")
            input()

            time_total = 0

            for test in range(10):
                os.system("clear||cls")
                print(     "============= Single-core test =============")
                if test != 9:
                    print(f"============= {test + 1} / 10 =======================")
                elif test == 9: # handling the last test
                    print(f"============= {test + 1} / 10 ======================")
                start = time.time() # test start time
                backend.spd(1, 25_000_000)
                end = time.time() # test end time
                time_total += (end - start)

            time_avg = (time_total / 10)
            points = 10_000 / time_avg

            os.system("clear||cls")
            print("============== Results ==============")
            print(f"\nTest type: Single-core, 10 tests" +
                  f"\nAverage time: {round(time_avg, 3)} sec" +
                  f"\nPoints: {round(points, 1)} pts")
            print("\n\nPress ENTER to continue")
            input()

        elif ans == "2": # multi core
            os.system("clear||cls")
            print("============== WARNING ==============")
            print("For better accuracy, you need to close all heavy apps!")
            print("Press ENTER to continue...")
            input()
            time_total = 0

            for test in range(10):
                os.system("clear||cls")
                print( "============= Multi-core test ==============")
                if test != 9:
                    print(f"============= {test + 1} / 10 =======================")
                elif test == 9: # handling the last test
                    print(f"============= {test + 1} / 10 ======================")
                start = time.time()
                backend.spd(2, 25_000_000)
                end = time.time()
                time_total += (end - start)

            time_avg = (time_total / 10)
            points = 10_000 / time_avg

            os.system("clear||cls")
            print("============== Results ==============")
            print(f"\nTest type: Multi-core, 10 tests" +
                  f"\nAverage time: {round(time_avg, 3)} sec" +
                  f"\nPoints: {round(points, 1)} pts")
            print("\n\nPress ENTER to continue")
            input()

        elif ans == "3":
            os.system("clear||cls")
            print(     "============ Information ============")
            print(  f"\nCPU cores: {backend.get(1)}")
            print(    f"CPU model: {backend.get(2)}")
            print(  f"\nProgram version: {version}")
            print(    f"Program directory {backend.directory()}")

            print("\n\nPress ENTER to continue...\n")
            input()

        elif ans == "4": # exit
            os.system("clear||cls")
            exit()