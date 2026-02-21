import bck.config as cfg
import tui.frontend as frt
import os

def main():
    os.system("clear||cls")

    print(      "=============== Setup ===============")
    print(    "\nWelcome to hPerf!\n" +
                "Do you want to enable checking for updates?\n")
    ans = input("(Y/n) >> ")

    if ans.lower() == "n":
        cfg.set("check_for_updates", 0)

    else:
        cfg.set("check_for_updates", 1)

    os.system("clear||cls")

    if os.name != "nt":
        print(      "=============== Setup ===============")
        print(    "\nShow CPU model in \"information\" tab?\n" +
                    "If you're on Windows, this will not work\n")

        ans = input("(Y/n) >> ")

        if ans.lower() == "n":
            cfg.set("show_cpu_model", 0)

        else:
            cfg.set("show_cpu_model", 1)

    os.system("clear||cls")

    if os.name != "nt":
        print(      "=============== Setup ===============")
        print(    "\nShow CPU frequency while in test?\n" +
                  "If you're on Windows, this will not work\n")

        ans = input("(Y/n) >>")

        if ans.lower() == "n":
            cfg.set("show_cpu_freq", 0)

        else:
            cfg.set("show_cpu_freq", 1)

    cfg.set("setup_on_startup", 0)

    frt.mm(False) 