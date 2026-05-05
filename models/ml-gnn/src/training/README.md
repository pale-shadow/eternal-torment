# Training Stuff

## Execution

from the top level of the repo

```sh
make python
. _build/bin/activate.fish
PYTHONPATH='.' python src/training/training.py
```

A log file named `training.log` is generated.

## Properties

- An edge in a connected graph is called a `bridge` if the removal of that edge, but not its end vertices, makes the graph disconnected.
- A graph with no cycles is an `acyclic graph`, also called a `forest`.
- A connceted forest is a `tree`.
- To determine whether a graph is connected we use an algorithm such as a `depth-first search`.
