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

Credits
-------
The "Daemon" class code (in battd.py) is licensed under CC BY-SA 3.0 and was written by Sander Marechal, original article:
[A simple unix/linux daemon in Python](http://www.jejik.com/articles/2007/02/a_simple_unix_linux_daemon_in_python/)