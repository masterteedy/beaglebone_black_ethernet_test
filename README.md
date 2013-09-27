BeagleBone Black Ethernet Test
==============================

Ethernet fails to come up sometimes when power is applied.

This script cycles power on a Web Power Switch[1] networked power switch and attempts to SSH into the BeagleBoard Black to see if network came up properly.  It may be useful to connect a serial cable to the BeagleBone Black to explore in the failed state.

[1] http://www.digital-loggers.com/lpc.html

python-dlipower may have to be installed from source:
https://github.com/dwighthubbard/python-dlipower
