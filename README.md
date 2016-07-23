## Overview
This is a simple tool to parse large log files by itterating through log lines using multiple processes.  It only supports nginx logs currently.

## Installation
____________

`python setup.py install`


## Run Tests

`nosetests`


## Usage
```
logparser -h
Log parser - A simple tool to aggregate log entries.

Usage:
  logparser nginx <file>
  logparser --version

Options:
  -h --help     Show this screen.
  --verbose  Verbosity level [default: False].
  ```

## Example
  `$ logparser nginx /path/to/your/log`
