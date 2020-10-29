# MAD-mazes


![Alt Text](./mazes/tiny.gif)

### Dependencies and Building
This project has python module dependencies which can be installed from PyPI, as well as extension modules which need to be installed in a virutal enviornment.

**First create and activate the virtual enviornment:**

```$ python3 -m venv venv```

**For Mac/Linux:**

```$ source ./venv/bin/activate```

**For Windows:**

```C> venv\Scripts\activate.bat ```

**Install dependencies via PyPI:**

```$ pip install -r requirements.txt```

**Finally build and install the extension modules in the virtual enviornment:**

```$ python setup.py install```

Now you can run the program!

```$ python main.py```

### Usage
When run without any arguments the program will run in GUI mode.

Below are the command-line options that are available.
```
usage: main.py [-h] [-p PATH] [-g] [--dijkstras] [--DFS]

optional arguments:
  -h, --help            show this help message and exit
  -p PATH, --path PATH  the path to the file(s) to solve
  -g, --gif             write out result as gif instead of png
  --dijkstras           solve using dijkstras algorithm
  --DFS                 solve using DFS
```
