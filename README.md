# mydrawer

python scripts for drawing experiment figures.

Requirement:

```
matplotlib-1.3.1
```

There are some problems (e.g., font) when running the script with matplotlib's version higher than 1.3.1.
If you have installed a higher version, please do the following:

```
pip uninstall matplotlib
pip install matplotlib==1.3.1
```

To check matplotlib's version, open your python shell, and then type in:
```
import matplotlib
print(matplotlib.__version__)
```

The code has been tested in the following environments:
```
macOS Mojave (10.14), python 2.7
Ubuntu 16.04, python 2.7
```

It is known that the code does not work with `virtualenv`, due to certain problems with matplotlib.

TODO: refactor the code to work with the latest `matplotlib` library.
