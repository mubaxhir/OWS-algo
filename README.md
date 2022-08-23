# geneural.net

## Table of Contents

- [Introduction](#introduction)
- [Setup](#setup)
- [How to run](#how-to-run)
- [Contributing](#contributing)

## Introduction

A re-implementation of 3D Tetris, along with a genetic programming algorithm that steadily improves its performance of playing the game.

Includes visualizations through a chart and replays of "fit" individuals in each generation.

## Setup

Node is required to run the simulation. Python 2 is required to run the genetic algorithm. Python 3 is required to run the web server

### Dependencies

* [Python 3.5](https://www.python.org/downloads/) or higher (for web server and for genetic algorithm), and also python-pip

* [Node 8](https://nodejs.org/en/download/current/) (for simulation)

### Setup Instructions

* Clone the repository and change directory to it.

* Set up Python virtual environment. **Also make sure that your working directory has no spaces in it.**

```bash
python -m venv venv
```

* Set up NPM dependencies.

```bash
cd simulation
npm install
```

## How to run

**To go into a virtual environment: (Linux/Mac) `source venv/bin/activate` (Windows) `venv\Scripts\activate`**

### Running the genetic algorithm

**To run, you need two terminals.**

1. `cd simulation && node index.js`

2. `python genetic/genetic_algorithms.py`

Genetic algorithm will run until 1000 generations by default. This can be configured in `genetic_algorithm.py`.

### Running the web server

1. `python3 genetic/webserver.py`

Server will be visible, by default, on [port 80 on localhost](http://localhost:80). You can compare it to our [web server](http://geneural.net) for reference.

The web server hosts data files which consist of a csv file (generations vs score) and a json file (replay data) which configure the `ai` endpoint. The `/` endpoint lets you play the game on a browser with WebGL and ES6 support.

## Contributing

Pull requests will always be welcome!

### To-do

[ ] Use a transpiler for older browser support
[ ] Improve genetic algorithm
[ ] Alternate views for the 3D Tetris game
[ ] Improve documentation
[ ] Add testing
[ ] And more...
