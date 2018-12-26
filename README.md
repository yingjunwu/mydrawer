# mydrawer

python scripts for drawing experiment figures.

requirement:

matplotlib-1.3.1

There are some problems (e.g., font) when running the script if the matplotlib library's version is higher than 1.3.1.
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