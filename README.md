# maze-solver

An automatic maze solver built in Python

## Purpose

This purpose of this project was to put into practice some of the things I've
been learning about data structures and algorithms in the
[Boot.dev](https://www.boot.dev) curriculum.  It was a lot of fun to make,
especially since it was the first time I implemented a GUI with one of my
projects.

## Installation

Simply clone the repository to your system with `git clone
https://github.com/wtwingate/maze-solver`. No third-party dependencies
required! 

NOTE: The GUI is implemented using Python's `tkinter` module. This is normally
included with most installations of Python, but not all. If you run into
problems, this is the most likely culprit.

## Usage

To run the program, simply `cd` into the directory and run `python3
src/main.py`. Alternatively, you can run the included shell script `./main.sh`.
Then, sit back and watch with _amazement_ as the maze automagically creates and
solves itself using the power of the [depth-first
search](https://en.wikipedia.org/wiki/Depth-first_search) algorithm!

You can tinker around with settings in `main.py` to create mazes of different
shapes and sizes. Have fun!
