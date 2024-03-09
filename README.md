# python-monorepo-evolution

An opinionated repo demonstrating the evolution from Jupyter notebook to
micro-service in a python monorepo.

This repo demonstrates how to develop a very simple service starting by sketching
the core implementation as a Jupyter notebook and then growing the repo to contain
a library and a micro-service.

# Technologies

This repo contains a highly opinionated selection of libs, tools, ... The following
list shows the main ingredients:

* Python 3.12
* Jupyter Notebook (for doing the initial sketch)
  * `matplotlib` is used in the notebook to "proof" the randomness is suitable
* `poetry` to manage packages and dependencies
* `pytest` for writing automated tests
* `FastAPI` to implement the RESTful-API
* `hypercorn` to run the service
* `docker` to build a container image

# Steps

Each evolutionary step is stored in a separate branch:

* `step/01-jupyter-notebook` contains the Jupyter notebook sketching the first
  draft
* `step/02-cli` contains a small cli application based on the sketch

# Use Case

The story behind this repo is to create a service to roll a die or multiple dice
for use with table-top role playing games. A roll is described using an input
string (see below) and must be "executed" by the application.

## Input specs

A RPG dice roller expression follows the following syntax:

```
[<dice count>]d<die num>[(+|-)<mod>]
```

* `dice count` is an optional (positive) number defining how many dice to roll (or how often to roll a single die and sum up the results)
  This number is optional. If not given defaults to 1.
* `die num` defines the number of sides the die must have. Valid numbers are 2, 3, 4, 6, 8, 10, 12, 20, 50 and 100
* `mod` defines a modifier to apply - a fixed number to either add or subtract from the die/dice roll result.
  `mod` and its preceding sign are optional (either sign and number are given or none of them). If no modifier has been given it defaults to 0.

### Examples

* `d20` means to roll a single 20-sided die
* `d20+2` means to roll a single 20-sided die and add `2` to the result
* `3d8-5` means to roll three eight-sided dice, add their numbers and subtract `5` from the result

## Natural result

For some of the rolls it is important to know what the _natural result_ is. The natural result is the result of the die/dice w/o applying the modifier.
I.e. when rolling `d20+2` a _natural one_ is ususally considered a _disaster_ where a _natural 20_ is a _triumphal success_.

