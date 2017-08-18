battd
=====
This is a simple daemon for battery status monitoring and stat plotting.

Usage
-----
Controlling daemon:
```
    $ python battd.py start
    $ python battd.py stop
    $ python battd.py restart
```
Plot battery charge stats:
```
    $ python battplot.py
```
Plotting includes basic discharge prediction function.

(For stat plotting function to work, matplotlib Python module is required)

Known bugs:
-----------
* Rotating battery log removes previous one, so plotting features are not available right after log rotation (Can be fixed by either keeping last N entries or increasing log size).
* Log rotations are not synchronized with Charging/Discharging state transitions. Logs should only be rotated when transitioning from Charging -> Discharging.

Credits
-------
The "Daemon" class code (in battd.py) is licensed under CC BY-SA 3.0 and was written by Sander Marechal, original article:
[A simple unix/linux daemon in Python](http://www.jejik.com/articles/2007/02/a_simple_unix_linux_daemon_in_python/)