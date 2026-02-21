# Launcher for hPerf

import tui.frontend as frt
import tui.setup as set
import bck.config as cfg

if __name__ == "__main__":
    if cfg.get("setup_on_startup") == 1:
        set.main()

    else:
        frt.mm(1)